from flet import *
from components.Book import Book

# Firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("./culminating.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class Library(UserControl):
    
    def build(self):
        self.divide = VerticalDivider(color = colors.BLACK, width = 9, thickness = 3)
        self.bookName = TextField(label = "Book Name", width = 300)
        self.authorName = TextField(label = "Author", width = 300)
        self.borrower = TextField(label = "Borrower", width = 300, multiline = True)
        self.status = RadioGroup(content = Row(controls = [
            Radio(value = "None", label = "None"),
            Radio(value = "Borrowed", label = "Borrowed")
        ]))
        self.addBtn = ElevatedButton(icon = icons.ADD_CIRCLE_ROUNDED, text = "Add Book", on_click = self.addBook, height = 50, color = colors.BLACK)
        self.dd = Dropdown(label = "Show", width = 190,  options = [
            dropdown.Option("All"),
            dropdown.Option("None"),
            dropdown.Option("Borrowed"),
        ], border_color = colors.BLACK, color = colors.BLACK, on_change = self.filter_books, value = "All", border_radius = 10)

        inputs = Column(
            controls = [
                self.bookName,
                self.authorName,
                self.borrower,
                self.status
            ], alignment = MainAxisAlignment.CENTER
        )

        filter = Container(
            content = Row(
                controls = [
                    self.dd
                ], alignment = MainAxisAlignment.END
            ),
            margin = margin.only(right = 15)
        )

        row = Container(
            content = Row(
                controls = [
                    inputs,
                    self.addBtn
                ]
            ), bgcolor = colors.BLUE_GREY_300, border_radius = 15, border = border.all(2.0, colors.BLACK), height = 400, width = 500, padding = 27
        )

        self.bookList = Row(
                height = 550,
                wrap = True,
                scroll = True,
                expand = 1
        )
        
        row1 = Row(
            controls = [
                row,
                self.divide,
                self.bookList,
            ]
        )

        return Column(
            controls = [
                filter,
                row1
            ]
        )
        
    def did_mount(self):
        self.getBooks()
        
    def filter_books(self, book):
        library = db.collection(u'library')
        if (self.dd.value == "None"):
            completed_library = library.where(u'status', u'==', "None").stream()
            self.bookList.controls.clear()
            for book in completed_library:
                self.bookList.controls.append(Book(book.id,
                                                   book.to_dict()['bookName'],
                                                   book.to_dict()['authorName'],
                                                   book.to_dict()['borrower'],
                                                   book.to_dict()['status'],
                                                   self.dd,
                                                   self.getBooks,
                                                   self.deleteBook,
                                                   db))
         
        elif (self.dd.value == "Borrowed"):
            completed_library = library.where(u'status', u'==', "Borrowed").stream()
            self.bookList.controls.clear()
            for book in completed_library:
               self.bookList.controls.append(Book(book.id,
                                                   book.to_dict()['bookName'],
                                                   book.to_dict()['authorName'],
                                                   book.to_dict()['borrower'],
                                                   book.to_dict()['status'],
                                                   self.dd,
                                                   self.getBooks,
                                                   self.deleteBook,
                                                   db))
        
        else:
            library = library.stream()
            self.bookList.controls.clear()
            for book in library :
                print(book.id)
                self.bookList.controls.append(Book(book.id,
                                                   book.to_dict()['bookName'],
                                                   book.to_dict()['authorName'],
                                                   book.to_dict()['borrower'],
                                                   book.to_dict()['status'],
                                                   self.dd,
                                                   self.getBooks,
                                                   self.deleteBook,
                                                   db))
        self.update()
    
    def getBooks(self):
        library = db.collection(u'library').stream()
        self.bookList.controls.clear()
        for book in library :
            print(book.id)
            self.bookList.controls.append(Book(book.id,
                                                book.to_dict()['bookName'],
                                                book.to_dict()['authorName'],
                                                book.to_dict()['borrower'],
                                                book.to_dict()['status'],
                                                self.dd,
                                                self.getBooks,
                                                self.deleteBook,
                                                db))
            self.update()
        
        
    def addBook(self, e):
        doc_ref = db.collection("library").document()
        doc_ref.set({
            u'bookName' : str(self.bookName.value),
            u'authorName' : str(self.authorName.value),
            u'borrower' : str(self.borrower.value),
            u'status' : str(self.status.value)
        })
        self.bookName.value = ""
        self.authorName.value = ""
        self.borrower.value = ""
        self.status.value = ""
        self.dd.value = "All"
        self.getBooks()
        
        
    def deleteBook(self, book):
        self.bookList.controls.remove(book)
        self.dd.value = "All"
        self.update()
