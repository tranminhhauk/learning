import os 
import random

class Storage:
    def __init__(self, folder):
        self.folder = folder
        self.check_folder()

    def check_folder(self):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def get_file_path(self, id) -> str:
        file_path = f"{self.folder}/{id}-info.txt"
        return file_path
    
    def create_id(self) -> str:
        while True:
            new_id = random.randint(1000, 9999) # TODO: enhancement
            file_path = self.get_file_path(new_id)
            if not os.path.exists(file_path):
                return str(new_id) 

    def read(self, id, expected_class):
        file_path = self.get_file_path(id)
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return expected_class.get_file_format(content)
    
    def save(self, item) -> bool:
        self.check_folder()
        file_path = self.get_file_path(item.get_id())
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(item.format_file_txt())
        return True

    def delete(self, id) -> bool:
        file_path = self.get_file_path(id)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def list_all(self, expected_class) -> list:
        lists = []
        for file in os.listdir(self.folder):
            with open(f"{self.folder}/{file}", "r", encoding="utf-8") as f:
                item = expected_class.get_file_format(f.read())
                lists.append(item)
        return lists
    
