


def authentication(shopperid):

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/University/Database/Assessment/Database/Assessment.db"
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
        return True
    else:
        return False




def first(shopperid):

    import sqlite3
    db_file = "/Users/boldizsarbanfia/Documents/University/Database/Assessment/Database/Assessment.db"
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    sql_query = "SELECT shopper_orders.order_id, shopper_orders.order_date, products.product_description, sellers.seller_name,\
     ordered_products.price,ordered_products.quantity, shopper_orders.order_status \
      FROM shoppers INNER JOIN ordered_products ON shopper_orders.order_id = ordered_products.order_id\
      INNER JOIN shopper_orders ON shoppers.shopper_id = shopper_orders.shopper_id\
    INNER JOIN sellers ON ordered_products.seller_id = sellers.seller_id\
    INNER JOIN products ON products.product_id = ordered_products.product_id\
    WHERE shopper_orders.shopper_id = ?  ORDER BY shopper_orders.order_date DESC "

    cursor.execute(sql_query, (shopperid,))
    shopper_row = cursor.fetchall()
    db.close()
    if shopper_row:
        for row in shopper_row:
            orderid = row[0]
            order_date = row[1]
            product_desc = row[2]
            sellername= row[3]
            qty_ordered = row[4]
            price = row[5]
            status = row[6]

            print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format( orderid, order_date, product_desc, sellername,qty_ordered, price, status))
    else:
        print("There was no previous order")
