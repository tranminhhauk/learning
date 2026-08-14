from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

def check_folder():
    if not os.path.exists("user-info"):
        os.makedirs("user-info")

def create_id():
    while True:
        new_id = random.randint(1000, 9999)
        file_path = f"user-info/user{new_id}-info.txt"
        if not os.path.exists(file_path):
            return str(new_id)

def read_user(user_id):
    file_path = f"user-info/user{user_id}-info.txt"
    print(file_path)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        parts = content.split('|')
        return {"user_id": parts[0],
                "name": parts[1],
                "dob": parts[2],
                "status": parts[3]}

def save(user_id, name, dob, status):
    file_path = f"user-info/user{user_id}-info.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"{user_id}|{name}|{dob}|{status}")

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/register', methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        name = request.form.get('name')
        dob = request.form.get('dob')
        status = "ACTIVE"
        
        check_folder()
        new_id = create_id()
        save(new_id, name, dob, status)
        
        return f"Created Successfully {new_id} | {name} | {dob} | {status}"
    else:
        return render_template('register.html')
    
@app.route('/update', methods=["GET", "POST"])
def update():
    if request.method == "POST":
        user_id = request.form.get('user_id').strip()
        user = read_user(user_id)
        if not user:
            return f"ERROR, Not Found ID: {user_id}"
            
        return render_template('update.html', name=user['name'], dob=user['dob'], user_id=user['user_id'])
    else:
        return render_template('update.html')

@app.route('/update/save', methods=["POST"])
def save_update():
    user_id = request.form.get('user_id')
    new_name = request.form.get('name')
    new_dob = request.form.get('dob')
    user = read_user(user_id)
    if not user:
        return f"ERROR: User {user_id} Not Found"
    
    save(user_id, new_name, new_dob, user['status'])
    return f"Update successful for ID {user_id}: {new_name}, {new_dob}"

@app.route('/deactivate', methods=['GET', 'POST'])
def deactive_info():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        user = read_user(user_id)
        if not user:
            return f"ERROR: User {user_id} Not Found"
        return render_template('deactivate.html', name=user['name'], dob=user['dob'], user_id=user['user_id'], status=user['status'])
    else:
        return render_template('deactivate.html')

@app.route('/deactivate/save', methods=['POST']) 
def save_deactive():
    user_id = request.form.get('user_id')
    new_status = request.form.get('status')
    
    user = read_user(user_id)
    if not user:
        return f"ERROR: User {user_id} Not Found"
    
    save(user_id, user['name'], user['dob'], new_status)
    return f"Status changed User {user_id} : {new_status}"


if __name__ == '__main__':
    app.run(debug=True, port=8080)