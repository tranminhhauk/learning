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