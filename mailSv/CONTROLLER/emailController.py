from sqlalchemy.exc import SQLAlchemyError
from MODEL.dbconnector import create_connection, Email
from loguru import logger

class EmailController:
    def __init__(self):
        self.session = create_connection()

    def fetch_emails(self, user_id):
        if self.session is None:
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
        if self.session is None:
            return {}
        try:
            email = self.session.query(Email).filter_by(id=email_id).first()
            if email:
                email_details = email.to_dict()
                logger.info(f"Truy xuất chi tiết email thành công: {email_details}")
                return email_details
            else:
                logger.error(f"Không tìm thấy email với ID: {email_id}")
                return {}
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi truy xuất chi tiết email: {e}")
            return {}
