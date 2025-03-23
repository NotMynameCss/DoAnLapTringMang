from sqlalchemy.exc import SQLAlchemyError
from MODEL.dbconnector import create_connection, User
from loguru import logger
from pydantic import ValidationError
from MODEL.models import UserModel, LoginModel  # Import LoginModel from models.py

class AuthController:
    def __init__(self, view):
        self.view = view
        if self.view is not None:
            self.view.set_controller(self)
        self.session = create_connection()

    def login(self, username, password):
        try:
            user_data = LoginModel(username=username, password=password)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

        if self.session is None:
            return "Lỗi kết nối đến database"
        try:
            user = self.session.query(User).filter_by(username=user_data.username, password=user_data.password).first()
            if user:
                logger.info(f"Đăng nhập thành công cho người dùng: {username}")
                return "Đăng nhập thành công"
            else:
                return "Tên người dùng hoặc mật khẩu không hợp lệ"
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi đăng nhập: {e}")
            return f"Lỗi khi đăng nhập: {e}"

    def register(self, username, password):
        try:
            user_data = UserModel(username=username, password=password)
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu: {e}")
            return f"Lỗi xác thực dữ liệu: {e}"

        if self.session is None:
            return "Lỗi kết nối đến database"
        try:
            user = self.session.query(User).filter_by(username=user_data.username).first()
            if user:
                return "Tên người dùng đã tồn tại"
            new_user = User(username=user_data.username, password=user_data.password)
            self.session.add(new_user)
            self.session.commit()
            logger.info(f"Đăng ký thành công cho người dùng: {username}")
            return "Đăng ký thành công"
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi đăng ký: {e}")
            return f"Lỗi khi đăng ký: {e}"