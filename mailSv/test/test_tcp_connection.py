import socket
import unittest
from network_config import SERVER_HOST, SERVER_PORT

class TestTCPConnection(unittest.TestCase):
    def test_tcp_connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            s.connect((SERVER_HOST, SERVER_PORT))
            s.sendall(b"PING")
            # Không cần nhận phản hồi, chỉ test kết nối
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"TCP connection failed: {e}")
        finally:
            s.close()

if __name__ == "__main__":
    unittest.main()
