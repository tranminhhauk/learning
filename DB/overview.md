## DataBase 

Là một tập hợp dữ liệu liên quan đến nhau được tổ chức dữ liệu 1 cách có cấu trúc -> để lưu trữ, truy cập dễ dàng, quản lí và chia sẻ cho nhiều người dùng hoặc ứng dụng cùng lúc
  
Dược kiểm soát bởi Database management system - DBMS

    - DBMS được thiết kế nhằm truy xuất thao tác và quản lí dữ liệu bên trong DB
    - Sử dụng các ngôn ngữ truy vấn để đưa ra các yêu cầu truy cập, sửa đổi, cập nhật,... 

### Database management System

Là phần mềm dùng để tạo, quản lí và vận hành database VD: postgreSQL, MySQL, SQLite. Chức năng chính bao gồm

    • Định nghĩa cấu trúc dữ liệu (schema)
    • Truy vấn, thêm, sửa, xóa dữ liệu
    • Kiểm soát truy cập đồng thời (nhiều người dùng cùng lúc)
    • Phân quyền và bảo mật
    • Đảm bảo toàn vẹn dữ liệu (constraint, transaction)
    • Sao lưu (backup) và phục hồi (restore)

-> Database là dữ liệu, DBMS là phần mềm quản lí cái dữ liệu đó 

Dữ liệu thông thường được lưu trên RAM (tắt server là mất) or trong các file text, JSON,... có nhược điểm là chậm, khó tìm kiếm, không có phân quyền

Database giải quyết được vấn đề:

    Tránh trùng lặp và lãng phí bộ nhớ
    Đảm bảo tính nhất quán
    Khả năng tìm kiếm và xử lý tốc độ cao
    Giải quyết tranh chấp khi nhiều người dùng chung
    Bảo mật và phân quyền nghiêm ngặt
    Khôi phục dữ liệu khi gặp sự cố 
### 2 Loại Database phổ biến

1. Relational - SQL

    - Dữ liệu được lưu trong các table bao gồm (row và column), liên kết với nhau qua primary key và foreign key (khóa chính và khóa ngoại), truy vấn bằng ngoon ngữ SQL
    
    Bảng dữ liệu khi tạo xong sẽ được lưu vào ổ cứng của máy tính hoặc server đang chạy DB đó

    VD về các DBMS dùng SQL: posgreSQL, MySQL

2. Non-relational - NoSQL

Cấu trúc linh hoạt và đa dạng hơn, không bị ràng buộc cột và hàng như trên -> dễ mở rộng, bao gồm nhiều dạng:

    • Document
    • Key-Value
    • Column-family
    • Graph 

### SQL

SQL là ngôn ngữ chuẩn được sử dụng để tương tác với các Hệ quản trị cơ sở dữ liệu quan hệ. Cho phép người dùng tạo và sửa đổi cấu trúc cơ sở dữ liệu, Các lệnh SQL được quy định theo tiêu chuẩn quốc tế 
   
Các khái niệm cơ bản:

    Table (Bảng): Nơi lưu trữ dữ liệu của một đối tượng cụ thể (Ví dụ: bảng User chứa thông tin người dùng, bảng Order chứa thông tin đơn hàng).

    Column: Các thuộc tính hoặc đặc điểm của đối tượng

    Row: Một dữ liệu cụ thể và duy nhất của đối tượng đó (Ví dụ: thông tin chi tiết của một người dùng cụ thể)


Các lệnh ngôn ngữ SQL cơ bản

1. DDL – Data Definition Language – Ngôn ngữ định nghĩa dữ liệu

Được sử dụng để định nghĩa và quản lý cấu trúc của cơ sở dữ liệu và các đối tượng trong đó như bảng, chỉ mục, và khóa.

    CREATE: Tạo ra một cơ sở dữ liệu mới, bảng mới, hoặc đối tượng khác 

    ALTER: Thay đổi cấu trúc của một bảng hiện có, chẳng hạn như thêm, sửa, hoặc xóa cột

    DROP: Xóa một bảng, cơ sở dữ liệu, hoặc đối tượng khác khỏi cơ sở dữ liệu.

    TRUNCATE: Xóa tất cả các hàng trong một bảng mà không xóa bảng

2. DML - Data Manipulation Language – Ngôn ngữ thao tác dữ liệu

:

    SELECT: Truy vấn dữ liệu từ một hoặc nhiều bảng
    INSERT: Thêm một hoặc nhiều hàng mới vào bảng
    UPDATE: Cập nhật dữ liệu trong một bảng hiện có
    DELETE: Xóa dữ liệu khỏi một bảng

3. DCL – Data Control Language – Ngôn ngữ điều khiển dữ liệu

Được sử dụng để kiểm soát truy cập vào dữ liệu trong cơ sở dữ liệu

    GRANT: Cấp quyền cho người dùng hoặc vai trò. 
    REVOKE: Thu hồi quyền từ người dùng hoặc vai trò.

4. TCL - Transaction Control Language - Ngôn ngữ kiểm soát giao dịch     

Dược sử dụng để quản lý các giao dịch trong cơ sở dữ liệu

    COMMIT: Lưu các thay đổi của giao dịch hiện tại vào cơ sở dữ liệu.
    ROLLBACK: Hủy bỏ các thay đổi của giao dịch hiện tại.
    SAVEPOINT: Tạo điểm lưu trong một giao dịch để có thể rollback tới đó.
    RELEASE SAVEPOINT: Xóa điểm lưu.

ACID trong transaction

    Atomicity (nguyên tử)	Làm hết hoặc không làm gì	
    Consistency (nhất quán)	Dữ liệu luôn thỏa mọi luật (ràng buộc)
	Isolation (cô lập)	Các giao dịch chạy đồng thời không làm hỏng nhau	
	Durability (bền vững)	Đã COMMIT thì không mất


DESCRIBE: Hiển thị cấu trúc của một bảng

SHOW: Hiển thị danh sách các cơ sở dữ liệu, bảng, hoặc thông tin khác

### JOIN

cho phép kết hợp dữ liệu từ hai hoặc nhiều bảng khác nhau dựa theoo điều kiện cụ thể, trong cùng một cơ sở dữ liệu

Khóa chính là một hoặc nhiều cột trong một bảng, dùng để định danh duy nhất một hàng dữ liệu. Giá trị phải là duy nhất không được trùng lặp

Khóa ngoại là một hoặc nhiều cột trong bảng này nhưng lại trỏ đến Khóa chính của một bảng khác. Nó được sinh ra để tạo mối quan hệ giữa hai bảng với nhau.

INNER JOIN là một lệnh được sử dụng để kết hợp các hàng từ cả hai bảng thỏa mãn điều kiện cho trước. Sử dụng INNER JOIN sẽ trả về những hàng có giá trị khớp nhau trong cả hai bảng.Đây là loại JOIN được sử dụng phổ biến nhất và được coi là thao tác JOIN mặc định

LEFT JOIN trả về tất cả các hàng từ bảng bên trái (bảng A), cùng với các hàng tương ứng từ bảng bên phải (bảng B). Nếu không có hàng tương ứng trong bảng B, các cột từ bảng B sẽ chứa giá trị NULL.

RIGHT JOIN cơ chế tương tự nhưng ngược lại với left join

Full Join trả về tất cả các hàng từ cả hai bảng, và điền các giá trị NULL cho các hàng không có tương ứng trong bảng kia. Điều này có nghĩa là FULL JOIN có thể phát hiện và trả về các hàng mà không có kết quả khớp trong bảng được kết hợp.

CROSS JOIN là dạng JOIN đơn giản nhất trong SQL. Nó kết hợp mỗi hàng từ một bảng với tất cả các hàng từ bảng khác (lưu ý nhiều khi sử dụng, thường dùng để tạo ma trận)

LEFT JOIN EXCLUDE/ RIGHT JOIN EXCLUDE: Thực hiện LEFT JOIN/ RIGHT JOIN mà không muốn lấy phần INNER JOIN. Thực tế thì không có riêng loại JOIN này, có thể dễ dàng thực hiện nó bằng việc thêm điều kiện WHERE Key IS NULL để lọc bỏ những record chung.

FULL JOIN EXCLUDE: Thực hiện FULL JOIN và bỏ đi phần INNER JOIN, xử lý tương tự loại ở trên 

### INDEX 