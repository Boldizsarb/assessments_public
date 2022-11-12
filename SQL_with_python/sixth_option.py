
import third_option
import datetime
import random

order_idlist = [] # captures the oreder id succesfully
ordered_products =[]

current_basket_id = []

# this needs to run first after the making alist
def shopper_orders(shopperid): #
    #  inserting a new row into the shpooer_order table for the basket with a status of ‘Placed’
    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")

    curr_date = datetime.date.today().strftime("%Y-%m-%d")
    order_status = "Placed"
    order_id = random.randrange(0, 9999999, 1)

    sql_insert = "INSERT INTO shopper_orders VALUES (?,?,?,?)"
    cursor.execute(sql_insert, (order_id, shopperid, curr_date, order_status,))
    db.commit()
    order_idlist.append(order_id)
    return order_id

# it returns the order id
something = []
# recreating a basket view with the right values
def making_alist(shopperid): # inserting the rows into ordered products
    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "select basket_contents.product_id, product_sellers.seller_id, basket_contents.quantity, basket_contents.price\
                FROM basket_contents INNER JOIN product_sellers ON product_sellers.product_id = basket_contents.product_id\
                INNER JOIN shopper_baskets ON shopper_baskets.basket_id = basket_contents.basket_id\
                WHERE shopper_baskets.shopper_id = ?"
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.execute(sql_query, (shopperid,))
    status = "Placed"
    all_row = cursor.fetchall()
    for row in all_row:

        productid= row[0]
        sellerid = row[1]
        qty = row[2]
        price = row[3]

        thistuple = (order_idlist[0], row[0], row[1], row[2], row[3], status)
        #ordered_products.append(order_idlist[0])
        #ordered_products.append(row)
        #ordered_products.append(status)
        ordered_products.append(thistuple)
        try:
            sql_insert = "INSERT INTO ordered_products (order_id, product_id, seller_id, quantity, price, ordered_product_status) VALUES (?,?,?,?,?,?)"
            cursor.execute(sql_insert, (order_idlist[0], productid, sellerid, qty, float(price), status,))
        except sqlite3.IntegrityError:
            #print("integrity error")
            pass
        # working hahaaaaa
    db.commit()
    db.close()

def returning_basket_id(shopperid):
    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    # finding the basket id of the shopperid
    sql_query = "SELECT basket_id FROM shopper_baskets WHERE shopper_id == ?"
    cursor.execute(sql_query, (shopperid,))
    one_row = cursor.fetchone()
    current_basket_id.append(one_row[0])





# when deleting it needs to be called first




def deleting_basket_contents(basketid): # call this first

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_delete = "DELETE FROM basket_contents WHERE basket_id == ?"
    cursor.execute(sql_delete, (basketid,))
    db.commit()
    db.close()
    #print("deleted basket content")


#deleting_basket_contents(10000) # works

def deleting_shopper_baskets(basketid): # call this second due to the primary key constraint

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_delete2 = "DELETE FROM shopper_baskets WHERE basket_id == ?"
    cursor.execute(sql_delete2, (basketid,))
    db.commit()
    db.close()
    #print("deleted shopper baskets")
#deleting_shopper_baskets(10000)



def checkout(shopperid):
    third_option.displaying_basket(shopperid) # displaying the basket if there is any

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    sql_query = "SELECT products.product_description, sellers.seller_name, basket_contents.quantity, basket_contents.price, SUM(basket_contents.quantity*basket_contents.price)\
                        FROM basket_contents INNER\
                        JOIN sellers ON sellers.seller_id = basket_contents.seller_id\
                        INNER JOIN products ON products.product_id = basket_contents.product_id\
                        INNER JOIN shopper_baskets on shopper_baskets.basket_id = basket_contents.basket_id\
                        WHERE shopper_baskets.shopper_id = ?\
                        GROUP BY basket_contents.product_id "

    cursor.execute(sql_query, (shopperid,))

    one_row = cursor.fetchone()

    if one_row is not None: # if there is a basket
        print("Would you like to proceed with the checkout (Y or N) ?")
        proceed = input()

        if proceed == "y":
            #  inserting a new row into the shpooer_order table for the basket with a status of ‘Placed’
            shopper_orders(shopperid) # creating order id
            making_alist(shopperid)  # inserting the items to the database
            returning_basket_id(shopperid)
            deleting_basket_contents(current_basket_id[0])
            deleting_shopper_baskets(current_basket_id[0])
            print("Checkout is complete, your order has been placed. ")
            # dont run it, it makeing entry

        elif proceed == "n":
           pass
        else:
            pass
    else:
        pass
    db.close()





# working dont run it because the stuff from the shopper_orders cant be deleted due to foreign key constraint

# Entry making: works perfectly
#shopper_orders(shopperid=10001)
#making_alist(shopperid=10001)
#returning_basket_id(10000)
#print(current_basket_id[0])
#deleting_basket_contents(current_basket_id[0])
#deleting_shopper_baskets(current_basket_id[0])

"""""
import sqlite3

db_file = "/Users/boldizsarbanfia/Documents/University/Database/Assessment/Database/Assessment.db"
db = sqlite3.connect(db_file)
cursor = db.cursor()
cursor.execute("PRAGMA foreign_keys=ON")
for item in ordered_products:
    sql_insert = "INSERT INTO ordered_products (order_id, product_id, seller_id, quantity, price, ordered_product_status) VALUES (?,?,?,?,?,?)"
    cursor.execute(sql_insert, (ordered_products,))
db.commit()
db.close()

"""""
