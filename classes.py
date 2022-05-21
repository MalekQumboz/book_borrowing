class Information:
    id = None
    full_nmae = ""
    age = ""
    id_no = ""    #id number


class Client(Information):
    phone_number=None

    def __init__(self,id ,full_name,age,id_no,phone_number):
        self.id=id
        self.full_nmae=full_name
        self.age=age
        self.id_no=id_no
        self.phone_number=phone_number


class Librarian(Information):
    emplyment_type=None     #(full/part)


    def __init__(self,id ,full_name,age,id_no,emplyment_type):
        self.id=id
        self.full_nmae=full_name
        self.age=age
        self.id_no=id_no
        self.emplyment_type=emplyment_type


class Book:
    id=None
    title=None
    descrition=None
    author=None
    status=None             #(Active-Inactive)

    def __init__(self,id,title,description,author):
        self.id=id
        self.title=title
        self.descrition=description
        self.author=author





class Borrow_order(Client,Book):
    id=None
    date=None
    client_id=Client.id
    book_id=Book.id
    status=Book.status             #(Active-Expired-Cancelled)







