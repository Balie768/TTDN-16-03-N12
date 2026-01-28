# Quản Lý Khách Hàng

## 1. Giới thiệu

Dự án **Quản Lý Khách Hàng** cung cấp các chức năng chính nhằm hỗ trợ doanh nghiệp trong việc quản lý và chăm sóc khách hàng hiệu quả. Hệ thống giúp theo dõi thông tin khách hàng, hỗ trợ khách hàng, thống kê hiệu suất làm việc của nhân viên và bảng xếp hạng khách hàng mua hàng. Ngoài ra, người dùng còn có thể thêm sản phẩm và đơn hàng của khách hàng.

## 2. Hình ảnh minh họa 📸

### **1. Trang quản lý khách hàng**
![KH_ttin](images/KH_ttin.png)
![KH_ttin1](images/KH_ttin1.png)
> Giao diện quản lý thông tin khách hàng

### **2. Trang hỗ trợ khách hàng**
![KH_hotro](images/KH_hotro.png)
![KH_hotro1](images/KH_hotro1.png)
> Quản lý yêu cầu và phản hồi từ khách hàng

### **3. Trang thống kê hỗ trợ khách hàng**
![KH_tke](images/KH_tke.png)
![KH_tke1](images/KH_tke1.png)
> Biểu đồ thống kê hiệu suất hỗ trợ khách hàng của nhân viên

### **4. Trang quản lý email và gửi thông báo**
![KH_mail](images/KH_mail.png)
![KH_mail1](images/KH_mail1.png)
> Giao diện quản lý email và gửi thông báo đến khách hàng

### **5. Trang chi tiết đơn hàng**
![KH_DH](images/KH_DH.png)
![KH_DH1](images/KH_DH1.pn.jpg)
> Hiển thị thông tin chi tiết đơn hàng của khách hàng

### **6. Trang chi tiết sản phẩm**
![KH_SP](images/KH_SP.png)
![KH_SP1](images/KH_SP1.png)
> Thông tin sản phẩm chi tiết dành cho khách hàng

## 3. Chức năng chính

- **Xem thông tin khách hàng**  
- **Hỗ trợ khách hàng**  
- **Thống kê hỗ trợ của nhân viên**  
- **Bảng xếp hạng khách hàng mua hàng**  

### Chức năng phụ

- **Thêm sản phẩm**  
- **Thêm đơn hàng sản phẩm của khách hàng**  

# Hệ thống quản lý văn bản

Hệ thống được xây dựng dựa trên thông tư 30 về công tác văn thư. Hệ thống cho phép người dùng quản lý văn bản đi, quản lý văn bản đến. Các văn bản đến sẽ được xử lý thông qua moulde quản lý công việc.
Hệ thống xây dựng trên nền tảng odoo 15. 

Dưới đây là 1 số hình ảnh minh hoạ
### **1. Trang Văn bản đến
![VB_den](images/VB_den.png)
![VB_den1](images/VB_den1.png)
### **2. Trang Văn bản đi
![VB_di](images/VB_di.png)
![VB_di1](images/VB_di1.png)
### **3. Trang Quản lý công việc
![VB_CV](images/VB_CV.png)
![VB_CV1](images/VB_CV1.png)

6. Một số cấu hình kèm theo:

    Độ mật
   ![VB_domat](images/VB_domat.png)
    Trạng thái
   ![VB_TT](images/VB_TT.png)
    Loại văn bản
   ![VB_HS](images/VB_HS.png)
    Hồ sơ
   ![VB_HS](images/VB_HS.png)
    Năm
   ![VB_nam](images/VB_namt.png)


# QUẢN LÝ NHÂN SỰ

## Demo sản phẩm:

### **1. Trang  Nhân viên

![NS](images/NS.png)
![NS_1](images/NS_1.png)

### **2. Trang Chức vụ 
![NS_CV](images/NS_CV.png)
![NS_CV1](images/NS_CV1.png)

### **3. Trang chấm công

![NS_chamcong](images/NS_chamcong.png)
![NS_chamcong1](images/NS_chamcong1.png)

### **4. Trang Lịch sử công tác
![NS_LSCT](images/NS_LSCT.png)
![NS_LSCT1](images/NS_LSCT1.png)

### **5. Trang Lịch sử đào tạo
![NS_LSDT](images/NS_LSDT.png)
![NS_LSDT1](images/NS_LSDT1.png)

### **6. Trang Danh sách chứng chỉ, bằng 
![NS_CCBC](images/NS_CCBC.png)
![NS_CCBD1](images/NS_CCBD1.png)
    
##  Công nghệ sử dụng

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Odoo](https://img.shields.io/badge/Odoo-512677?style=for-the-badge&logo=odoo&logoColor=white)
![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

## Cài đặt môi trường

### 1. Clone dự án
```sh
git clone https://gitlab.com/Drabula/TTDN-15-04-N8.git
cd TTDN-15-04-N8
```

### 2. Cài đặt các thư viện cần thiết
Chạy lệnh sau để cài đặt các thư viện bắt buộc:
```sh
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev \
libssl-dev python3.10-distutils python3.10-dev build-essential libffi-dev \
zlib1g-dev python3.10-venv libpq-dev
```

### 3. Khởi tạo môi trường ảo
```sh
python3.10 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt
```

###  Cấu hình Database
Hệ thống sử dụng PostgreSQL chạy trên Docker. Để khởi tạo database, thực hiện:
```sh
sudo apt install docker-compose
sudo docker-compose up -d
```

##  Cấu hình hệ thống

### Tạo tệp `odoo.conf`
Tạo tệp `odoo.conf` với nội dung sau:
```ini
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5434
xmlrpc_port = 8069
```

##  Chạy hệ thống

Chạy lệnh sau để khởi động hệ thống:
```sh
python3 odoo-bin.py -c odoo.conf -u all
```
Sau khi chạy xong, truy cập [http://localhost:8069/](http://localhost:8069/) để đăng nhập vào hệ thống.

---
**Hoàn tất cài đặt!** 🚀
Nhóm 12 - CNTT16-03
