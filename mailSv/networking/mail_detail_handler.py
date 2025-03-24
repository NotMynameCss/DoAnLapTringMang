from loguru import logger
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from MODEL.dbconnector import Email

class MailDetailHandler:
    """Xử lý chi tiết email cho mail server"""
    
    def __init__(self, session: Session):
        self.session = session
        
    def get_email_detail(self, email_id: int) -> Optional[Dict[str, Any]]:
        """
        Lấy chi tiết của một email từ database
        
        Args:
            email_id: ID của email cần lấy chi tiết
            
        Returns:
            Dict chứa chi tiết email hoặc None nếu không tìm thấy
        """
        try:
            # Validate email_id
            if not isinstance(email_id, int) or email_id <= 0:
                logger.error(f"Invalid email ID: {email_id}")
                return None
                
            email = self.session.query(Email).filter_by(id=email_id).first()
            if not email:
                logger.warning(f"Không tìm thấy email với ID: {email_id}")
                return None
                
            detail = {
                'id': email.id,
                'sender': email.sender,
                'recipients': email.recipients,
                'cc': email.cc,
                'bcc': email.bcc,
                'subject': email.subject,
                'body': email.body,
                'attachments': email.attachments,
                'timestamp': email.timestamp.isoformat() if email.timestamp else None
            }
            
            logger.info(f"Đã lấy chi tiết email {email_id} thành công")
            return detail
            
        except Exception as e:
            logger.error(f"Lỗi khi lấy chi tiết email {email_id}: {e}")
            return None
