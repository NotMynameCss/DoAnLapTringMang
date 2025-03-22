from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger
from pydantic import ValidationError
from MODEL.models import EmailModel, UserModel  # Import EmailModel and UserModel from models.py

Base = declarative_base()

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sender = Column(String(255), nullable=False)
    recipients = Column(Text, nullable=False)
    cc = Column(Text)
    bcc = Column(Text)
    subject = Column(String(255))
    body = Column(Text)
    attachments = Column(Text)
    timestamp = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    def to_dict(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'recipients': self.recipients,
            'cc': self.cc,
            'bcc': self.bcc,
            'subject': self.subject,
            'body': self.body,
            'attachments': self.attachments,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

def create_connection():
    try:
        engine = create_engine('mysql+mysqlconnector://root:@localhost/mail_server_db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        logger.info("Kết nối thành công đến database")
        return Session()
    except Exception as e:
        logger.error(f"Lỗi kết nối đến database: {e}")
        return None
