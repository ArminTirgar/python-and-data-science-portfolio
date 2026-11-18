


if __name__ == "__main__":

    my_library = Library()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show Books")
        print("5. Exit")

        user_input = input("Enter your option: ")

        if user_input == "1":
            title = input("Please enter the title: ")
            author = input("Please enter the author: ")
            my_library.add_book(title, author)

        elif user_input == "2":
            title = input("Please enter the title: ")
            my_library.remove_book(title)

        elif user_input == "3":
            title = input("Please enter the title: ")
            result = my_library.search_book(title)

            if result:
                print(f"Book found: {result['title']}")
                print(f"Author: {result['author']}")
            else:
                print("Book not found.")

        elif user_input == "4":
            my_library.show_books()

        elif user_input == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid input.")
