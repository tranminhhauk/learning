### Docker là phần mềm giúp đóng gói toàn bộ môi trường chạy của 1 ứng dụng vào 1 đơn vị là container, để chạy giống nhau ở mọi nơi

### Docker giải quyết việc khi set up và deploy  server từ việc phải cài đặt các công cụ, môi trường cần cho application đến việc chạy được ứng dụng xảy ra việc không đồng nhất giữa các môi trường trên nhiều server khác nhau.

### Docker cho phép tạo các môi trường độc lập và tách biệt để khởi chạy và phát triển ứng dụng và môi trường này được gọi là container. Khi cần deploy lên bất kỳ server nào chỉ cần run container của Docker

1. Docker container: Container là 1 process cô lập chạy từ image, chứa tất cả các thành phần cần thiết của một ứng dụng như mã nguồn, thư viện, và các công cụ, giúp đảm bảo ứng dụng có thể chạy đồng nhất trên mọi môi trường

Vòng đời của container

created → running → paused → stopped → removed

Container không phải là 1 máy ảo vì dùng chung nhân kernel với máy chủ nên nhẹ và khởi động nhanh hơn.

Khác biệt chính nằm ở cơ chế phân chia tài nguyên: Máy ảo ảo hóa ở phần cứng, mỗi máy ảo sẽ chạy 1 os riêng, docker ảo hóa ở os, khác biệt đó liên quan đến 2 tính chất cốt lõi của linux

Namespaces: Cô lập những gì container thấy (như tiến trình, mạng, thư mục) để nó nghĩ rằng nó đang chạy một mình.

cgroups (Control Groups): Giới hạn mức CPU và RAM tối đa mà container được phép dùng.

2. Docker image: là bản đóng gói chỉ đọc chứa ứng dụng và môi trường của nó, được build từ Dockerfile bao gồm nhiều layer xếp chồng.Image là khuôn mẫu để tạo container, Container là một thể hiện đang chạy của image, có thêm một lớp ghi riêng ở trên cùng. Từ một image có thể chạy nhiều container độc lập, giống như một class tạo ra nhiều object.

    đặc điểm của image: 

    immutable: image build xong thì không sửa được, muoons sửa được phải bulid image mới
    1 image có thể chạy được nhiều container
    Không chứa dữ liệu run time, dữ liệu khi sinh ra chạy nằm ở lớp ghi của container

Dockerfile --(docker build)--> Image --(docker run)--> Container

3. DockerFIle là 1 file văn bản chứa danh sách các lệnh mô tả cách xây dựng 1 image. Docker đọc file này từ trên xuống dưới, mỗi lệnh tạo ra 1 layer

4. Docker registry: Docker đóng gói ứng dụng thành các imgae, registry là nơi lưu trữ và cho phép tải các image từ nhiều nguồn: Docker Hub

## 2. Lệnh CLi cơ bản
 - image:

docker image pull (image)  : tải image từ registry

docker image push (image) : tải image từ máy local lên registry

docker images: liệt kê toàn bộ image đang có trong local

docker image prune: xóa các image không còn chạy nữa

- container:

docker container run name (image:tag): chạy 1 container

docker ps - docker ps -a: list container

docker container stop (container)

docker container prune

docker container exec (container) (command) : dùng để chạy 1 command trong 1 container

docker run alpine

docker exec -it image_id sh/bash: tạo tiến trình thứ cấp song song

docker logs -f <tên_hoặc_id_container>: xem log thời gian thực

ocker inspect <tên_hoặc_id_container_hoặc_image>: xem toàn bộ thông tin chi tiết

## Port Mapping

forward proxy: loc request tu local connect ra internet

reverse proxy: can bang tai

docker run -p target_port:container_port
### Volume

Volume là cơ chế lưu trữ dữ liệu độc lập với vòng đời container. 

image is immutable, Container is stateless -> volume đưa dữ liệu ra ngoài lớp ghi của container, giúp giữ liệu không bao giờ  mất khi container bị xóa 

phổ biến: 

    - Bind Mount Lấy một thư mục/file cụ thể từ máy thật đã tồn tại vào bên trong Container. Dùng khi lập trình giúp đồng bộ code tức thì sửa ở VS Code là container tự cập nhật

    - Named Volume: Vùng nhớ riêng độc lập, hoàn toàn do Docker tự quản lý.D ùng cho Database: Lưu trữ dữ liệu bền vững, không lo mất data khi xóa hay rebuild container, tối ưu hiệu năng đọc/ghi
docker volume create volume_name

docker run -v local_dir: container_dir

-Name Volume: docker run -d -p port_target:port_local -v <tên_volume>:<đường_dẫn_trong_container> --name container image

Hot reload: docker run -d -p port_target:port_local -v "%cd%:/app" --name container images: 

docker volume create library_data

docker volume ls/prune

docker volume rm library_data
### Docker Networking

Khi chạy ứng dụng nhiều lớp, các container cần giao tiếp với nhau. Khi các container nằm chung trong 1 mạng Compose (mặc định Compose tự tạo 1 mạng, bridge)

3 Loại Mạng chính:

    bridge (Mặc định): Mạng nội bộ cô lập. Các container cùng mạng giao tiếp qua Tên Container / Tên Service nhờ DNS nội bộ.

    host: Dùng chung card mạng với máy thật (không cần -p).

    none: Tắt hoàn toàn kết nối mạng (dùng cho tiến trình bảo mật cao).

Lệnh CLI quản lý Mạng:

    docker network ls: Danh sách các mạng.

    docker network create <tên_mạng>: Tạo mạng bridge mới.
### DockerFile

Docker File là template giúp xây dựng image riêng

FROM (image) chỉ định image gốc ban đầu tạo ra 1 image mới

RUN (command) chạy câu lệnh bên trong container

WORKDIR (directory): tạo 1 thư mục mặc định khi container chạy

COPPY (src) (dest) : coppy file từ máy local đi vào trong image

ADD

EXPOSE (port): thông báo port đang chạy 

CMD: thực thi khi container chạy 

    -COPY: chỉ copy file thư mục từ máy thật vào image

    -ADD: tương tự coppy nhưng có thêm tính năng tự giải nén file, hoặc tải file từ URL

    CMD: Lệnh mặc định khi container chạy, dễ bị ghi đè từ bên ngoài.

    ENTRYPOINT: Cố định lệnh thi hành chính của container, khó bị ghi đè.

FLOW:

Dockerfile (viết requirement, docker.ignore), -> image -> container (run bằng dettach, hot reload)

    Viết file requirements.txt bằng venv

    pip freeze > requirements.txt

    RUN pip install --no-cache-dir -r requirements.txt : cài đặt tất cả thư viện Python trong file requirements.txt và tự động dọn dẹp file tạm để giữ cho Docker Image nhẹ nhất có thể

    file .dockerignore : báo cho Docker biết những file/thư mục nào không copy vào image khi chạy lệnh COPY
            -> mẫu __pycache__/
                    *.py[cod]
                    .venv/
                    .git/
                    .env
                    *.log

### Docker Compose

là công cụ giúp định nghĩa và chạy các ứng dụng đa container (Multi-Container) thông qua một file cấu hình duy nhất đặt tên là docker-compose.yaml.

docker compose up -d

Lúc này Docker Compose sẽ tự động làm chuỗi công việc sau:

    - Tạo một mạng ảo bridge chung cho tất cả các service.
    - Pull các Image từ Docker Hub về nếu chưa có.
    - Build các Image từ Dockerfile nội bộ.
    - Khởi tạo các Volume lưu trữ.
    - Khởi chạy các Container dettach theo đúng thứ tự khai báo.

Quy trình làm việc với Docker Compose gồm:
1. Tạo Dockerfile, dockerignore: Định nghĩa môi trường cho từng thành phần.
2. Tạo file docker-compose.yml: Khai báo các dịch vụ (services), ports, volume và mạng.
3.  Dùng lệnh để khởi chạy toàn bộ ứng dụng

Các lệnh hay dùng: 

    - docker compose ps : list container
    - docker compose logs -f web: xem log real time
    - docker compose exec web sh : mở shell thứ cấp
    - docker compose up -d --build: để build lại image sau khi thay đổi dockerfile hoặc requirements.txt
    - docker compose down: dừng toàn hộ hệ thống ( thêm -v nếu muốn dừng và xóa toàn bộ DB/volume)

### Docker compose file (docker-compose.yaml)
mẫu cấu trúc: 

    version: '3.8'
    services:
        (container 1)                   vd: app python
        web:
            build: .                    (tự build image từ docker file)
            port: 
                - map Port_chạy: Port container
            volumes:
                - .:/app                (Bind mount - Hot reload)
            depends_on:
                - db                    (thiết lập thứ tự chạy vd database chạy trước web )
    services:
        (container 2)                      Database
        db: 
            image: todo
            environment:
                - todo
            volumees:
                -todo                      (Named volums lưu trữ dữ liệu DB)
    volumse:
        todo                              (named volumes dùng chung)

