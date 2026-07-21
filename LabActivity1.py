# Act1: Aliah's Interactive Library Kiosk
def check_borrowing(overdue_books, status):
    if overdue_books == "yes":
        return "Not allowed: overdue books"
    if status == "suspended":
        return "Not allowed: suspended account"
    return "Borrowing allowed"


borrow_count = 0

while True:
    name = input("Enter student name (type 'exit' to stop): ")
    if name.lower() == "exit":
        break

    overdue = input("Do you have overdue books? (yes/no): ")
    status = input("What is your status? (active/suspended): ")
    books_wanted = int(input("How many books do you want to borrow? "))

    result = check_borrowing(overdue, status)
    print(result)

    if result == "Borrowing allowed":
        if books_wanted == 0:
            print("You didn't ask for any books, so there's nothing to borrow right now.")
        elif books_wanted > 3:
            print("You can only take up to 3 books at a time, so we're giving you 3.")
            books_wanted = 3
            borrow_count += 1
        else:
            print(f"You can borrow {books_wanted} book(s), enjoy!")
            borrow_count += 1

print(f"\nTotal students who successfully borrowed books: {borrow_count}")