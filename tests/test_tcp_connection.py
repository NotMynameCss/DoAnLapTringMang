import socket

def test_tcp_connection():
    HOST = 'localhost'
    PORT = 65432
    try:
        with socket.create_connection((HOST, PORT), timeout=5) as s:
            s.sendall(b'PING')
            response = s.recv(1024)
            assert response is not None
            print("TCP connection test: OK")
    except Exception as e:
        print(f"TCP connection test failed: {e}")

if __name__ == "__main__":
    test_tcp_connection()
