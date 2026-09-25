from data import Storage
from user import User
from book import Book

class UserMananger:
    def __init__(self):
        self.user_storage = Storage(folder = 'user-info')
    
    def get_user(self, user_id):
        return self.user_storage.read(user_id, User)

    # def show_all_user(self):
    #     users = self.user_storage.list_all(User)
    #     result = []
    #     for user in users:
    #         result.append(user)
    #     return result

    def register_user(self, data):
        new_id = self.user_storage.create_id()
        # lock by new_id
        # ->> TODO
        new_user = User(user_id=new_id, name=data.get('name'), dob=data.get('dob'))
        self.user_storage.save(new_user)
        # unlock / release lock new_id
        # ->> TODO
        return new_user
    
    def new_info(self, user_info, data) -> bool:
        if 'name' in data:
            user_info.name = data['name']
        if 'dob' in data:
            user_info.dob = data['dob']
        return self.user_storage.save(user_info)

    def deactive_user(self,user_id):
        user = self.user_storage.read(user_id, User)
        if not user:
            return None
        user.status = 'INACTIVE'
        self.user_storage.save(user)
        return user

    def delete_user(self, user_id):
        return self.user_storage.delete(user_id)

class BookManagement:
    def __init__(self):
        self.book_storage = Storage(folder= 'book-info')

    def get_book(self,book_id):
        return self.book_storage.read(book_id, Book)

    # def show_all_book(self):
    #     books = self.book_storage.list_all(Book)
    #     result = []
    #     for book in books:
    #         result.append(book)
    #     return result

    def register_book(self,data):
        new_id = self.book_storage.create_id()
        title = data.get('title')
        author = data.get('author')
        new_book = Book.create_new_book(book_id=new_id, title=title, author=author)
        self.book_storage.save(new_book)
        return new_book

    def new_info_book(self, book, data):
        if 'author' in data:
            book.author = data['author']
        if 'title' in data:
            book.title = data['title']
        self.book_storage.save(book)

    def delete_book(self, book_id):
        return self.book_storage.delete(book_id)
    
    def search(self, keyword):
        keyword = keyword.strip().lower()
        book = self.book_storage.list_all(Book)
        result = []
        for b in book:
            if keyword in b.title.lower() or keyword in b.author.lower():
                result.append(b)
        return result

class LibraryService:
    def __init__(self, user_manager: UserMananger, book_management: BookManagement):
        self.user_manager = user_manager
        self.book_management = book_management

    def checkout(self, user_id,book_id):
        user = self.user_storage.read(user_id)
        book = self.book_storage.read(book_id)
        if not user or not book:
            return None, "not_found"
        if user.status != "ACTIVE":
            return None, "user_inactive"
        if not book.check_out(user_id):
            return None, "already_borrowed"
        self.book_storage.save(book)
        return book, None

    def return_book(self, user_id, book_id):
        book = self.book_storage.read(book_id)
        if not book:
            return None, "not_found"
        if book.borrowed_by != user_id:
            return None, "wrong_borrower"
        book.return_book()
        self.book_storage.save(book)
        return book, None