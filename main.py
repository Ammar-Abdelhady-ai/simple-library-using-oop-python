from author import Author
from liberary import Liberary
from books import Book

lib = Liberary()

# define the Authors in liberary
au1 = Author("Zed Shaw", "01026207313", "ammarabdelhady8@gmail.com")
au2 = Author("Leo Tolstoy", "01026242313", "sami@gmail.com")
au3 = Author("Shir Hashirim", "010262458313", "ali8@gmail.com")


lib.add_author(au1)                   #use to add author to liberary 
lib.add_author(au2)
lib.add_author(au3)


# define the Books in liberary
bo1 = Book("python hard way", "this booh use to learn python very good", "September 19, 2013", "English", au1.id)
bo2 = Book("War and Peace", "descriptions the warcand peace and its result", 1869, "Russian", au2.id)
bo3 = Book("Song of Songs", "The introduction calls the poem \"the song of songs\"", 1977, "English", au3.id)
bo4 = Book("Learn C the Hard Way", "Practical Exercises on the Computational Subjects You Keep Avoiding (Like C)", 
"August 10, 2015", "English", au1.id)

lib.add_book(bo1)                       #use to add book in liberary 
lib.add_book(bo2)
lib.add_book(bo3)
lib.add_book(bo4)



lib.remove_author(au2.id)               #use to remove author from liberary with id
lib.print_author(au3.id)                #use to print author informayion with id
lib.print_all_author()                  #use to print all author in liberary with no argument


lib.remove_book(au2.id)                 #use to remove book from liberary with id
lib.print_book(au3.id)                  #use to print book informayion with id
lib.print_all_book()                    #use to print all book in liberary with no argument

lib.print_author_books(au1.id)          #use to print all books of the author
                                        #hint author one have two books 

""" # you can use that ........
#use try and except to error
 
for author in lib.Author:
    print(f"Name : {author.name} - ", f"phone : {author.phone} - ", f"email : {author.mail} ")

# git the id from user
try:

    num = int(input("input the id that you want to delete author have : "))

except Exception as error :
    print(f"please inter integer number not inter {error}")

else:
        
    lib.remove_author(num)
    print("----------------------------------------------------------------")
    print(f"after remove author number {num}")
"""

"""
for author in lib.Author:
    print(f"Name : {author.name} - ", f"phone : {author.phone} - ", f"email : {author.mail} ")

lib.print_author(au2.id)

lib.print_all_author()

"""

"""
lib.print_book(bo2.id)

print("----------------", "\n")

lib.print_all_book()

print("----------------", "\n")

lib.remove_book(bo2.id)

n = 1
for book, author in zip(lib.Book, lib.Author) :
    print(f"the author number : {n} ")
    print(f"Title : {book.title} - ")
    print(f"Publishing data : {book.publishing_data} - ")
    print( f"Version : {book.version} ")
    print(f"Language : {book.language} - ")
    print(f"name of Author : {author.name}")
    print("-------------------------------------------------\n")
    n = n +1

lib.print_all_book()
lib.print_all_author()
"""
