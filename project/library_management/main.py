from flask import Flask, jsonify , request
import logic


app = Flask(__name__)

@app.route('/user', methods = ['GET','POST'])         
def handle_user():
    if request.method == "GET":
        result = logic.show_all_user()
        return jsonify(result), 200
    
    elif request.method == "POST":
        data = request.get_json()
        new_user = logic.register_user(data)
        return jsonify({"Created":new_user}), 201
    
@app.route('/user/<user_id>', methods = ['PUT', 'DELETE'])
def update_user(user_id):
    user = logic.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if request.method == "PUT":
        data = request.get_json()
        logic.new_info(user, data)
        return jsonify({"message":"update successfuly", "user": user.convert_dict()})
    
    elif request.method == "DELETE":
        delete = logic.delete_user(user_id)
        if delete is False:
            return jsonify({"message": "Not found"}), 404
        return jsonify({"message": "User deleted successfully"}), 200
    
@app.route('/user/deactive/<user_id>', methods = ['PUT'])
def deactive(user_id):
    user = logic.deactive_user(user_id)
    if not user:
        return jsonify({"error": "User Not Found"}), 400
    return jsonify({"message": "OK", "User": user}), 200       


@app.route('/book', methods = ['GET','POST'])
def handle_book():
    if request.method == 'GET':
        result = logic.show_all_book()
        return jsonify(result), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        new_book = logic.register_book(data)
        return jsonify({"append new book": new_book}), 201

@app.route('/book/<book_id>', methods = ["PUT", "DELETE"])
def update_book(book_id):
    if request.method == "PUT":
        book = logic.get_book(book_id)
        if not book:
            return jsonify({"error": "book not found"}), 404
        data = request.get_json()
        logic.new_info_book(book, data)
        return jsonify({'message': 'Update Successfuly', "book": book.convert_dict()})

    elif request.method == "DELETE":
        delete = logic.delete_book(book_id)
        if not delete:
            return jsonify({"error": "Not found"}), 404
        return jsonify({'message': "Book deleted successfully"}), 200



@app.route('/<user_id>/checkout/<book_id>', methods = ['POST'])
def checkout_book(user_id, book_id):
    book, error = logic.checkout(user_id, book_id)
    if error == "not_found":
        return jsonify({"error": "Not found"}), 404
    if error == "user_inactive":
        return jsonify({"error": "User Not Active"}), 404
    if error == "already_borrowed":
        return jsonify({"error": "Book already borrowed"}), 400
    return jsonify({"message": "Checked out", "book": book}), 200


@app.route('/<user_id>/return/<book_id>', methods=['POST'])
def return_book(user_id, book_id):
    book, error = logic.return_book(user_id, book_id)
    if error == "not_found":
        return jsonify({"error": "Book not found"}), 404
    if error == "wrong_borrower":
        return jsonify({"error": "This user did not borrow this book"}), 400
    return jsonify({"message": "Returned", "book": book}), 200


@app.route('/book/search', methods = ["GET"])
def search_book():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400
    result = logic.search(keyword)
    return jsonify(result), 200


if __name__ == '__main__':
    app.run(debug=True, port=8080)