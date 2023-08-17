# assignment 05

# Task: Build a basic management system of your own choice such as student, online shop etc, that uses the idea of inheritance. Also, mention the type of inheritance being used.


# defining class
class Library():
    def __init__(self, list_of_books, Library_name):
        # creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No reader have lend this book
            self.lend_data[books] = None

    def display_books(self):
        for index, books in enumerate(self.list_of_books):
            print(f"{index}:{books}")

    def lend_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = reader
                print("\nBook Lend")
            else:
                print(f"\nSorry This book is lend by {self.lend_data[book]}")
        else:
            print("\nwrong book name")

    def return_book(self, book, reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("\nSorry but This book is not Lend")
        else:
            print("\nwrong book name")

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)



def main():
    # By deafault variables
    list_books = ['abc', 'xyz', 'pqr', 'mno']
   
    Library_name = 'THE XYZ '
    secret_key = 0000000

    minahil = Library(list_books, Library_name)

    print(f"\t\tWelecome To {minahil.library_name} library\n\ne for exit \nDisplay Book Using 's' \nadd lend book using 'l'\nReturn a Book using 'r' \nAdd Book Using 'a' \nDelete Book using 'd' \n ")
    Exit = False
    while (Exit is not True):
        _input = input("\noption:")
        print("\n")

        if _input == "e":
            Exit = True

        elif _input == "s":
            minahil.display_books()

        elif _input == "l":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")

            minahil.lend_book(_input3, _input2)

        elif _input == "a":
            _input2 = input("Book name:")
            minahil.add_book(_input2)

        elif _input == "d":
            _input_secret = int(input("Write the secret key to delete:"))
            if (_input_secret == secret_key):
                _input2 = input("Book Which you want to delete:")
                minahil.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        elif _input == "r":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            minahil.return_book(_input3, _input2)


if __name__ == "__main__":
    main()