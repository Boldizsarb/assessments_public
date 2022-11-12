


globalshopperid = []

def authentication(shopperid):

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT shopper_first_name, shopper_surname FROM shoppers WHERE shopper_id = ?"

    cursor.execute(sql_query, (shopperid,))

    shopper_row = cursor.fetchone()
    db.close()
    if shopper_row:
        shopper_firstname = shopper_row[0]
        shopper_surname = shopper_row[1]
        print("Welcome {0} {1}".format(shopper_firstname, shopper_surname))
        globalshopperid.append(shopperid)
        return True
    else:
        return False



############################################################################################################################



product_id_list = []
seller_name_list = [] # extracting the given value and turning it with an sql query into what I need which is the seller id.
qty_list = []
price_list = []

def second_category():
    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT categories.category_description FROM categories --ORDER BY category_description"
    cursor.execute(sql_query)
    category_list = []
    b = 1

    print("Product Categories")
    print()
    all_rows = cursor.fetchall()
    for row in all_rows:
        categories = row[0]
        category_list.append(categories) # populating the list
        print("{0}. {1}".format(b,categories))
        b = b+1
    db.close()

    chosen_category = int(input("Enter the number against the product category you want to choose: "))

    while chosen_category > 6 or chosen_category == 0:
        chosen_category = int(input("Enter the number against the product category you want to choose: "))
    return chosen_category

#second_category()
#returned_category = second_category()
#print(returned_category)

def second_products(): # displaying the products within the chosen category
    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    categorynumber = second_category() #using the returned number as the primary key and variable

    sql_query = "select products.product_description FROM products INNER JOIN categories ON categories.category_id = products.category_id WHERE categories.category_id == ?"
    cursor.execute(sql_query, (categorynumber,))

    productlist = []
    c = 1

    all_rows = cursor.fetchall()
    for row in all_rows:
        products = row[0]
        productlist.append(products)
        print("{0}. {1}".format(c, products))
        c = c+1
    db.close()

    producnumber = int(input("Enter the number against the product you want to choose: "))
    product_id_list.append(productlist[producnumber -1])
    return(productlist[producnumber -1]) #makin a string out of a list with the index number of the variable


#chosen_productdesc = second_products() # storing the returned string in a variable for reusing purposes, To find the product id

#print(second_products())
#second_products()

def second_seller():

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT sellers.seller_name, product_sellers.price FROM product_sellers INNER JOIN sellers ON sellers.seller_id = product_sellers.seller_id INNER JOIN products ON products.product_id= product_sellers.product_id WHERE products.product_description = ?"
    product_numb = second_products()
    cursor.execute(sql_query, (product_numb,))

    seller_list = []
    v =1
    all_rows = cursor.fetchall()
    for row in all_rows:
        sellername = row[0]
        price = row[1]
        seller_list.append(sellername)
        seller_list.append(price)
        print("{0}. {1}\t{2}".format(v,sellername,price))
        v = v+1
    db.close()
    which_sellernumber = int(input("Enter the number against the seller you want to chose: "))
    # thinkering with the index numbers to return the precise string of seller name
    if which_sellernumber == 2:
        #print(seller_list[which_sellernumber ])
        seller_name_list.append(seller_list[which_sellernumber])
        return seller_list[which_sellernumber ]

    elif which_sellernumber == 3:
        #print(seller_list[which_sellernumber +1])
        seller_name_list.append(seller_list[which_sellernumber + 1])
        return seller_list[which_sellernumber +1]
    elif which_sellernumber == 4:
        seller_name_list.append(seller_list[which_sellernumber + 2])
        #print((seller_list[which_sellernumber + 2]))
        seller_name_list.append(seller_list[which_sellernumber + 2])

    else:
        #print(seller_list[which_sellernumber - 1])
        seller_name_list.append(seller_list[which_sellernumber - 1])
        return seller_list[which_sellernumber - 1]




#returned_seller_name = second_seller() # storing the returned string in a variable
#second_seller()

def finding_productid(): # not good, initiates the program for the second time

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT products.product_id FROM products WHERE products.product_description == ?"
    productid = product_id_list[0]
    cursor.execute(sql_query, (productid,))
    one_row = cursor.fetchone()
    prodid = one_row[0]
    #print(prodid)
    db.close()
    return prodid

def finding_sellerid():
    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT sellers.seller_id FROM sellers Where sellers.seller_name == ?"
    sellerid = seller_name_list[0]
    cursor.execute(sql_query, (sellerid,))
    one_row = cursor.fetchone()
    seller = one_row[0]
    # print(prodid)
    db.close()
    return seller



def finding_price():

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    sql_query = "SELECT price FROM product_sellers   WHERE product_sellers.product_id == ? AND product_sellers.seller_id == ?"
    productid = finding_productid()
    sellerid = finding_sellerid()
    cursor.execute(sql_query, (productid, sellerid,))
    one_row = cursor.fetchone()
    price = one_row[0]
    db.close()

    return price



def qty():
    qty_number = int(input("Enter the quantity of the selected product you want to buy: "))
    while qty_number <= 0:
        qty_number = int(input("Enter the quantity of the selected product you want to buy: "))
    qty_list.append(qty_number)
    return qty_number


# main call!!!!!!!!!
#second_seller() # calling the all the function, qty excluded The fIRST CALL
#qty() # second call


# after the main program run!

#print(finding_productid()) # working call the function
#print(finding_sellerid()) # working call the function
#print(finding_price()) # working call the function

#print(qty_list[0]) # use the list not the function.

basket_id_list = []

def checking_shopper_baskets():
    import sqlite3
    import datetime
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    shopperid = globalshopperid[0]  # the shopper id.
    sql_query = "select basket_id from shopper_baskets WHERE shopper_id ==?"
    cursor.execute(sql_query, (shopperid,))
    basketrow = cursor.fetchone()
    if basketrow is not None: # if there is a basket id then i dont know that yet update probably
        # uptdating the time only
        time = datetime.datetime.now()
        sql_update = "UPDATE shopper_baskets SET basket_created_date_time == ? WHERE shopper_id == ?"
        cursor.execute(sql_update,(time, shopperid,))
        db.commit()
        #returning the basket id number either way
        sql_query2 = "SELECT basket_id FROM shopper_baskets WHERE shopper_id == ?"
        cursor.execute(sql_query2, (shopperid,))
        one_row = cursor.fetchone()
        basketid = one_row[0]
        return basketid
    else:
        time_created = datetime.datetime.now()
        sql_insert = "INSERT INTO shopper_baskets (shopper_id, basket_created_date_time) VALUES (?,?)"
        cursor.execute(sql_insert, ( shopperid, time_created))
        db.commit()
        #returning the basketid number either way
        sql_query2 = "SELECT basket_id FROM shopper_baskets WHERE shopper_id == ?"
        cursor.execute(sql_query2, (shopperid,))
        one_row = cursor.fetchone()
        basketid = one_row[0]
        return basketid
    db.close()

# it throws an an error if the shopper if the shopper id is not correct. so far. since it runs the main due to the import


#checking_shopper_baskets() # calling the function # utolsoelotti call
#print(checking_shopper_baskets()) # it returns the basked id.

def inserting_data():

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()

    # chechking if there is anything in the basket
    basketid = checking_shopper_baskets()
    shopperid = globalshopperid[0]
    productid = finding_productid()
    sellerid = finding_sellerid()
    qty_number = qty_list[0]
    price = finding_price()

    cursor.execute("PRAGMA foreign_keys=ON")
    sql_query = "SELECT * FROM basket_contents WHERE basket_id == ?"
    cursor.execute(sql_query, (basketid,))
    basketrow = cursor.fetchone()
    try:
        if basketrow is not None:
            try:
                # if there is an existing basket, then it will be updated by the new orders.
                new_or_not =input("There is an existent basket already, if you like it overriden type yes, othervise type no!")
                if new_or_not == "yes":
                    # it overrides the previous basket The one created at latest!
                    # while the program running it works once. To be able to update again you need to close the program and reopen it.
                    #
                    sql_update = "UPDATE basket_contents SET product_id = (?)\
                                            , seller_id = (?)\
                                            , quantity =  (?)\
                                            , price = (?)\
                                             WHERE product_id = (select basket_contents.product_id FROM shopper_baskets INNER JOIN basket_contents ON basket_contents.basket_id = shopper_baskets.basket_id WHERE basket_created_date_time <= DATE('now')ORDER BY basket_created_date_time DESC\
                                                LIMIT 1)"
                    cursor.execute(sql_update, (productid, sellerid, qty_number, price,))
                    db.commit()
                    print("Basket updated with the chosen items!")
                else:
                    sql_insert1 = "INSERT INTO basket_contents VALUES (?,?,?,?,?)"
                    cursor.execute(sql_insert1, (basketid, productid, sellerid, qty_number, price, ))
                    db.commit()
                    print("Items added to the basket")
            except sqlite3.IntegrityError:
                sql_insert2 = "INSERT INTO basket_contents VALUES (?,?,?,?,?)"
                cursor.execute(sql_insert2, (basketid, productid, sellerid, qty_number, price,))
                db.commit()
                print("Items added to the basket")

        else:
            # if there is no existing basket, a new one will be created.
            sql_insert3 = "INSERT INTO basket_contents VALUES (?,?,?,?,?)"
            cursor.execute(sql_insert3, (basketid, productid, sellerid, qty_number, price, ))
            db.commit()
            print("Items added to the basket")
    except sqlite3.IntegrityError:
        # if the product is already in the bag once, it will update the rest of the values
        sql_update2 = "UPDATE basket_contents SET seller_id = (?)\
                      , quantity =  (?), price = (?)  WHERE basket_id = ? AND product_id = ?"
        cursor.execute(sql_update2, (sellerid, qty_number, price, basketid, productid,))
        db.commit()
    db.commit()












#second_seller() # calling the all the function, qty excluded The fIRST CALL
#qty() # second call
#checking_shopper_baskets() # calling the function # utolsoelotti call
#inserting_data() # last call






