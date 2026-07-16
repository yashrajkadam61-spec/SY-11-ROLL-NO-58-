class book:
    def __init__(self,book_id,title,author):
        self .book_id = book_id
        self .title = title
        self .author = author
        self .is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else  "Available"
        return f"ID:(self.book_id), Title: (self.title), Author: (self.author), Status: (status)"
    
    #student class
    class student:
        def __init__(self,student_id,name):
            self.student_id = student_id
            self.name = name
            self.borrowed_book = []
        def borrowed_books(self,books):
            self.borrowed_book.append(books)  
        def return_books(self,books):
            self.borrowed_books.remove(books)   

    #library class
    class library:
        def __init__(self):
            self.books = {}   
            self.student = {}

        def add_book(self,book):
            self.books[book.book_id] = book
            print(f"student 'student.name'registered successfuly.")  
            return
        

        
               

        
          

        