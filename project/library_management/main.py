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
    
class Storage:
    def __init__(self, folder = "user-info"):
        self.folder = folder
        self.check_folder()

    def check_folder(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
    def get_file_path(self, user_id):
        file_path = f"{self.folder}/user{user_id}-info.txt"
        return file_path
    def create_id(self):
        while True:
            new_id = random.randint(1000, 9999)
            file_path = self.get_file_path(new_id)
            if not os.path.exists(file_path):
                return str(new_id)
            
    def read_user(self, user_id):
        file_path = self.get_file_path(user_id)
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return User.get_file_format(content)
    
    def save(self, user):
        self.check_folder()
        file_path = self.get_file_path(user.user_id)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(user.format_file_txt())
        return True

    def delete_user(self, user_id):
        file_path = self.get_file_path(user_id)
        if not file_path:
            return False
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
storage = Storage()
@app.route('/user', methods = ['POST'])
def register_user():
    data = request.get_json()
    new_id = storage.create_id()
    new_user = User(user_id=new_id, name=data.get('name'), dob=data.get('dob'))
    storage.save(new_user)
    return jsonify(new_user.convert_dict()), 201
@app.route('/user/<user_id>', methods = ['PUT'])
def update_user(user_id):
    user = storage.read_user(user_id)
    if not user:
        return jsonify({"error": "Not found User"}), 404
    data = request.get_json()
    if 'name' in data:
        user.name = data['name']
    if 'dob' in data:
        user.dob = data['dob']
    storage.save(user)
    return jsonify({'message': 'Update Successfuly', "user": user.convert_dict()})
@app.route('/user/<user_id>/deactive', methods = ['PUT'])
def deactive_user(user_id):
    user = storage.read_user(user_id)
    if not user:
        return jsonify({"error": "Not found User"}), 404
    user.status = 'INACTIVE'
    storage.save(user)
    return jsonify({"message": "OK", "user": user.convert_dict()}), 200
@app.route('/user/<user_id>/', methods = ['DELETE'])
def delete_user(user_id):
    deleted = storage.delete_user(user_id)
    if deleted is False:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200
if __name__ == '__main__':
    app.run(debug=True, port=8080)