from pydantic import BaseModel, constr

class EmailModel(BaseModel):
    sender: constr(min_length=1, max_length=255)
    recipients: constr(min_length=1)
    cc: str = ""
    bcc: str = ""
    subject: str = ""
    body: str = ""
    attachments: str = ""

class UserModel(BaseModel):
    username: constr(min_length=1, max_length=255)
    password: constr(min_length=1, max_length=255)

class RegisterModel(BaseModel):
    username: constr(min_length=1, max_length=255)
    password: constr(min_length=1, max_length=255)

class LoginModel(BaseModel):
    username: constr(min_length=1, max_length=255)
    password: constr(min_length=1, max_length=255)
