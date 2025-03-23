from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, Index, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from loguru import logger

Base = declarative_base()

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sender = Column(String(255), nullable=False, index=True)
    recipients = Column(Text, nullable=False)
    cc = Column(Text)
    bcc = Column(Text)
    subject = Column(String(255))
    body = Column(Text)
    attachments = Column(Text)
    timestamp = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', index=True)

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
    username = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)

class Label(Base):
    __tablename__ = 'labels'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='labels')

class EmailLabel(Base):
    __tablename__ = 'email_labels'
    email_id = Column(Integer, ForeignKey('emails.id'), primary_key=True)
    label_id = Column(Integer, ForeignKey('labels.id'), primary_key=True)

User.labels = relationship('Label', order_by=Label.id, back_populates='user')

# Create indexes for optimization
Index('ix_email_sender', Email.sender)
Index('ix_email_timestamp', Email.timestamp)
Index('ix_user_username', User.username)

class DatabaseConnector:
    _instance = None
    _session = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
            cls._instance._create_connection()
        return cls._instance

    def _create_connection(self):
        try:
            engine = create_engine('mysql+mysqlconnector://root:@localhost/mail_server_db', echo=True)  # Enable echo to log SQL statements
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            self._session = Session()
            logger.info("Kết nối thành công đến database")
        except Exception as e:
            logger.error(f"Lỗi kết nối đến database: {e}")
            self._session = None

    def get_session(self):
        return self._session

def create_connection():
    db_connector = DatabaseConnector()
    return db_connector.get_session()
