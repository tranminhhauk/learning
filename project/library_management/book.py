class Book:
    def __init__(self, book_id, title, author, status = "AVAILABLE", borrowed_by = ""):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.borrowed_by = borrowed_by
    def get_id(self):
        return self.book_id
    def check_out(self, user_id):
        if self.status == 'BORROWED':
            print("this book is already check out")
            return False
        else:
            self.status = 'BORROWED'  
            self.borrowed_by = user_id
            return True
    def return_book(self):
        self.status = 'AVAILABLE'
        self.borrowed_by = ""
    def convert_dict(self):
        return {"book_id": self.book_id, "title": self.title, "author": self.author, "status": self.status,"borrowed_by": self.borrowed_by}
    def format_file_txt(self):
        return f"{self.book_id}|{self.title}|{self.author}|{self.status}|{self.borrowed_by}"
    @classmethod
    def get_file_format(cls, data):
        get_data = data.split('|')
        if len(get_data) > 4:
            borrowed_by = get_data[4]
        else:
            borrowed_by = ""  
        return cls(book_id = get_data[0], title = get_data[1], author = get_data[2], status = get_data[3], borrowed_by=borrowed_by)

