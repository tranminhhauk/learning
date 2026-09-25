class User:
    def __init__(self, user_id, name, dob, status):
        self.user_id = user_id
        self.name = name
        self.dob = dob
        self.status = status
        
    def get_id(self):
        return self.user_id
    
    def convert_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "name": self.name,
            "dob" : self.dob, 
            "status" : self.status
                }

    def format_file_txt(self) -> str:
        return f"{self.user_id}|{self.name}|{self.dob}|{self.status}"

    @classmethod
    def create_new_user(cls, user_id, name, dob):
        return cls(user_id=user_id, name=name, dob=dob, status = "ACTIVE")
    
    @classmethod
    def get_file_format(cls, data):
        get_data = data.strip().split('|')
        if len(get_data) >= 4:
            return cls(user_id = get_data[0], name = get_data[1], dob = get_data[2], status = get_data[3])
        return None