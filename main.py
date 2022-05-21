from classes import Client
from classes import Librarian
from classes import Book
from classes import Borrow_order
from datetime import datetime
#
# print("""
# 1. Create a new client.
# 2. Create a new librarian.
# 3. Ensert book information.
# 4. Request to borrow a book.
# 5. Return the borrowed book.
#
# Choose the service, by entering the service number: """)
#
# input_1=int(input())
#
#
# list_clients=[]
# list_librarianes=[]
# list_books=[]
#
# input_2=None
# id=1
#
# if input_1==1:  #Create a new client
#
#     print("To create the account:")
#
#     full_nmae=input("Full name:")
#     age=input("Age:")
#     id_no=input("Id number:")
#     phone_number=input("Phone number:")
#
#     client = Client(id, full_nmae, age, id_no, phone_number)
#     list_clients.append(client)
#     id += 1
#
#     input_2= int(input("""An account has been created successfully.
#     1. If you want to go back to the main menu, enter 1.
#     2. If you want to exit the program, enter number 2.
#     """))
#
#     if input_2==1:
#         pass
#     elif input_2==2:
#         quit() # for exit
#     else:
#         print("The service number you entered does not exist.")
#
#
#
#
#
#
#
# elif input_1==2:    #Create a new librarian
#
#     print("To create the account:")
#
#     full_nmae = input("Full name:")
#     age = input("Age:")
#     id_no = input("Id number:")
#     emplyment_type = input("Emplyment type:")
#     librarian = Librarian(id, full_nmae, age, id_no, emplyment_type)
#     list_librarianes.append(librarian)
#     id += 1
#
#     print("An account has been created successfully.")
#
#
# elif input_1==3:     #Create books
#     print("To ensert book information:")
#
#     title = input("The title of the book:")
#     descrition = input("Description of the book:")
#     author = input("Author:")
#     status = input("If the book is borrowed enter “Not Available”, otherwise enter “Available”:")
#
#     book=Book(id,title,descrition,author)
#     if status == "Available":
#         status="Available"
#         book.status=status
#         print("The book data has been entered successfully.")
#     elif status == "Not Available":
#         status="Not Available"
#         book.status = status
#         print("The book data has been entered successfully.")
#
#     else:
#         print("The entry is incorrect, please check the entry you entered.")
#
#
#
# elif input_1==4:
#     pass
# elif input_1==5:
#     pass
# else:
#     print("The service number you entered does not exist.")
#


#################################################################################################



list_clients=[]
list_librarianes=[]
list_books=[]
list_borrow_order=[]

check="true"
input_2=None
id=1
id_book=1
id_borrow=1

while check=="true":
    print("""
    1. Create a new client.
    2. Create a new librarian.
    3. Ensert book information.
    4. Request to borrow a book.
    5. Return the borrowed book.
    6. Close the program.

    Choose the service, by entering the service number: """)

    input_1 = int(input())

    if input_1==1:  #Create a new client

        print("To create the account:")

        full_nmae=input("Full name:")
        age=input("Age:")
        id_no=input("Id number:")
        phone_number=input("Phone number:")

        client = Client(id, full_nmae, age, id_no, phone_number)
        list_clients.append(client)
        id += 1

        input_2= int(input("""An account has been created successfully.
        1. If you want to go back to the main menu, enter 1.
        2. If you want to exit the program, enter number 2.
        """))

        if input_2==1:
            pass
        elif input_2==2:
            quit() # for exit
        else:
            print("The service number you entered does not exist.")


    elif input_1==2:    #Create a new librarian

        print("To create the account:")

        full_nmae = input("Full name:")
        age = input("Age:")
        id_no = input("Id number:")
        emplyment_type = input("Emplyment type:")
        librarian = Librarian(id, full_nmae, age, id_no, emplyment_type)
        list_librarianes.append(librarian)
        id += 1

        input_2 = int(input("""An account has been created successfully.
                1. If you want to go back to the main menu, enter 1.
                2. If you want to exit the program, enter number 2.
                """))

        if input_2 == 1:
            pass
        elif input_2 == 2:
            quit()  # for exit
        else:
            print("The service number you entered does not exist.")


    elif input_1==3:     #Create books
        print("To ensert book information:")

        title = input("The title of the book:")
        descrition = input("Description of the book:")
        author = input("Author:")
        status = input("If the book is borrowed enter “Not Available”, otherwise enter “Available”:")

        book=Book(id_book,title,descrition,author)
        if status == "Available":
            status="Available"
            book.status=status
            print("The book data has been entered successfully.")
        elif status == "Not Available":
            status="Not Available"
            book.status = status
            print("The book data has been entered successfully.")

        else:
            print("The entry is incorrect, please check the entry you entered.")
            pass


        list_books.append(book)
        id_book+=1

        input_2 = int(input("""
                        1. If you want to go back to the main menu, enter 1.
                        2. If you want to exit the program, enter number 2.
                        """))
        if input_2 == 1:
            pass
        elif input_2 == 2:
            quit()  # for exit
        else:
            print("The service number you entered does not exist.")



    elif input_1==4:                            #borrow a book


        input_id_book=int(input("Enter the id of the book you want to borrow:"))
        registered=None

        #borrow_order=Borrow_order()

        for a in list_books:

            if input_id_book == a.id:
                registered=1

            else:
                registered=2


        if registered==1:
            input_3=input("Enter the ID number to borrow:")

            reserv=1
            for s in list_clients:
                if input_3== s.id_no:
                    reserv=2

            if reserv==1:
                print("There is no account for you, create an account before borrowing")
            elif reserv==2:

                # borrow_order.id=id_borrow
                # borrow_order.date=datetime.now()  #for show time
                # borrow_order.client_id=input_3
                # borrow_order.book_id=input_id_book
                # borrow_order.status="Not Available"

                print("The book has been borrowed successfully.")

        else:
            print("The book is not registered in the library")


        id_borrow+=1

        input_2 = int(input("""
                                1. If you want to go back to the main menu, enter 1.
                                2. If you want to exit the program, enter number 2.
                                """))
        if input_2 == 1:
            pass
        elif input_2 == 2:
            quit()  # for exit
        else:
            print("The service number you entered does not exist.")



    elif input_1==5:
        pass
    elif input_1==6:
        print("The program has been closed successfully.")
        quit()
    else:
        print("The service number you entered does not exist.")



else:
    quit()  # for exit


