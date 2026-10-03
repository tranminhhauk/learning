# Basic

## 1. What is the difference between a List and a LinkedList? When would you choose one over the other?

->> List là dữ liệu lưu trữ dưới dạng mảng động, truy xuất được trên index O(1), insert\delete chậm O(n) bởi vì sau khi thêm xóa phải sắp xếp lại các phần tử của toàn bộ mảng, có thể truy xuất ngẫu nhiên không duyệt toàn bộ mảng, list chỉ lưu data của nó nên yêu cầu ít bộ nhớ hơn

->> Linkedlist: Danh sách liên kết, các phần tử bên trong được gọi là các NODE, mỗi node phải lưu trữ 2 thông tin bao gồm Data và địa chỉ tham chiếu đến node tiếp theo. Insert\Dele nhanh hơn list vì không cần sắp xếp lại các phần tử mà chỉ cần tham chiếu tới phần tử sau đó O(1), Ngược lại Linkedlist không thể truy xuất ngẫu nhiên bằng index mà phải duyệt qua tất cả phần tử từ đầu tiên để tìm 

## 2. What is the difference between a Queue and a Stack?

->> Queue: FIFO, phần tử vào hàng đợi đầu tiên sẽ được lấy ra trước, bao gồm 2 đầu mở: thêm ở cuối và ra ở đầu

->> Stack: LIFO, vào sau ra trước, có 1 đầu mở để thực hiện thêm và lấy phần tử

## 3. What is LIFO vs FIFO? Give a real-world example of each.

ex: FIFOL: Xếp hàng mua vé xe buýt Người nào đến xếp hàng đầu tiên sẽ được mua vé và rời khỏi hàng đầu tiên. Người đến sau hải đứng ở sau và đợi tất cả những người phía trước mua xong thì mới đến lượt

LIFO: Giống như 1 cái tủ ngăn kéo gấp quần áo, chiếc áo cuối cùng để vào sẽ nằm trên cùng và khi lấy ra theo thứ tự thì chiếc áo trên cùng sẽ được lấy ra đầu tiên

## 4. . What is a Set? How does it differ from a List?
 
->> Set là cấu trúc dữ liệu bao gồm các phần tử không trùng lặp và không cố định, không thể truy xuất bằng index nhưng Set dùng Hash table nên việc truy xuất phần tử dựa trên value rất nhanh O(1), dùng {} để khai báo

## 5. What is the time complexity of searching in an array vs a HashMap?
- Time complexity dựa trên việc searching dựa trên index hay theo value

-Array: searching by index O(1)

-Hashmap tìm theo key - value O(n)

## 6. What is recursion? What are the risks of using it?

->> Đệ quy được định nghĩa là 1 func tự gọi lại chính nó -> dùng cơ chế chia nhỏ bài toán thành các bài toán con cùng loại: Đệ quy bao gồm đk dừng, và gọi lại chính nó với para nhỏ hơn

->> Rủi ro: Khó debug, tràn bộ nhớ, dễ sai, tốn bộ nhớ

Đệ quy thường được dùng trong Tree, vì không thể biểu diễn bằng vòng lặp, cốt lõi vẫn nên ưu tiên vòng lặp hơn

# Advanced

By java ->> TODO