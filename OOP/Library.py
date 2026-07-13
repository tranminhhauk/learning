import random
import string

class Book:
    def __init__(self, title, author, ip):
        self.title = title
        self.author = author
        self.ip = ip
        self.is_available = True
    def check_out(self):
        if self.is_available == False:
            print('error! this book is already check out')
            return False
        else:
            self.is_available = False
            return True
    def return_book(self):
        self.is_available = True
    def __str__(self):
        if self.is_available == True:
            status = 'ready'
        else:
            status = 'not ready'
        return f'{self.title} {self.ip} - {status}'
class Member:
    def __init__(self, name):
        self.name = name
        self.member_id = random.randint(1000, 9999)
        self.borrowed_book = []
        
    def borrow_book(self, book):
        if len(self.borrowed_book) >= 3:
            print('error! member is has more than 3 book')
            return False
        else:
            self.borrowed_book.append(book) 
            return True
       
    def return_book(self, book):
        if book in self.borrowed_book:
            self.borrowed_book.remove(book)
            return True
        else:
            print('error! book not in member list')
            return False
    def __str__(self):
        return f' {self.name} ID: {self.member_id} - Borrow {len(self.borrowed_book)}'

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)
    def register_member(self, member):
        self.members.append(member)
    def check_out_book(self, member_name, ip):
        find_book = None
        for b in self.books:
            if b.title == ip:
                find_book = b
                break
        find_member = None
        for mem in self.members:
            if mem.name == member_name:
                find_member = mem
                break
        if find_book and find_member:
            if find_book.check_out() == True:
                if find_member.borrow_book(find_book) == True:
                    return f'{member_name} muon thanh cong: {find_book.title}'
                else:
                    find_book.return_book()
                    return f'{member_name} da muon du 3 cuon'
            return f'{find_book.title} hien da duoc muon'
        return f'khong tim thay sach hoac thanh vien nay'
    def return_book(self, member_name, ip):
        find_book = None
        for b in self.books:
            if b.title == ip:
                find_book = b
                break
        find_member = None 
        for m in self.members:
            if m.name == member_name:
                find_member = m
                break
        if find_book and find_member:
            if find_member.return_book(find_book) == True:
                find_book.return_book()
                return f'{member_name} da tra xong: {find_book.title}'
            return f'{find_book.title} khong co ttron {member_name}'
        return f'khong khop thong tin tra sach'
    
lib = Library('Thu vien')
with open('readme.md.txt', 'r', encoding= 'utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        values = line.split(',')

        if values[0] =='Book':
            obj = Book(values[1], values[2], values[3])
            lib.add_book(obj)
            print(f"da nap sach {obj.title} ")
        elif values[0] == 'Member':
            obj = Member(values[1])
            lib.register_member(obj)
            print(f'da tao thanh vien {obj.name}')
        elif values[0] == 'Borrow':
            ket_qua = lib.check_out_book(values[1], values[2])
            print(ket_qua)
        elif values[0] == 'Return':
            ket_qua = lib.return_book(values[1], values[2])
            print(ket_qua)
