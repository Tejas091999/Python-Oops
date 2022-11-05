class Library:
    def __init__(self,ListOfBooks):
        self.books = ListOfBooks
    def displayavaiblebooks(self):
        print("The books present in this library are: ")
        for book in self.books:
            print(book)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"You have issued a {bookname}.Please keep it safe")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry!! This book is already taken")
            return False
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("Thank you for returning this book!")
class Student:
    def requestbook(self):
        self.books = input("Which book do you want to read: ")
        return self.books
    def returnbook(self):
        self.books = input("Which book do you want to return: ")
        return self.books
if __name__=="__main__":
    centralLibrary = Library(["MATHS","CHEMISTRY","ENGLISH","BIOLOGY"])
    centralLibrary.displayavaiblebooks()
    while(True):
        welcomemsg = '''=====WELCOME TO LIBRARY=====
        Please choose an option:
        1.LISTINGS ALL THE BOOKS.
        2.REQUEST A BOOK.
        3.RETURN A BOOK.
        4.EXIT.'''
        a = int(input("Enter your choice: "))
        if a == 1:
            centralLibrary.displayavaiblebooks()
        elif a == 2:
            centralLibrary.borrowbook(Student.requestbook)
        elif a == 3:
            centralLibrary.returnbook(Student.returnbook)
        elif a == 4:
            print("Thank you for using this library")
            print("Please do visit again!")
            exit()
