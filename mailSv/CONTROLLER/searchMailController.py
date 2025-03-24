# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.exc import SQLAlchemyError
from MODEL.dbconnector import create_connection, Email
from utils.logger import get_logger

logger = get_logger()

class SearchMailController:
    def __init__(self):
        self.session = create_connection()
        if self.session is None:
            logger.error("Failed to create database connection")

    def search_emails(self, query):
        if self.session is None:
            return "Lỗi kết nối đến database"
        try:
            emails = self.session.query(Email).filter(
                (Email.subject.like(f"%{query}%")) |
                (Email.body.like(f"%{query}%"))
            ).all()
            logger.info(f"Truy xuất {len(emails)} email với từ khóa {query}")
            return emails
        except SQLAlchemyError as e:
            logger.error(f"Lỗi khi tìm kiếm email: {e}")
            return f"Lỗi khi tìm kiếm email: {e}"
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return f"Unexpected error: {e}"
