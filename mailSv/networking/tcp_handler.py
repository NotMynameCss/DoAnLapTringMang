import socket
import threading
from loguru import logger
from typing import Callable, Any
from contextlib import contextmanager

class TCPHandler:
    """Xử lý kết nối TCP cho mail server"""
    
    def __init__(self, host: str = 'localhost', port: int = 65432, timeout: int = 60):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.server_socket = None
        self.is_running = False
        self._setup_logging()

    def _setup_logging(self):
        """Cấu hình logging chi tiết"""
        logger.add(
            "logs/network_{time}.log", 
            rotation="500 MB",
            retention="10 days",
            compression="zip",
            format="{time} | {level} | {message} | {extra}",
            backtrace=True,
            diagnose=True
        )

    @contextmanager
    def _socket_context(self):
        """Context manager để tự động đóng socket"""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.settimeout(self.timeout)
            yield self.server_socket
        finally:
            if self.server_socket:
                self.server_socket.close()

    def start(self, request_handler: Callable[[socket.socket, Any], None]):
        """
        Khởi động TCP server với handler được chỉ định
        
        Args:
            request_handler: Callback xử lý request từ client
        """
        try:
            with self._socket_context() as server:
                server.bind((self.host, self.port))
                server.listen(5)
                self.is_running = True
                logger.info(f"Server started on {self.host}:{self.port}")

                while self.is_running:
                    try:
                        client_socket, addr = server.accept()
                        client_socket.settimeout(self.timeout)
                        logger.info(f"New connection from {addr}")
                        
                        client_thread = threading.Thread(
                            target=self._handle_client,
                            args=(client_socket, addr, request_handler),
                            daemon=True
                        )
                        client_thread.start()
                        
                    except socket.timeout:
                        logger.warning("Socket accept timeout, continuing...")
                        continue
                    except Exception as e:
                        logger.error(f"Error accepting connection: {str(e)}")
                        continue

        except Exception as e:
            logger.error(f"Critical server error: {str(e)}")
            raise

    def _handle_client(self, 
                      client_socket: socket.socket,
                      addr: tuple,
                      handler: Callable):
        """Xử lý kết nối client trong thread riêng"""
        try:
            with logger.contextualize(client=addr):
                with self._client_socket_context(client_socket):
                    handler(client_socket)
        except socket.timeout:
            logger.warning(f"Client {addr} connection timeout")
        except ConnectionResetError:
            logger.warning(f"Client {addr} connection reset")
        except Exception as e:
            logger.error(f"Error handling client {addr}: {str(e)}")

    @contextmanager
    def _client_socket_context(self, client_socket):
        """Context manager for client sockets"""
        try:
            yield client_socket
        finally:
            try:
                client_socket.close()
            except:
                pass

    def stop(self):
        """Dừng TCP server an toàn"""
        self.is_running = False
        if self.server_socket:
            try:
                self.server_socket.shutdown(socket.SHUT_RDWR)
            except:
                pass
            finally:
                self.server_socket.close()
                logger.info("Server stopped")
