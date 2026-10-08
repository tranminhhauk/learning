# Basic
## 1. what is OOP? Explain inheritance, encapsulation, polymorphism, and abstraction with a real-life example
- OOP mô hình lập trình hướng đối tượng dựa trên class - Object: mỗi object bao gồm atribute và method, OOP chia nhỏ hệ thống lớn thành các đối tượng độc lập 

### 1. encapsulation: 
Gom nhóm các attributes và method có liên quan với nhau  vào 1 class, che giấu chi tiết bên trong khỏi sự can thiệp từ bên ngoaì
### 2. inheritance
Cho phép 1 lớp con kế thừa - tái sử dụng những gì từ lớp cha-> giảm thiểu việc trùng lặp code, đồng thời lớp con cũng có thể có những cái riêng 
### 3. polymorphism
Khái niệm cho phép các object thuộc class khác nhau có thể cùng có 1 method với atributes khác nhau - nhiều hình thái
### 4. abstraction
Bao gồm việc ẩn đi các chi tiết phức tạp bên trong, tập trung vào việc trả lời cái gì -> làm gì thay vì làm như thế nào, giúp method linh hoạt dễ mở rộng
## 2.. How is encapsulation different from data abstraction?

encapsulation: che giấu, ẩn đi, bảo vệ dữ liệu của object - tránh sửa đổi từ bên ngoài, "Làm sao để bảo vệ dữ liệu an toàn", đóng gói là công cụ thực  thi

abtraction: Tập trung vào việc ẩn đi sự phức tạp của method, "tính năng gì", trừu tượng liên quan đến vấn đề thiết kế

## 3. Describe the difference between interface and abstract class. When would you use each?
- Khác biệt cốt lõi, Abtract class định nghĩa bản chất của đối tượng (là gì), interface định nghĩa đối tượng có thể làm gì
- sử dụng abtract khi cần tái sử dụng code, định nghĩa chung ở lớp cha, và để các lớp con tự implement
- sử dụng interface khi các class khác nhau về bản chất nhưng sở hữu cùng 1 phương thức (dùng trong Dependency injection)
## 4.. What are Access modifiers in Java? Explain each.
-- Java
## 5. Can we declare an abstract method as private? Why or why not?
Không thể khai báo 1 abstract method private vì abstract là method ghi đè không thực thi , mục đích là tạo ra cái khuôn mẫu để các lớp con ghi đè 

Mục đích của private là quyt định method đó chỉ được truy cập nội bộ trong class khai báo nó, các lớp con kế thừa không nhìn thấy không biết , không có quyền truy cập
## 6. Can a method or a class be final and abstract at the same time? Explain.
TODO
## 7. What is constructor? How many types of constructors are there?
Constructor là 1 hàm đặt biệt tự động gọi khi 1 object được tạo ra, nhiệm vụ là khởi tạo giá trị ban đầu bao gồm các thuộc tinh của đối tượng

Trong python có 2 constructor đặt biệt, __init__, khởi tạo giá trị ban đầu cho đối tượng vừa tạo  __new__, dùng để tạo đối tượng, cấp phát bộ nhớ, ít dùng

## 8. What is method overloading? How is it different from method overriding?

TODO

## 9. What is an enum? When would you use it instead of constants?

TODO
## 10. What is a static class? What are static methods?

TODO

# Advanced

## 1. What is SOLID? Describe each principle and give an example of violating one.
- SOLID là 5 nguyên tắc quan trọng trong lập trình hướng đối tượng về thiết kế hệ thống

1. Single Responsibility Principle
    - Luôn đảm bảo mỗi class chỉ nên chịu trách nhiệm về 1 nhiệm vụ cụ thể, chỉ có 1 lí do để thay đổi 
    - Nhiều nhiệm vụ -> Nhiều class

2. Open/Closed Principle    
    - "Mở cho việc mở rộng, đóng cho việc sửa đổi". Nghĩa là thiết kế 1 class sao cho khi thêm 1 tính năng mới không cần phải sửa lại code cũ
    - Khi có thêm tính năng mới, nên tạo class mới chứ không if-else liên tục để không sửa lại code cũ

3. Liskov Substitution Principle 
    - Bắt nguồn từ tính chất kế thừa, thiết kế class kế thừa sao cho class con phải có thể thay thế được class cha mà vẫn đúng, nếu không thay thế được:
    -> dùng abstaction

4. Interface Segregation Principle
    - Không nên thiết kế interface quá phình to, nên chia thành nhiều interface nhỏ 
    -> để Class không implement những method nó không dùng đến

5. Dependency Inversion Principle
    - Khuyến khích phụ thuộc vào abtraction không phụ thuộc vào chi tiết
    -> Giảm sự ràng buộc, code tự do linh hoạt hơn, dễ test, dễ thay thế 

## 2. What is dependency injection? Why does it matter for testability?

dependency injection là kĩ thuật thực thi truyền các đối tượng mà class cần, bắt nguồn từ nguyên lí Dependency Inversion

## 3. What is the Singleton pattern? When would you NOT use it?

TODO

## 4. What is the Factory pattern? How does it differ from the Abstract Factory pattern?

## 5. What is the difference between composition and inheritance? When do you prefer composition?

## 6. Explain the Open/Closed Principle. How would you refactor a class that violates it?

Mở để mở rộng: có thể thêm hành vi, tính năng mới.
Đóng để sửa đổi: khi thêm tính năng mới, không phải sửa code cũ đã chạy ổn định.
-> dựa vào abstraction và đa hình để tính năng mới được thêm vào bằng cách viết class mới thay vì sửa class cũ

## 7. What is the Liskov Substitution Principle? Give an example of a violation.

Nếu B là con của A, thì phải có thể thay thế object A bằng object B mà code vẫn chạy đúng, cụ thể:

- lớp con không đòi nhiều input hơn so vơi lớp cha 
- lớp con không trả kết quả khác ý nghĩa so với lớp cha
- kiểm tra điều kiện cha đúng -> con cũng phải đúng
- lớp con không có lỗi mà lớp cha không có