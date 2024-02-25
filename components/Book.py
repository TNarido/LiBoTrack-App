from flet import *

class Book(UserControl):

    def __init__(self, id, bookName, authorName, borrower, status, dd, getBooks, deleteBook, db):
        super().__init__()
        self.id = id
        self.bookName = bookName
        self.authorName = authorName
        self.borrower = borrower
        self.status = status
        self.dd = dd
        self.getBooks = getBooks
        self.delete = deleteBook
        self.db = db
        
    def build(self):
        self.text1 = Text(value = str(self.bookName), size = 25, weight = FontWeight.BOLD, font_family = "Times New Roman", width = 350)
        self.text2 = Text(value = str(self.authorName), size = 14, font_family = "Times New Roman", italic = True)
        self.text3 = Text(value = str(self.borrower), size = 15, font_family = "RobotoSlab")
        self.text4 = Text(value = str(self.status), size = 20, font_family = "Consolas", weight = FontWeight.BOLD)
        self.design = Text("✯⸺⸺✯⸺⸺✯⸺⸺✯⸺⸺✯⸺⸺✯⸺⸺✯")

        #============================EDIT SECTION============================#
        
        self.editBookName = TextField(value = str(self.bookName), label = "Book Name", width = 300)
        self.editAuthorName = TextField(value = str(self.authorName), label = "Author", width = 300)
        self.editBorrower = TextField(value = str(self.borrower), label = "Borrower", multiline = True, width = 300)
        self.editStatus = RadioGroup(content = Row(controls = [
            Radio(value = "None", label = "None"),
            Radio(value = "Borrowed", label = "Borrowed")
        ]), value = str(self.status))
        self.savebtn = IconButton(icon=icons.CHECK, on_click=self.updateBook)
        self.cancelbtn = IconButton(icon=icons.CANCEL, on_click=self.cancelEdit)
        
        info = Column(
            controls = [
                self.text1,
                self.text2,
                self.design,
                self.text3,
                self.text4
            ], alignment = MainAxisAlignment.START
        )

        menu = PopupMenuButton(
                items = [
                    PopupMenuItem(text = "Edit", on_click = self.showEdit),
                    PopupMenuItem(), #divider
                    PopupMenuItem(text = "Delete", on_click = self.deleteBook),
                ]
            )
        
        option = Container(
            content = Column(
                controls = [
                    self.savebtn,
                    self.cancelbtn
                ]
            ), bgcolor = colors.BLUE_GREY_100, border_radius = 15, border = border.all(3.0, colors.BLACK)
        )

        self.bookrow = Container(
            content = Row(
                controls=[
                    info,
                    menu
                ],
                width = 100,
                alignment = MainAxisAlignment.SPACE_BETWEEN
            ), width = 400, padding = 5, border = border.all(2.0, colors.BLACK), border_radius = 10,
        )

        if self.status == "None":
            self.bookrow = Container(
                content = Row(
                    controls = [
                        info,
                        menu
                    ],
                    width = 100,
                    alignment = MainAxisAlignment.SPACE_BETWEEN
                ), width = 400, padding = 5, border = border.all(2.0, colors.BLACK), border_radius = 10,
            )
            
        elif self.status == "Borrowed":
            self.bookrow = Container(
                content = Row(
                    controls = [
                        info,
                        menu
                    ],
                    width = 100,
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                ), width = 400, padding = 5, bgcolor = colors.RED_300, border = border.all(2.0, colors.BLACK), border_radius = 10
            )

        self.editInputs = Container(
            content = Column(
                controls = [
                    self.editBookName,
                    self.editAuthorName,
                    self.editBorrower,
                    self.editStatus
                ], width = 10
            ), width = 340, padding = 5, bgcolor = colors.BLUE_GREY_100, border = border.all(3.0, colors.BLACK), border_radius = 10
        )
  
        self.editrow = Row(
            controls = [
                self.editInputs,
                option
            ], width = 400, alignment = MainAxisAlignment.CENTER, visible = False
        )

        return Column(
            controls = [
                self.bookrow,
                self.editrow
            ]
        )
        
    def showEdit(self, e):
        self.bookrow.visible=False
        self.editrow.visible=True
        self.update()
        
    def cancelEdit(self, e):
        self.bookrow.visible=True
        self.editrow.visible=False
        self.update()
        
    def updateBook(self, e):
        newBookName = str(self.editBookName.value)
        newAuthorName = str(self.editAuthorName.value)
        newBorrower = str(self.editBorrower.value)
        newStatus = str(self.editStatus.value)
        book_ref = self.db.collection(u'library').document(self.id)
        book_ref.update({
                u'bookName' : newBookName,
                u'authorName' : newAuthorName,
                u'borrower' : newBorrower,
                u'status' : newStatus,
            })
        self.editrow.visible=False
        self.bookrow.visible=True
        self.dd.value = "All"
        self.getBooks()
        
    def deleteBook(self, e):
        self.delete(self)
        book_ref = self.db.collection(u'library').document(self.id)
        book_ref.delete()
        self.getBooks()