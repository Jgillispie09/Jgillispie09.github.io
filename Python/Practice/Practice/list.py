import time
movers_complete = ["1. Best Price Movers, 4.5 Stars, 128 Reviews, https://www.bestpricemoversusa.com, (813)724-3311, Request quote", "2. Antares Moving Company, 5 Stars, 20 Reviews, https://www.antaresmovingcompany.com, (727)303-6379, Request quote", "3. B&T Moving Company, 4.9 Stars, 262 Reviews, https://www.bntmoving.com, (813)616-3232, Request quote", "4. All Out Moving LLC, 4.7 Stars, 176 Reviews, https://www.needmoversfast.com, (813)803-0480, Request quote", "5. Einstein Moving Company, 4.9 Stars, 30 Reviews, https://einsteinmoving.com, (813)934-7221, Request quote", "6. Bull Moving, 4.7 Stars, 698 Reviews, https://www.bullmovingfl.com, (813)943-6043, Request quote", "7. Premier Movers 4 Less, 5 Stars, 97 Reviews, https://www.premiermovers4less.com, (813)444-7716, Request quote", "8. Two Men and a Truck, 4.7 Stars, 199 Reviews, https://www.twomenandatruck.com, (813)279-8228, Request quote", "9. Florida Boys Moving and Storage, 5 Stars, 159 Reviews, https://www.floridaboysmoving.com, (813)321-0684, Request quote", "10. College Hunks Hauling Junk and Moving, 4.9 Stars, 1,087 Reviews, https://www.collegehunkshaulingjunk.com, (813)331-0502, Request quote", "11. Good Greek Moving and Storage, 4.6 Stars, 695 Reviews, https://www.greekmoving.com, (813)438-2700, Request quote"]
movers_rating = ["1. Florida Boys Moving and Storage, 5 Stars, 159 Reviews, https://www.floridaboysmoving.com, (813)321-0684, Request quote", "2. Premier Movers 4 Less, 5 Stars, 97 Reviews, https://www.premiermovers4less.com, (813)444-7716, Request quote", "3. Antares Moving Company, 5 Stars, 20 Reviews, https://www.antaresmovingcompany.com, (727)303-6379, Request quote", "4. College Hunks Hauling Junk and Moving, 4.9 Stars, 1,087 Reviews, https://www.collegehunkshaulingjunk.com, (813)331-0502, Request quote", "5. B&T Moving Company, 4.9 Stars, 262 Reviews, https://www.bntmoving.com, (813)616-3232, Request quote", "6. Einstein Moving Company, 4.9 Stars, 30 Reviews, https://einsteinmoving.com, (813)934-7221, Request quote", "7. Bull Moving, 4.7 Stars, 698 Reviews, https://www.bullmovingfl.com, (813)943-6043, Request quote", "8. All Out Moving LLC, 4.7 Stars, 176 Reviews, https://www.needmoversfast.com, (813)803-0480, Request quote", "9. Two Men and a Truck, 4.7 Stars, 199 Reviews, https://www.twomenandatruck.com, (813)279-8228, Request quote", "10. Good Greek Moving and Storage, 4.6 Stars, 695 Reviews, https://www.greekmoving.com, (813)438-2700, Request quote", "11. Best Price Movers, 4.5 Stars, 128 Reviews, https://www.bestpricemoversusa.com, (813)724-3311, Request quote"]

print("Hello, user! What would you like to do today?\n 1. View list of movers")
main_option = input("Select an option: \n")
if main_option == "1":
    print("\nHere is the current list of movers:")
    time.sleep(1)
    print(*movers_complete, sep = "\n")
else:
    print("I'm sorry, that is not a valid option.")
print("\nWhat would you like to do next?\n 1. Return to main menu\n 2. Sort list")
sub_option = input("Select an option: \n")
if sub_option == "1":
    print("Hello, user! What would you like to do today?\n 1. View list of movers")
    main_option = input("Select an option: \n")
    if main_option == "1":
        print("\nHere is the current list of movers:")
        time.sleep(1)
        print(*movers_complete, sep = "\n")
    else:
        print("I'm sorry, that is not a valid option.")
    print("\nWhat would you like to do next?\n 1. Return to main menu\n 2. Sort list")
    sub_option = input("Select an option: \n")
    if sub_option == "1":
        print("Placeholder")
    elif sub_option == "2":
        print("\nHow would you like me to sort the list?\n 1. By rating")
        sorting = input("Select an option: \n")
        if sorting == "1":
            print("Here is the list of movers sorted by Star rating: ")
            print(*movers_rating, sep = "\n")
        else:
            print("I haven't thought of what to do next!")
    else:
        print("I'm sorry, that is not a valid option.")
elif sub_option == "2":
    print("\nHow would you like me to sort the list?\n 1. By rating")
    sorting = input("Select an option: \n")
    if sorting == "1":
        print("Here is the list of movers sorted by Star rating: ")
        print(*movers_rating, sep = "\n")
    else:
        print("I haven't thought of what to do next!")
else:
    print("I'm sorry, that is not a valid option.")