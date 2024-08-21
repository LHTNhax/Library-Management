from Array import MyArray
from Mydictionary import MyDictionary

class Book:
    def __init__(self, id, title, author, genre, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.quantity = quantity
        self.borrowed = 0
        self.status = "Available"

class BooksManager:
    def __init__(self):
        self.book_list = MyDictionary()
        self.borrowed_book = MyArray()

    def add_book(self, book):
        self.book_list.insert(book.id, [book.title, book.author, book.genre, book.quantity, book.borrowed, book.status])
        print("Book added successfully!")

    def change_info(self):
        change = input("Enter book id to change info: ")
        change = change.upper()
        if change in self.book_list.keys:
            num = int(input("Choose the number of category you want to change: 1.title  |  2.author  |  3.genre  |  4.quantity \n"))
            if 0 < num < 4:
                new = input("Enter new info: ")
                self.book_list[change][num - 1] = new.title()
                print("Book info changed!")
            elif num == 4:
                new = int(input("Enter new info: "))
                if new <= 0:
                    print("Quantity must be larger than 0. Please try again!")
                else:
                    self.book_list[change][num - 1] = new
                    print("Book info changed!")
            else:
                print("Invalid number. Please try again!")
        else:
            print("Book not found.")

    def remove_book(self):
        remove = input("Enter book's id to remove: ")
        remove = remove.upper()
        if remove in self.book_list.keys:
            if self.book_list[remove][4] == 0:
                try:
                    self.book_list.delete(remove)
                    print("Book removed!")
                except KeyError:
                    print("This book does not exist!")
            else:
                print("Some copies of this book is being borrowed. This book can't be removed right now.")
        else:
            print("This book does not exist.")

    def find_book(self):
        book = input("Enter book's id to find: ")
        book = book.upper()
        if book in self.book_list.keys:
            print_table()
            print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                  f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                  f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
            print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
        else:
            print("Book not found.")

    def display_book_list(self):
        print_table()
        for book in sorted(self.book_list.keys):
            print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                  f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                  f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
            print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")

    def sort_book_list(self):  # Sort book title
        print_table()
        for book, value in sorted(self.book_list, key=lambda info: info[1][0]):
            print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                  f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                  f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
            print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")

    def filter(self):
        category = int(
            input("Choose a number of category to filter: 1.title  |  2.author  |  3.genre  |  4.status \n"))
        if 0 < category < 5:
            if category == 4:
                category += 2  # change index to Status
                value = input("Enter a value to filter out:  Available  |  Not Available \n")
            else:
                value = input("Enter the value to filter out: ")
            print_table()
            for book in self.book_list.keys:
                if self.book_list[book][category - 1] == value.title():
                    print(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                          f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                          f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|")
                    print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
        else:
            print("Invalid number. Please try again!")

    def borrow_book(self, id):
        if self.book_list[id][5] == "Available":
            self.borrowed_book.append(id)
            self.book_list[id][4] += 1
            if self.book_list[id][3] == self.book_list[id][4]:
                self.book_list[id][5] = "Not Available"
            return True
        else:
            print("This book is not available now!")
            return False

    def return_book(self, id):
        try:
            self.borrowed_book.remove(id)
            self.book_list[id][4] -= 1
            print("Returned book successfully!")
            if self.book_list[id][4] < self.book_list[id][3]:
                self.book_list[id][5] = "Available"
            return True
        except:
            print("This book was not borrowed.")
            return False

    def print_borrowed_list(self):
        print("+--------+---------------------+")
        print("|  ID    |    Borrowed Books   |")
        print("+--------+---------------------+")
        for book in self.borrowed_book:
            print(f'|{book.center(8)}|{self.book_list[book][0].center(21)}|')
            print("+--------+---------------------+")

    def save_file_borrowed_book(self):
        data = open("Borrowed_books.txt", "w")
        data.write("+--------+---------------------+\n")
        data.write("|  ID    |    Borrowed Books   |\n")
        data.write("+--------+---------------------+\n")
        for book in self.borrowed_book:
            data.write(f'|{book.center(8)}|{self.book_list[book][0].center(21)}|\n')
            data.write("+--------+---------------------+\n")
        print("Saved to file!")
        data.close()

    def save_file_book_list(self):
        data = open("Book_list.txt", "w")
        data.write("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+\n")
        data.write("|  ID    |        Title        |       Author       |     Genre     |   Quantity    |   Borrowed    |    Status     |\n")
        data.write("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+\n")
        for book in sorted(self.book_list.keys):
            data.write(f"|{book.center(8)}|{self.book_list[book][0].center(21)}|{self.book_list[book][1].center(20)}|"
                       f"{self.book_list[book][2].center(15)}|{str(self.book_list[book][3]).center(15)}|"
                       f"{str(self.book_list[book][4]).center(15)}|{self.book_list[book][5].center(15)}|\n")
            data.write("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+\n")
        print("Data saved!")
        data.close()

    def check_id(self, id):
        if id in self.book_list.keys:
            return 1
        else:
            return 0

def print_table():
    print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
    print("|  ID    |        Title        |       Author       |     Genre     |   Quantity    |   Borrowed    |    Status     |")
    print("+--------+---------------------+--------------------+---------------+---------------+---------------+---------------+")
