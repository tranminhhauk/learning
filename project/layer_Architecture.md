## 1. Layer Architecture (Kiến trúc phân lớp)

### - Layer Architecture là cách tổ chức code thành các lớp  xếp chồng lên nhau, mỗi lớp chỉ đảm nhận một nhóm trách nhiệm và chỉ được giao tiếp với lớp liền kề.

Về Nguyên tắc:
    
    - Chỉ lớp trên gọi xuống lớp dưới.
    - Lớp dưới không được biết đến lớp trên (để không phụ thuộc ngược).
    - Dữ liệu đi qua từng lớp như dây chuyền: request đi xuống, response đi lên.
    - Sửa 1 class không được ảnh hưởng đến class khác

### Ưu điểm:
    - Tách biệt các phần dễ Scale - Maintain - Development - Debug

# 2.  3-layer Architecture

- Chia hệ thống thành 3 tầng rõ ràng. dùng trong các hệ thống lớn

Tầng |  Vai trò |
|---|---|
| **Presentation Tier** |  Hiển thị giao diện, nhận thao tác người dùng |
| **Business logic**  | Xử lý logic nghiệp vụ, quy tắc, tính toán |
| **Data Access**  | Lưu trữ và truy xuất dữ liệu (database) 

### Flow:

 Client - > Presentation -> Business Logic -> Data access và ngược lại

#### Về ưu điểm:

    - Tách biệt frontend - Backend - Database
    - Tránh sự phụ thuộc ngược vào nhau khi debug

# 3. MVC (Model - View - Controller)

### overView: MVC là 1 pattern và được tổ chức bên trong layer Presentation

| Thành phần | Vai trò |
|---|---|
| **Model** | Chứa dữ liệu + logic nghiệp vụ liên quan đến dữ liệu đó 
| **View** | Hiển thị dữ liệu ra giao diện (HTML, Json,...)
| **Controller** | Nhận input từ người dùng, gọi Model xử lý, View để render

### Detail about responsibility: 

Controller: 

    - validate input cơ bản (HTTP method, check xem có đủ tham số, biến đầu vào không, xử lí exception)

View: 
    
    - Chịu trách nhiệm về define và convert dữ liệu đầu ra ( Jonify, html template)

Model:

    - Quản lí dữ liệu ứng dụng, logic xử lí, dữ liệu liên quan đến nghiệp vụ 

    Nguyên tắc: Không chứa logic truy vấn dữ liệu hay logic nghiệp vụ phức tạp (vì sẽ chồng lên Business layer)

### Flow:

```
Người dùng thao tác (click, submit )
        │
        ▼
   Controller nhận request
        │
        ▼
   Controller gọi Model tương ứng để xử lý 
        │
        ▼
   Model trả kết quả về Controller
        │
        ▼
   Controller chọn View phù hợp, truyền dữ liệu vào
        │
        ▼
   View trả response ra giao diện cho người dùng thấy
```

# 4. SOLID principle
1. Single Responsibility Principle

    - Luôn đảm bảo mỗi class chỉ nên chịu trách nhiệm về 1 nhiệm vụ cụ thể
    - Nhiều nhiệm vụ -> Nhiều class
2. Open/Closed Principle    

    - "Mở cho việc mở rộng, đóng cho việc sửa đổi". Nghĩa là thiết kế 1 class sao cho khi thêm 1 tính năng mới không cần phải sửa lại code cũ
    - Khi có thêm tính năng mới, nên tạo class mới chứ không if-else liên tục
    
3. Liskov Substitution Principle 

    - Bắt nguồn từ tính chất kế thừa, thiết kế class kế thừa sao cho class con phải có thể thay thế được class cha
    -> dùng abstaction

4. Interface Segregation Principle

    - Không nên thiết kế interface quá phình to, nên chia thành nhiều interface nhỏ 
    -> để Class không implement những method nó không dùng đến

5. Dependency Inversion Principle

    - Khuyến khích phụ thuộc vào abtraction không phụ thuộc vào chi tiết
    -> Giảm sự phụ thuộc đến lỗi không đáng có, code tự do linh hoạt hơn