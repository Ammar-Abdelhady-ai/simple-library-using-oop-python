class Author:
    __author_Id = 0

    def __init__(self, Name, Phone, Mail):
        Author.__author_Id  += 1
        self.id = Author.__author_Id
        self.name = Name
        self.phone = Phone
        self.mail = Mail