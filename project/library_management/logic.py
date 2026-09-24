from data import Storage
from user import User
from book import Book

# user_storage = Storage(folder= 'user-info', object= User)
book_storage = Storage(folder= 'book-info')

class UserMananger:
    def __init__(self):
        self.user_storage = Storage(folder = 'user-info')
    
    def get_user(self, user_id):
        return self.user_storage.read(user_id)

    def show_all_user(self):
        users = self.user_storage.list_all()
        result = []
        for user in users:
            result.append(user.convert_dict())
        return result

    def register_user(self, data):
        new_id = self.user_storage.create_id()
        # lock by new_id
        new_user = User(user_id=new_id, name=data.get('name'), dob=data.get('dob'))
        self.user_storage.save(new_user)
        # unlock / release lock new_id
        return new_user.convert_dict()
    
    def new_info(self, value, data) -> bool:
        if 'name' in data:
            value.name = data['name']
        if 'dob' in data:
            value.dob = data['dob']
        return self.user_storage.save(value)

    def deactive_user(self,user_id):
        user = self.user_storage.read(user_id)
        if not user:
            return None
        user.status = 'INACTIVE'
        self.user_storage.save(user)
        return user.convert_dict()

    def delete_user(self, user_id):
        return self.user_storage.delete(user_id)
    
def get_book(book_id):
    return book_storage.read(book_id)

def show_all_book():
    books = book_storage.list_all()
    result = []
    for book in books:
        result.append(book.convert_dict())
    return result

def register_book(data):
    new_id = book_storage.create_id()
    title = data.get('title')
    author = data.get('author')
    new_book = Book(book_id=new_id, title=title, author=author, status="AVAILABLE")
    book_storage.save(new_book)
    return new_book.convert_dict()

def new_info_book(book, data):
    if 'author' in data:
        book.author = data['author']
    if 'title' in data:
        book.title = data['title']
    book_storage.save(book)

def delete_book(book_id):
    return book_storage.delete(book_id)

def checkout(self, user_id,book_id):
    user = self.user_storage.read(user_id)
    book = book_storage.read(book_id)
    if not user or not book:
        return None, "not_found"
    if user.status != "ACTIVE":
        return None, "user_inactive"
    if not book.check_out(user_id):
        return None, "already_borrowed"
    book_storage.save(book)
    return book.convert_dict(), None

def return_book(user_id, book_id):
    book = book_storage.read(book_id)
    if not book:
        return None, "not_found"
    if book.borrowed_by != user_id:
        return None, "wrong_borrower"
    book.return_book()
    book_storage.save(book)
    return book.convert_dict(), None

def search(keyword):
    keyword = keyword.strip().lower()
    book = book_storage.list_all()
    result = []
    for b in book:
        if keyword in b.title.lower() or keyword in b.author.lower():
            result.append(b.convert_dict())
    return result