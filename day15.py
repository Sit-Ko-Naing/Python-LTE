cmd_list = ("list","search","register","delete","quit")
books = ["book1","book2","book3","book4"]

def usr_list():
    if len(books) == 0:
        print("There is no books in library.")
    else:
        print("List of Books ")
        for book_name in books:
            print(f"[{books.index(book_name) + 1}] : {book_name}")

    
def usr_search():
    search_keyword = input("Enter book name / keyword : ")
    for book_name in books:
        if search_keyword in book_name:
            print(f"[{books.index(book_name) + 1}] : {book_name}")


def usr_register():
    book_name = input("Enter a book name to register : ")
    if book_name in books:
        print("This book is already in library.")
    else:
        books.append(book_name)

def usr_delete():
    delete_book = input("Enter book number you wanna delete : ")
    # sure = input(f"You want to delete {books[delete_book -1]}  : Comfirm Y/N : ")
    books.remove(delete_book)
    # if sure == "Y":
    #     books.pop(delete_book -1)
    # else:
    #     pass


print('''
_________________________________
          
        LTE Library
    _______________________
    |                     |    
    |   # List            |
    |   # Search          |
    |   # Register        |
    |   # Delete          |
    |   # Quit            |
    |_____________________|
        
    ''')
while True:
    cmd = ""
    while not cmd in cmd_list:  
        cmd = input("Choose one option : ")

    if cmd == "list":
        usr_list()
    elif cmd == "search":
        usr_search()
    elif cmd == "register":
        usr_register()
    elif cmd == "delete":
        usr_delete()
    elif cmd == "quit":
        print("Thank for using my application.")
        break

