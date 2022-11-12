
import math


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
    try:
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


        # printing the Total price of the bag:
        """""
        sql_query3 = "SELECT shopper_baskets.basket_id FROM shopper_baskets WHERE shopper_id = ?"
        cursor.execute(sql_query3, (shopperid,))
        another_row = cursor.fetchone()
        basket_id = another_row[0]

        sql_query2 = "SELECT SUM(basket_contents.price) FROM basket_contents WHERE basket_id = ?" # instead of 2 we need the actual number
        cursor.execute(sql_query2, (basket_id,))
        one_row = cursor.fetchone()
        total = one_row[0]
        print(f"Basket Total is: {total}")
        """""
        sql_query4 = "SELECT  SUM(basket_contents.quantity*basket_contents.price)\
                            FROM basket_contents INNER\
                            JOIN sellers ON sellers.seller_id = basket_contents.seller_id\
                            INNER JOIN products ON products.product_id = basket_contents.product_id\
                            INNER JOIN shopper_baskets on shopper_baskets.basket_id = basket_contents.basket_id\
                            WHERE shopper_baskets.shopper_id = ?\
                            GROUP BY basket_contents.product_id "
        cursor.execute(sql_query4, (shopperid,))
        all_row = cursor.fetchall()
        total = []
        for row in all_row:
            total.append(row)
        #print(total)
        total2 = sum(map(sum, total))
        print(f"Basket Total is: {total2}")


        # removing

        while IndexError:  # keep iterrating if the input is out of range. If the chosen item is invalid
            try:
                remove_number = int(input("Enter the of the basket you want to remove: "))
                selected_item = basket_content[remove_number - 1]
                break
            except IndexError:
                print("Try again, the basket item no. you have entered is not in your basket!")

        #print(selected_item)

        # finding the product id of the chosen product
        product_desc = selected_item
        sql_query2 = "SELECT products.product_id FROM products WHERE products.product_description == ?"
        cursor.execute(sql_query2, (product_desc,))
        one_row = cursor.fetchone()
        product_id = one_row[0]


        try:
            basket_content[1]
            pass

        except IndexError:
            # if the basket has only one item it will require a confirmation

            finalize = input("Do you definitely want to delete this product and empty your basket? (Y/N)? ")
            if finalize == "y" or "Y":
                pass
            else:
                exit()


        cursor.execute("PRAGMA foreign_keys=ON")
        sql_delete = "DELETE FROM basket_contents WHERE product_id = ?"
        cursor.execute(sql_delete, (product_id,))
        db.commit()
        print("Item removed from your basket!")



        #print(basket_content[1])

        db.close()
    except ValueError:
        print("Should have Entered a number!")



#displaying_basket(shopperid=10001) # prints the total and the basket so far