from flask import Flask, jsonify , request
import random
import os

app = Flask(__name__)

class User:
    def __init__(self, user_id, name, dob, status="ACTIVE"):
        self.user_id = user_id
        self.name = name
        self.dob = dob
        self.status = status
    def get_id(self):
        return self.user_id
    def convert_dict(self):
        return {"user_id": self.user_id, "name": self.name, "dob" : self.dob, "status" : self.status}
    def format_file_txt(self):
        return f"{self.user_id}|{self.name}|{self.dob}|{self.status}"
    
    @classmethod
    def get_file_format(cls, data):
        get_data = data.split('|')
        if len(get_data) >= 4:
            return cls(user_id = get_data[0], name = get_data[1], dob = get_data[2], status = get_data[3])
        return None
    
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

    
class Storage:
    def __init__(self, folder, object):
        self.folder = folder
        self.object = object
        self.check_folder()

    def check_folder(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def get_file_path(self,id):
        file_path = f"{self.folder}/{id}-info.txt"
        return file_path
    
    def create_id(self):
        while True:
            new_id = random.randint(1000, 9999)
            file_path = self.get_file_path(new_id)
            if not os.path.exists(file_path):
                return str(new_id)
            
    def read(self, id):
        file_path = self.get_file_path(id)
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return self.object.get_file_format(content)
    
    def save(self, item):
        self.check_folder()
        file_path = self.get_file_path(item.get_id())
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(item.format_file_txt())
        return True

    def delete(self, id):
        file_path = self.get_file_path(id)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            return False
        
user_storage = Storage(folder= 'user-info', object= User)
book_storage = Storage(folder= 'book-info', object= Book)

@app.route('/user', methods = ['POST'])
def register_user():
    data = request.get_json()
    new_id = user_storage.create_id()
    new_user = User(user_id=new_id, name=data.get('name'), dob=data.get('dob'))
    user_storage.save(new_user)
    return jsonify(new_user.convert_dict()), 201
@app.route('/user/<user_id>', methods = ['PUT'])
def update_user(user_id):
    user = user_storage.read(user_id)
    if not user:
        return jsonify({"error": "Not found User"}), 404
    data = request.get_json()
    if 'name' in data:
        user.name = data['name']
    if 'dob' in data:
        user.dob = data['dob']
    user_storage.save(user)
    return jsonify({'message': 'Update Successfuly', "user": user.convert_dict()})
@app.route('/user/<user_id>/deactive', methods = ['PUT'])
def deactive_user(user_id):
    user = user_storage.read(user_id)
    if not user:
        return jsonify({"error": "Not found User"}), 404
    user.status = 'INACTIVE'
    user_storage.save(user)
    return jsonify({"message": "OK", "user": user.convert_dict()}), 200
@app.route('/user/<user_id>', methods = ['DELETE'])
def delete_user(user_id):
    deleted = user_storage.delete(user_id)
    if deleted is False:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200

@app.route('/book', methods = ['POST'])
def register_book():
    data = request.get_json()
    new_book_id = book_storage.create_id()
    new_title = data.get('title')
    new_author = data.get('author')
    new_book = Book(book_id=new_book_id, title= new_title, author= new_author, status ='AVAILABLE')
    book_storage.save(new_book)
    return jsonify(new_book.convert_dict()), 201

@app.route('/book/<book_id>', methods = ['DELETE'])
def delete_book(book_id):
    delete = book_storage.delete(book_id)
    if not delete:
        return jsonify({"error": "Not found"}), 404
    return jsonify({'message': "Book deleted successfully"}), 200

@app.route('/user/<user_id>/checkout/<book_id>', methods = ['POST'])
def checkout_book(user_id, book_id):
    user = user_storage.read(user_id)
    book = book_storage.read(book_id)
    if not user or not book:
        return jsonify({"error": "Not found"}), 404
    if user.status != "ACTIVE":
        return jsonify({"error": "User Not Active"}), 404
    if not book.check_out(user_id):
        return jsonify({"error": "Book already borrowed"}), 400
    book_storage.save(book)
    return jsonify({"message": "Checked out", "book": book.convert_dict()}), 200


@app.route('/user/<user_id>/return/<book_id>', methods=['POST'])
def return_book(user_id, book_id):
    book = book_storage.read(book_id)
    if not book:
        return jsonify({"error": "Not found"}), 404
    if book.borrowed_by != user_id:
        return jsonify({"error": "This user did not borrow this book"}), 400
    book.return_book()
    book_storage.save(book)
    return jsonify({"message": "Returned", "book": book.convert_dict()}), 200
 
if __name__ == '__main__':
    app.run(debug=True, port=8080)