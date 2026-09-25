from flask import Flask, request
from logic import *
from common.common import format_resp
from common import http_method

app = Flask(__name__)

user_manager = UserMananger()
book_management = BookManagement()
library_service = LibraryService(user_manager, book_management)

@app.route('/user', methods = [http_method.GET, http_method.POST])         
def handle_user():
    if request.method == http_method.GET:
        result = user_manager.show_all_user()
        user = []
        for u in result:
            user.append(u.convert_dict())
        return format_resp({"show all" : user}, 200)
    
    elif request.method == http_method.POST:
        data = request.get_json()
        new_user = user_manager.register_user(data)
        view_out = new_user.convert_dict()
        return format_resp({"created new user" : view_out}, 201)
    
@app.route('/user/<user_id>', methods = [http_method.PUT, http_method.DELETE])
def update_user(user_id):
    user = user_manager.get_user(user_id)
    if not user:
        return format_resp({"error": "User not found"},404)
    
    if request.method == http_method.PUT:
        data = request.get_json()
        is_success = user_manager.new_info(user, data)
        if is_success:
            view_out = user.convert_dict()
            return format_resp({"update successfuly": view_out}, 200)
        return format_resp({"msg": "update failed"}, 400)
    
    elif request.method == http_method.DELETE:
        delete = user_manager.delete_user(user_id)
        if delete is False:
            return format_resp({"msg": "Not found"}, 404)
        return format_resp({"msg": "User deleted successfully"}, 200)
    
@app.route('/user/deactive/<user_id>', methods = [http_method.PUT])
def deactive(user_id):
    user = user_manager.deactive_user(user_id)
    if not user:
        return format_resp({"error": "User Not Found"}, 400)
    view_out = user.convert_dict()
    return format_resp({"Deactive Ok": view_out}, 200)   

@app.route('/book', methods = [http_method.GET, http_method.POST])
def handle_book():
    if request.method == http_method.GET:
        result = book_management.show_all_book()
        books =[]
        for b in result:
            books.append(b.convert_dict())
        return format_resp({"Show all Books": books}, 200)
    
    elif request.method == http_method.POST:
        data = request.get_json()
        new_book = book_management.register_book(data)
        view_out = new_book.convert_dict()
        return format_resp({"append new book": view_out}, 201)

@app.route('/book/<book_id>', methods = [http_method.PUT, http_method.DELETE])
def update_book(book_id):
    if request.method == http_method.PUT:
        book = book_management.get_book(book_id)
        if not book:
            return format_resp({"error": "book not found"}, 404)
        data = request.get_json()
        book_management.new_info_book(book, data)
        view_out = book.convert_dict()
        return format_resp({'Update Successfuly': view_out}, 200)

    elif request.method == http_method.DELETE:
        delete = book_management.delete_book(book_id)
        if not delete:
            return format_resp({"error": "Not found"}, 404)
        return format_resp({'message': "Book deleted successfully"}, 200)



@app.route('/<user_id>/checkout/<book_id>', methods = ['POST'])
def checkout_book(user_id, book_id):
    book, error = library_service.checkout(user_id, book_id)
    if error == "not_found":
        return format_resp({"error": "Not found"}, 404)
    if error == "user_inactive":
        return format_resp({"error": "User Not Active"}, 404)
    if error == "already_borrowed":
        return format_resp({"error": "Book already borrowed"}, 400)
    view_out = book.convert_dict()
    return format_resp({"Checked out OK": view_out}, 200)


@app.route('/<user_id>/return/<book_id>', methods=['POST'])
def return_book(user_id, book_id):
    book, error = library_service.return_book(user_id, book_id)
    if error == "not_found":
        return format_resp({"error": "Book not found"}, 404)
    if error == "wrong_borrower":
        return format_resp({"error": "This user did not borrow this book"}, 400)
    view_out = book.convert_dict()
    return format_resp({"Returned OK": view_out}, 200)


@app.route('/book/search', methods = ["GET"])
def search_book():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return format_resp({"error": "Missing keyword"}, 400)
    result = book_management.search(keyword)
    books =[]
    for b in result:
        books.append(b.convert_dict())
    return format_resp({"Book info": books}, 200)


if __name__ == '__main__':
    app.run(debug=True, port=8080)