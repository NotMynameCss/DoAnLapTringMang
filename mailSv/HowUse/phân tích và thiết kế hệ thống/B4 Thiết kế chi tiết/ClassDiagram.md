# Bước 8: Vẽ chi tiết từng Class Diagram

## Tổng quan
Class Diagram là một phần quan trọng trong thiết kế hệ thống, giúp mô tả cấu trúc của hệ thống thông qua các lớp và mối quan hệ giữa chúng. Mục tiêu của bước này là vẽ chi tiết từng Class Diagram cho hệ thống mailServer.

## Class Diagram cho hệ thống mailServer

### 1. Class Diagram cho `User`
```plaintext
+-----------------+
|      User       |
+-----------------+
| - id: int       |
| - username: str |
| - password: str |
+-----------------+
| + __init__()    |
| + to_dict()     |
+-----------------+
```

### 2. Class Diagram cho `Email`
```plaintext
+-----------------+
|      Email      |
+-----------------+
| - id: int       |
| - sender: str   |
| - recipients: str|
| - cc: str       |
| - bcc: str      |
| - subject: str  |
| - body: str     |
| - attachments: str|
| - timestamp: datetime|
+-----------------+
| + __init__()    |
| + to_dict()     |
+-----------------+
```

### 3. Class Diagram cho `Label`
```plaintext
+-----------------+
|      Label      |
+-----------------+
| - id: int       |
| - name: str     |
| - user_id: int  |
+-----------------+
| + __init__()    |
| + to_dict()     |
+-----------------+
```

### 4. Class Diagram cho `EmailLabel`
```plaintext
+-----------------+
|   EmailLabel    |
+-----------------+
| - email_id: int |
| - label_id: int |
+-----------------+
| + __init__()    |
| + to_dict()     |
+-----------------+
```

### 5. Class Diagram cho `AuthController`
```plaintext
+---------------------------+
|      AuthController       |
+---------------------------+
| - view: View              |
+---------------------------+
| + __init__(view: View)    |
| + send_request(message: str) -> str|
| + login(username: str, password: str) -> str|
| + register(username: str, password: str) -> str|
+---------------------------+
```

### 6. Class Diagram cho `MailController`
```plaintext
+---------------------------+
|      MailController       |
+---------------------------+
| - view: View              |
+---------------------------+
| + __init__(view: View)    |
| + send_request(message: str) -> str|
| + send_email(sender: str, recipients: str, cc: str, bcc: str, subject: str, body: str, attachments: str) -> str|
| + fetch_emails(email_type: str) -> List[Email]|
| + fetch_all_emails() -> List[Email]|
| + fetch_all_users() -> List[User]|
| + fetch_emails_by_user(username: str) -> List[Email]|
| + refresh_emails() -> List[Email]|
+---------------------------+
```

### 7. Class Diagram cho `MainController`
```plaintext
+---------------------------+
|      MainController       |
+---------------------------+
| - view: View              |
+---------------------------+
| + __init__(view: View)    |
| + handle_login(username: str, password: str) -> str|
| + handle_register(username: str, password: str) -> str|
+---------------------------+
```

### 8. Class Diagram cho `View`
```plaintext
+---------------------------+
|           View            |
+---------------------------+
| - root: Tk                |
| - username: str           |
+---------------------------+
| + __init__(root: Tk, username: str)|
| + compose_email()         |
| + search_email()          |
| + show_inbox()            |
| + show_sent()             |
| + show_drafts()           |
| + show_trash()            |
| + show_labels()           |
| + show_settings()         |
| + show_chat()             |
| + show_users()            |
| + fetch_and_display_emails(email_type: str)|
| + refresh_emails()        |
| + get_selected_user() -> str|
| + set_controller(controller: Controller)|
| + on_user_select(event: Event)|
+---------------------------+
```

## Kết luận
Class Diagram giúp mô tả cấu trúc của hệ thống mailServer thông qua các lớp và mối quan hệ giữa chúng. Điều này giúp đảm bảo rằng hệ thống được thiết kế một cách hiệu quả và đáp ứng được các yêu cầu của người dùng.
