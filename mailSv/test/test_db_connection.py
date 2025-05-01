import unittest
from MODEL.dbconnector import DBConnection, User

class TestDBConnection(unittest.TestCase):
    def test_db_session(self):
        with DBConnection() as session:
            users = session.query(User).all()
            self.assertIsInstance(users, list)

if __name__ == "__main__":
    unittest.main()
