from sqlalchemy.exc import SQLAlchemyError
from MODEL.dbconnector import create_connection, Email
from loguru import logger
from pydantic import BaseModel, ValidationError

class EmailCreateModel(BaseModel):
    sender: str
    recipients: str
    cc: str = ""
    bcc: str = ""
    subject: str = ""
    body: str = ""
    attachments: str = ""

class EmailController:
    """
    Controller quản lý các thao tác liên quan đến email.
    """

    def __init__(self):
        self.session = create_connection()

    def fetch_emails(self, user_id):
        """
        Truy xuất danh sách email của người dùng.

        Args:
            user_id (str): ID của người dùng.

        Returns:
            list: Danh sách email dưới dạng dictionary.
        """
        if self.session is None:
            logger.error("Không thể kết nối đến cơ sở dữ liệu")
            return []
        try:
            emails = self.session.query(Email).filter_by(sender=user_id).all()
            email_list = [email.to_dict() for email in emails]
            logger.info(f"Truy xuất email thành công cho người dùng {user_id}: {email_list}")
            return email_list
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất email: {e}")
            return []

    def fetch_email_details(self, email_id):
        """
        Truy xuất chi tiết email.

        Args:
            email_id (int): ID của email.

        Returns:
            dict: Chi tiết email dưới dạng dictionary.
        """
        if self.session is None:
            logger.error("Không thể kết nối đến cơ sở dữ liệu")
            return {}
        try:
            email = self.session.query(Email).filter_by(id=email_id).first()
            if email:
                email_details = email.to_dict()
                logger.info(f"Truy xuất chi tiết email thành công: {email_details}")
                return email_details
            else:
                logger.warning(f"Không tìm thấy email với ID: {email_id}")
                return {}
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất chi tiết email: {e}")
            return {}

    def create_email(self, email_data):
        """
        Tạo email mới trong cơ sở dữ liệu.

        Args:
            email_data (dict): Dữ liệu email cần tạo.

        Returns:
            dict: Email đã được tạo dưới dạng dictionary.
        """
        if self.session is None:
            logger.error("Không thể kết nối đến cơ sở dữ liệu")
            return {}
        try:
            # Validate dữ liệu bằng Pydantic
            email_data = EmailCreateModel(**email_data)
            email = Email(**email_data.dict())
            self.session.add(email)
            self.session.commit()
            logger.info(f"Tạo email thành công: {email.to_dict()}")
            return email.to_dict()
        except ValidationError as e:
            logger.error(f"Lỗi xác thực dữ liệu email: {e}")
            return {"error": str(e)}
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi tạo email: {e}")
            self.session.rollback()
            return {"error": str(e)}

    def delete_email(self, email_id: int, user_id: str) -> dict:
        """
        Xóa email của user được chỉ định.

        Args:
            email_id (int): ID của email cần xóa.
            user_id (str): ID của người dùng sở hữu email.

        Returns:
            dict: Kết quả xóa email.
        """
        if self.session is None:
            logger.error("Không thể kết nối đến cơ sở dữ liệu")
            return {"success": False, "message": "Lỗi kết nối đến cơ sở dữ liệu"}

        try:
            # Kiểm tra email tồn tại và thuộc về user
            email = self.session.query(Email).filter(
                Email.id == email_id,
                Email.sender == user_id
            ).first()

            if not email:
                logger.warning(f"Không tìm thấy email ID {email_id} của user {user_id}")
                return {"success": False, "message": "Email không tồn tại hoặc bạn không có quyền xóa"}

            # Xóa email
            self.session.delete(email)
            self.session.commit()
            logger.info(f"Đã xóa email ID {email_id} của user {user_id}")
            return {"success": True, "message": "Xóa email thành công"}

        except SQLAlchemyError as e:
            self.session.rollback()
            logger.error(f"Lỗi khi xóa email: {e}")
            return {"success": False, "message": f"Lỗi cơ sở dữ liệu: {str(e)}"}
