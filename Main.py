from BookManagement import*
from ReaderManagement import *

def main():
    while True:
        print("\n+------------ Library Management System ------------+")
        print("|                                                   |")
        print("|  Which Section Would You Like To Manage?          |")
        print("|  1. Book Management                               |")
        print("|  2. Reader Management                             |")
        print("|  3. Exit                                          |")
        print("|                                                   |")
        print("+---------------------------------------------------+")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                print("Moving to Book Management Section...")
                print()
                print("~" * 120)
                book_menu()
            elif choice == 2:
                print("Moving to Reader Management Section...")
                print()
                print("~" * 120)
                reader_menu()
            elif choice == 3:
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again!")
        except:
            print("Invalid input. Please try again!")

manager = BooksManager()
def book_menu():
    while True:
        print("\n+----------------- Book Management -----------------+")
        print("|  1. Add Book                                      |")
        print("|  2. Change Book Info                              |")
        print("|  3. Remove Book                                   |")
        print("|  4. Find Book                                     |")
        print("|  5. Display All Books                             |")
        print("|  6. Sort Book list By Alphabetical Title          |")
        print("|  7. Display Book List With filter                 |")
        print("|  8. Print Borrowed Book List                      |")
        print("|  9. Save File Borrowed Book                       |")
        print("|  10. Exit                                         |")
        print("+---------------------------------------------------+")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                id = input("Enter book's id: ")
                if manager.check_id(id):
                    print("This ID is already existed. Please try again!")
                    continue
                title = input("Enter book's title: ")
                author = input("Enter book's author: ")
                genre = input("Enter book's genre: ")
                quantity = int(input("Enter book quantity: "))
                if quantity <= 0:
                    print("Number of copies must be larger than 0. Please try again!")
                    continue
                book = Book(id.upper(), title.title(), author.title(), genre.title(), quantity)
                manager.add_book(book)

            elif choice == 2:
                manager.change_info()

            elif choice == 3:
                manager.remove_book()

            elif choice == 4:
                manager.find_book()

            elif choice == 5:
                manager.display_book_list()

            elif choice == 6:
                manager.sort_book_list()

            elif choice == 7:
                manager.filter()

            elif choice == 8:
                manager.print_borrowed_list()

            elif choice == 9:
                manager.save_file_borrowed_book()

            elif choice == 10:
                print("Exiting Book Management Section...")
                break

            else:
                print("Invalid choice. Please try again.")

        except:
            print("Invalid input. Please try again.")
        print()
        manager.save_file_book_list()
        print("~" * 120)

def reader_menu():
    reader_management = ReaderManagement()
    while True:
        print("\n+--------------------- Readers management ----------------------+")
        print("|  1. Add Reader                                                |")
        print("|  2. Change Reader Info                                        |")
        print("|  3. Remove Reader                                             |")
        print("|  4. Find Reader By Name                                       |")
        print("|  5. Display List Of Reader                                    |")
        print("|  6. Print List Of Reader With Descending Borrow Date / Fine   |")
        print("|  7. Show list of reader with filter                           |")
        print("|  8. Return book                                               |")
        print("|  9. Check expired date and issue fine to readers              |")
        print("|  10. Exit                                                     |")
        print("+---------------------------------------------------------------+")

        try:
            action = int(input("Enter your choice: "))
            if action == 1:
                name = input("Enter reader's name: ")
                email = input("Enter reader's email: ")
                phone_number = int(input("Enter reader's phone number: "))
                book_id = input("Enter id of borrowed book: ")
                borrow_date = input("Enter borrow date, format is year-month-day: ")
                new_reader = Reader(name.title(), email.lower(), str(phone_number), book_id.upper(), borrow_date)
                try:
                    if manager.borrow_book(new_reader.book_id):
                        reader_management.add_reader(new_reader)
                except:
                    print("This book does not exist.")

            elif action == 2:
                if not reader_management.change_reader_info():
                    print("No matching reader info. Please check reader's name or book title again.")

            elif action == 3:
                if not reader_management.remove_reader():
                    print("No matching reader to remove. Please check reader's name or book title again.")

            elif action == 4:
                found = reader_management.find_reader_by_name()
                if not found:
                    print("Reader does not found.")

            elif action == 5:
                reader_management.display_list_of_readers()

            elif action == 6:
                reader_management.print_list_by_borrow_date_or_fine()

            elif action == 7:
                reader_management.show_list_of_readers_with_filter()

            elif action == 8:
                name = input("Enter name of the reader returning the book: ")
                book = input("Enter name of the book: ")
                if reader_management.add_returned_book(name, book.upper()):
                    manager.return_book(book.upper())
                    print("Book returned successfully!")
                else:
                    print("No matching reader. Please check reader's name or book title again.")

            elif action == 9:
                reader_management.check_expired_date()

            elif action == 10:
                print("Exiting Readers Management...")
                break

            else:
                print("Invalid choice. Please try again.")

        except:
            print("Invalid input. Please try again.")
        print()
        reader_management.save_to_file()
        print("~" * 120)

if __name__ == "__main__":
    main()
