### Process là một chương trình đang chạy, os quản lí bằng PCB (process control block), mỗi process chứa đầy đủ thông tin để 1 chương trình có thể hoạt động, có không gian địa chỉ riêng, hoạt động độc lập với process khác

### Thread là một phần thực thi bên trong 1 process, process có thể có nhiều thread, thread được sử dụng cho các nhiệm vụ nhỏ , các thread trong cùng 1 process có thể chia sẻ tài nguyên, dùng chung heap biến toàn cục

## Multithreading và Multiprocessing

Multi-thread: là một tổ hợp nhiều thread riêng lẻ với nhau
- Các luồng là độc lập -> thực hiện nhiều công việc cùng thúc
- Mỗi luồng có thể dùng chung và chia sẻ tài nguyên trong suốt quá trình chạy 
- Luồng là độc lập vậy nên không ảnh hưởng đến luồng khác nếu 1 luồng bị lỗi

Nhược điểm

- Càng nhiều luồng thì xử lý càng phức tạp.
- Xử lý vấn đề về tranh chấp bộ nhớ, đồng bộ dữ liệu 
Cần phát hiện tránh các luồng chết (dead lock), luồng chạy mà không làm gì trong ứng dụng cả.

Multiprocessing: là khả năng 1 hệ thống hỗ trợ nhiều bộ vi xử lý cùng lúc. Các ứng dụng trong hệ thống được chia thành nhiều quy trình nhỏ và chạy độc lập, os sẽ phân bổ các luồng cho core sử lí cải thiện hiệu suất của hệ thống
- Việc tạo đa tiến trình tốn nhiều thời gian, mooixi tiếng trinhgf sở hữu một không gian địa chỉ riêng biệt

## Concurrency và Parallelism

- Concurrency (đồng thời): nhiều tác vụ cùng đang tiến triển trong một khoảng thời gian, không nhất thiết chạy cùng một khoảnh khắc. Trên 1 nhân, hệ điều hành chuyển qua lại rất nhanh. Xen kẽ


- Parallelism (song song): nhiều tác vụ thực sự chạy cùng một lúc trên nhiều nhân. Cùng lúc

Hai loại tác vụ 

I/O-bound: chủ yếu chờ (mạng, đĩa, database). Dùng thread hoặc asyncio.

CPU-bound: chủ yếu tính toán (xử lý ảnh, mã hóa, số học). Cần nhiều process, vì dùng các tác vụ tính toán nặng CPU chạy liên tục không có thời gian chờ nên dùng multiprocess (hoặc thread thật sự song song)

## Race Condition (điều kiện tranh chấp)

là lỗi xảy ra trong hệ thống khi nhiều thread hoặc process cùng truy cập và thay đổi một dữ liệu dùng chung tại cùng một thời điểm, dẫn đến kết quả sai lệch do phụ thuộc vào thứ tự thực thi trước - sau, dẫn đến các kết quả không lường trước và ngoài ý muốn

-> giải pháp: dùng các phương pháp đồng bộ hóa như lock, để tại 1 thời điểm chỉ có 1 đối tượng được phép chỉnh sửa những biến gây xung đột

## Deadlock

Deadlock là tình trạng các thread/process chờ lẫn nhau vô hạn, mỗi bên giữ một tài nguyên và chờ tài nguyên do bên khác giữ, nên không ai tiến triển được.

Thread 1: lấy A rồi chờ B     |  Thread 2: lấy B rồi chờ A
    ex:  todo
-> giải pháp hiệu quả và đơn giản: 

- Quy ước mọi thread luôn lấy lock theo cùng một thứ tự (luôn A trước, rồi B). Khi đó không thể tạo vòng chờ.

- Dùng một lock duy nhất bảo vệ cả hai tài nguyên. Đơn giản, không deadlock, nhưng giảm song song.