# Sơ đồ liên kết giữa các file trong thư mục `mailSv`

```plaintext
mailSv/
├── CONTROLLER/
│   ├── authController.py
│   ├── fetchMailController.py
│   ├── mailController.py
│   ├── mainController.py
│   ├── searchMailController.py
│   ├── sendMailController.py
│   └── userController.py
├── MODEL/
│   ├── dbconnector.py
│   ├── models.py
│   └── ...
├── VIEW/
│   ├── authView.py
│   ├── mainView.py
│   ├── mailView.py
│   └── subView/
│       └── subMailView/
│           ├── leftFrame.py
│           ├── rightFrame.py
│           └── topFrame.py
├── server.py
├── main.py
└── HowUse/
    ├── API_Documentation.md
    ├── Deployment_Guide.md
    ├── Coder Manual/
    │   ├── HowUseController/
    │   │   ├── HowUseControllerOverView.md
    │   │   ├── HowUseauthController.md
    │   │   ├── HowUsemailController.md
    │   │   └── ...
    │   ├── HowUseDatabase/
    │   │   └── HowUseDatabase.md
    │   ├── HowUseview/
    │   │   ├── HowUseViewOverview.md
    │   │   ├── HowUseViewMailView.md
    │   │   └── ...
    └── file_structure_diagram.md
```

## Mô tả liên kết giữa các file

### CONTROLLER
- **authController.py**: Quản lý xác thực người dùng, bao gồm đăng nhập và đăng ký.
- **fetchMailController.py**: Quản lý các chức năng liên quan đến truy xuất email.
- **mailController.py**: Quản lý các hoạt động liên quan đến email như gửi email, truy xuất email và người dùng. Sử dụng `fetchMailController.py`, `sendMailController.py`, và `searchMailController.py`.
- **mainController.py**: Xử lý các yêu cầu đăng nhập và đăng ký từ người dùng. Sử dụng `authController.py`.
- **searchMailController.py**: Quản lý các chức năng liên quan đến tìm kiếm email.
- **sendMailController.py**: Quản lý các chức năng liên quan đến gửi email.
- **userController.py**: Quản lý các chức năng liên quan đến người dùng.

### MODEL
- **dbconnector.py**: Kết nối đến cơ sở dữ liệu MySQL và tạo bảng nếu chưa tồn tại.
- **models.py**: Định nghĩa các mô hình dữ liệu sử dụng trong ứng dụng.

### VIEW
- **authView.py**: Quản lý giao diện đăng nhập và đăng ký người dùng.
- **mainView.py**: Khởi tạo giao diện chính của ứng dụng, bao gồm việc hiển thị giao diện đăng nhập.
- **mailView.py**: Quản lý giao diện chính sau khi đăng nhập thành công.
- **subView/subMailView**: Chứa các khung giao diện con của `mailView.py`.
  - **leftFrame.py**: Khung bên trái chứa các nút điều hướng.
  - **rightFrame.py**: Khung bên phải hiển thị danh sách người dùng và chi tiết người dùng.
  - **topFrame.py**: Khung trên cùng chứa thanh tìm kiếm và nút soạn thư mới.

### Khác
- **server.py**: Cấu hình máy chủ để lắng nghe các kết nối từ máy khách và xử lý các yêu cầu.
- **main.py**: Điểm khởi đầu của ứng dụng, khởi tạo `MainController` và `MailController`, và bắt đầu máy chủ.
- **HowUse**: Chứa các tài liệu hướng dẫn sử dụng và triển khai hệ thống.
  - **API_Documentation.md**: Tài liệu chi tiết về các API được sử dụng trong hệ thống.
  - **Deployment_Guide.md**: Hướng dẫn triển khai hệ thống mailServer.
  - **Coder Manual**: Chứa các tài liệu hướng dẫn sử dụng cho các thành phần khác nhau của hệ thống.
    - **HowUseController**: Hướng dẫn sử dụng các controller.
    - **HowUseDatabase**: Hướng dẫn sử dụng cơ sở dữ liệu.
    - **HowUseview**: Hướng dẫn sử dụng các view.
  - **file_structure_diagram.md**: Sơ đồ liên kết giữa các file trong thư mục `mailSv`.
