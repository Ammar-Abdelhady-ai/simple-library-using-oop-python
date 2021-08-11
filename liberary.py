class Liberary:

    Author = []
    Book = []

    # Authors operations in liberary

    # add author to list
    def add_author(self, author) :
        self.Author.append(author)

    # remove author from list by id
    def remove_author(self, id) :

        for author in self.Author:

            if author.id == id:
                self.Author.remove(author)
                break

            print(f"your id : {id} not faund ")
                
    # print author's information by id
    def print_author(self, id) :

        for author in self.Author:

            if author.id == id:
                print(f"Name : {author.name} - ", f"phone : {author.phone} - ", f"email : {author.mail} ")

                return

        print(f"your id : {id} not faund ")

    # print all authors in liberary 
    def print_all_author(self):
        for author in self.Author:
            print(f"Name : {author.name} - ", f"phone : {author.phone} - ", f"email : {author.mail} ")


    # Books oberations in liberary

    # add book to list
    def add_book(self, book):
        self.Book.append(book)

    # remove book from liberary
    def remove_book(self, id):
        for book in self.Book:
            if book.id == id:
                self.Book.remove(book)
                return
        print(f"sorry your id : {id} not found")

    #print book with id
    def print_book(self, id):
        for book, author in zip(self.Book, self.Author) :
            if book.id == id :
                print(f"Title : {book.title} - ")
                print(f"Publishing data : {book.publishing_data} - ")
                print( f"Version : {book.version} ")
                print(f"Language : {book.language} - ")

                if author.id == book.author_id_of_book:
                    print(f"name of Author : {author.name}")
                    break

                return
        print(f"sorry your id : {id} not found")

    #print all books in liberary
    def print_all_book(self) :
        n = 1
        for book in self.Book :
            print(f"the book number : {n} \n")
            print(f"Title : {book.title} - ")
            print(f"Publishing data : {book.publishing_data} - ")
            print( f"Version : {book.version} ")
            print(f"Language : {book.language} - ")
            for author in self.Author:
                if author.id == book.author_id_of_book:
                    print(f"name of Author : {author.name}")

            n = n + 1
        return                
        

   
    def print_author_books(self, id):
        for book, author in zip(self.Book, self.Author) :
            is_the_id_exist = False
            if book.author_id_of_book == id:
                is_the_id_exist = True

                if is_the_id_exist:
                    for book in self.Book:                    
                        print(f"the name of author is : {author.name} ")
                        print(f"Title of the book is : {book.title} - ")
                        print(f"Publishing data of the book is : {book.publishing_data} - ")
                        print( f"Version of the book is : {book.version} ")
                        print(f"Language of the book is : {book.language} - ")
                        print("-------------------------------------------------\n")
            
                if is_the_id_exist == False:
                    print(f"id of Author : {id} not faund")
                return