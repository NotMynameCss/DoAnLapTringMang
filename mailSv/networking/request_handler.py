from loguru import logger
import json
from typing import Any, Dict
from CONTROLLER.mainController import MainController
from networking.mail_detail_handler import MailDetailHandler
from MODEL.dbconnector import create_connection

class RequestHandler:
    """Xử lý các request từ client"""
    
    def __init__(self, main_controller: MainController):
        self.main_controller = main_controller
        self.session = create_connection()
        self.mail_detail_handler = MailDetailHandler(self.session)
        self.command_map = {
            'LOGIN': self._handle_login,
            'REGISTER': self._handle_register,
            'SEND_EMAIL': self._handle_send_email,
            'FETCH_EMAILS': self._handle_fetch_emails,
            'FETCH_EMAIL_DETAIL': self._handle_fetch_email_detail
        }

    def handle_request(self, client_socket: Any):
        """
        Xử lý request từ client socket

        Args:
            client_socket: Socket kết nối với client
        """
        while True:
            try:
                data = client_socket.recv(4096).decode('utf-8')
                if not data:
                    break
                    
                logger.info(f"Received request: {data}")
                response = self._process_request(data)
                client_socket.send(response.encode())
                
            except Exception as e:
                logger.error(f"Error handling request: {e}")
                break

    def _process_request(self, data: str) -> str:
        """Xử lý request và trả về response phù hợp"""
        try:
            command, *params = data.split()
            handler = self.command_map.get(command)
            
            if handler:
                return handler(*params)
            return "Unknown command"
            
        except Exception as e:
            logger.error(f"Error processing request: {e}")
            return f"Error: {str(e)}"

    def _handle_login(self, username: str, password: str) -> str:
        return self.main_controller.handle_login(username, password)

    def _handle_register(self, username: str, password: str) -> str:
        return self.main_controller.handle_register(username, password)

    def _handle_send_email(self, *params) -> str:
        return self.main_controller.handle_send_email(*params)

    def _handle_fetch_emails(self, username: str, folder: str) -> str:
        emails = self.main_controller.handle_fetch_emails(username, folder)
        return json.dumps(emails)

    def _handle_fetch_email_detail(self, email_id: str) -> str:
        """Xử lý yêu cầu lấy chi tiết email"""
        try:
            email_id = int(email_id)
            detail = self.mail_detail_handler.get_email_detail(email_id)
            if detail:
                return json.dumps(detail)
            return json.dumps({"error": "Email not found"})
        except ValueError:
            return json.dumps({"error": "Invalid email ID"})
        except Exception as e:
            logger.error(f"Lỗi xử lý yêu cầu chi tiết email: {e}")
            return json.dumps({"error": str(e)})
