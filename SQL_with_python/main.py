import sqlite3
import alt_function
import menupoints
import second_option
import third_option
import foruth_option
import fifth_option
import sixth_option

real_shopperid = []
# Runs the whole program
def run():
    shoppper_id = int(input("Enter the shopper ID:")) # Prompting for shopper id
    #process = menupoints.authentication(shoppper_id) # searching for shopper id, greeting the user
    process = second_option.authentication(shoppper_id)

    if process == True:
        real_shopperid.append(shoppper_id) # storing the id for reusing purposes.
        # greet it by neame
        print("Orinocco - Sopper Main Menu")
        while True:
            try:
                alt_function.main_options() # printing the main menu
                print() # leaving space
                menunumber = int(input()) # prompting
            except ValueError:
                #print("Please enter the correct menu point")
                pass
            except UnboundLocalError:
                print("Please enter the correct menu point")
            try:

                if menunumber == 1:
                    menupoints.first(shoppper_id)
                    print()
                elif menunumber == 2:

                    second_option.second_seller()
                    second_option.qty()
                    second_option.checking_shopper_baskets()
                    second_option.inserting_data()
                    print()

                elif menunumber == 3:
                    third_option.displaying_basket(shoppper_id)
                    print()

                elif menunumber == 4:
                    foruth_option.displaying_basket(shoppper_id)
                    print("Bakset Updated:")
                    print()
                    third_option.displaying_basket(shoppper_id)
                    print()

                elif menunumber == 5:
                    fifth_option.displaying_basket(shoppper_id)
                    print()

                elif menunumber == 6:
                    sixth_option.checkout(shoppper_id)
                    print()
                elif menunumber == 7:
                    break
                else:
                    print("Invalid option menu, Plesase chose form the menu!")
            except ValueError:
                print("Please enter the correct menu point")
            except UnboundLocalError:
                print("Please enter the correct menu point")


    else:
        print("There is no customer with this shopper id!")

run()

