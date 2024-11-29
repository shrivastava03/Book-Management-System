# Task => Create a new library management systm
 # class lib = list of books,borrow,return,donate
 # class student = request_book , return_book, donate_book

class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks

    def display_books(self):
        print("List of all available books in Library!!")
        for i in range(len(self.books)):
            print(i,'-',self.books[i])

    def borrow(self, name , bookname):
        if bookname not in self.books:
            print(bookname, "is not available currently!")
        else:
            tracker.append({name:bookname})
            print(f"Book Issued : {bookname} is available")
            self.books.remove(bookname)

    def returnBook (self,bookname):
        print("Book returned!! Thanks for reading, i hope it was fruitful.")
        self.books.append(bookname)

    def donate(self,bookname):
        print(f"Thanks for donating the book : {bookname}")
        self.books.append(bookname)

class Student:
    def requestBook(self):
        print("Welcome!! Are you looking for a book")
        self.book = input("Enter the book you want : ")
        return self.book
    
    def returnbookfromstudent(self):
        print("Welcome to return portal")
        name = input("Enter you name : ")
        self.book = input("Enter the book you want to return : ")
        if {name:self.book} in tracker:
            tracker.remove({name:self.book})
        return self.book
    
    def donationbook(self):
        print("Welcome to donation portal")
        self.book = input("Enter the book you want to donate: ")
        return self.book
        


if __name__ ==   '__main__':
    Aimerz_library = Library(["Stats_vol1",'Machine learning'
                              ,'Nerural Network','Python Advanced'])
    tracker = []
    student = Student()
    
    print("Welcome to My Library!!")
    print("Choose any option according to the operation you wanna perform :- \
        \n 1. List all available book \
        \n 2. Request to borrow   \
        \n 3. Return a book \
        \n 4. Donate a book \
        \n 5. Track your issued books \
        \n 6. Exit the portal ")
    
    while(True):
            try:
                 userChoice = int(input("Enter you choice between 1 to 6 : "))
                 if userChoice == 1:
                   Aimerz_library.display_books()
                 elif userChoice == 2:
                   Aimerz_library.borrow(input("Enter your name : "),student.requestBook())
                 elif userChoice == 3:
                   Aimerz_library.returnBook(student.returnbookfromstudent())
                 elif userChoice == 4:
                   Aimerz_library.donate(student.donationbook())
                 elif userChoice == 5:
                   flag = 0
                   print("Welcome to tracker portal!")
                   username = input("Enter your name : ")
                   for issue in tracker:
                    for key,value in issue.items():
                      if key == username:
                        print(f'{key} has borrowed {value} book')
                        flag = 1
                        break
                    if flag == 0:
                    
                        print("You haven't issued any book.")
            
                 elif userChoice == 6:
                  print("See you Again!!")
                  exit()
                 else :
                  print("Invalid Response")
            except Exception as e:

               print(f'{e}  --- invalid response')

              
        
        





