import third_option


def displaying_basket(shopperid): # this is the calling fucntion
    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT products.product_description, sellers.seller_name, basket_contents.quantity, basket_contents.price, SUM(basket_contents.quantity*basket_contents.price)\
                    FROM basket_contents INNER\
                    JOIN sellers ON sellers.seller_id = basket_contents.seller_id\
                    INNER JOIN products ON products.product_id = basket_contents.product_id\
                    INNER JOIN shopper_baskets on shopper_baskets.basket_id = basket_contents.basket_id\
                    WHERE shopper_baskets.shopper_id = ?\
                    GROUP BY basket_contents.product_id "

    cursor.execute(sql_query, (shopperid,))

    one_row = cursor.fetchone()
    db.close()
    if one_row is not None:
        fetchall(shopperid)
    else:
        print("Your basket is empty!")


def fetchall(shopperid):
    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/Coding/assessments/database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT products.product_description, sellers.seller_name, basket_contents.quantity, basket_contents.price, SUM(basket_contents.quantity*basket_contents.price)\
                        FROM basket_contents INNER\
                        JOIN sellers ON sellers.seller_id = basket_contents.seller_id\
                        INNER JOIN products ON products.product_id = basket_contents.product_id\
                        INNER JOIN shopper_baskets on shopper_baskets.basket_id = basket_contents.basket_id\
                        WHERE shopper_baskets.shopper_id = ?\
                        GROUP BY basket_contents.product_id "
    basket_content = []
    c = 1
    cursor.execute(sql_query, (shopperid,))

    all_rows = cursor.fetchall()
    print("Basket Item, Product Description, Seller Name, Qty, Price, Total")
    for row in all_rows:
            proddesc = row[0]
            sellername = row[1]
            qty = row[2]
            price = row[3]
            total = row[4]
            basket_content.append(proddesc)
            print("{0}.{1}\t{2}\t{3}\t{4}\t{5}\t".format(c, proddesc, sellername, qty, price, total))
            c = c + 1
    #db.close() # not closing here just yet

    while IndexError: # keep iterrating if the input is out of range. If the chosen item is invalid
        try:
            item_row = int(input("Enter the basket number of the item you want to change the quantity of. "))
            selected_item = basket_content[item_row - 1]
            #print(selected_item)
            break
        except IndexError:
            print("Try again, that number is invalid")
    print(selected_item)
    product_desc = selected_item
    qty = int(input("Enter quantity of the selected product you want to buy"))
    if qty <= 0: # if the qty is 0 it will iterrate the input
        print("The quantity must be greater than 0!")
        while qty <=0:
            qty = int(input("Enter quantity of the selected product you want to buy: "))

    # finding the product id
    sql_query2 = "SELECT products.product_id FROM products WHERE products.product_description == ?"
    cursor.execute(sql_query2 , (product_desc,))
    one_row = cursor.fetchone()
    product_id = one_row[0]

    # updating the item qty:
    sql_update = "UPDATE basket_contents SET quantity = ? WHERE product_id == ?"
    cursor.execute(sql_update, (qty, product_id))
    db.commit()

    db.close()


#displaying_basket(shopperid= 10001)
#print("Bakset Updated:")
#print()
#third_option.displaying_basket(shopperid=10001)
