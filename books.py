class Book:
    __book_Id = 0

    def __init__(self, Title, Publishing_data, Version, Language, author_id):
        Book.__book_Id  += 1
        self.id = Book.__book_Id
        self.title = Title
        self.publishing_data = Publishing_data
        self.version = Version
        self.language = Language
        self.author_id_of_book = author_id

