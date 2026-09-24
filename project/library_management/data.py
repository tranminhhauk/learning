import os 
import random

class Storage:
    def __init__(self, folder):
        self.folder = folder
        self.check_folder()

    def check_folder(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def get_file_path(self,id):
        file_path = f"{self.folder}/{id}-info.txt"
        return file_path
    
    def create_id(self):
        while True:
            new_id = random.randint(1000, 9999) # TODO: enhancement
            file_path = self.get_file_path(new_id)
            if not os.path.exists(file_path):
                return str(new_id) 

# A -> 456 -> 456-info.txt  -> new id
# B -> 456 -> 456-info.txt -> new ifo           

    def read(self, id):
        file_path = self.get_file_path(id)
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return self.object.get_file_format(content)
    
    def save(self, item) -> bool:
        self.check_folder()
        file_path = self.get_file_path(item.get_id())
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(item.format_file_txt())
        return True

# 4563|abc|10/20/3040|ACTIVE
# 4563|xyz|10/20/3040|ACTIVE

    def delete(self, id):
        file_path = self.get_file_path(id)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            return False

    def list_all(self, expected_class):
        lists = []
        for file in os.listdir(self.folder):
            with open(f"{self.folder}/{file}", "r", encoding="utf-8") as f:
                item = expected_class.get_file_format(f.read())
                lists.append(item)
        return lists
    
