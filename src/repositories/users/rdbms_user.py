from .abstruct import AbstractUserDatabaseNotify
from models.index import User, Company
from config.index import get_db
from sqlalchemy.orm import Session
from schemas.index import UserOut, UserAuth
from services.jwt_token import create_access_token, verify_password, create_refresh_token, get_hashed_password

class UserCompanyRDBMS(AbstractUserDatabaseNotify):
    user = User

    def __init__(self):
        self.db: Session = next(get_db())

    def save(self, data: UserAuth, company_id: int) -> User:
        user = User(name=data.name, line_user_id=data.line_id, picture_url=data.image_url)
        company = self.db.query(Company).get(company_id)
        user.companies.append(company)
        self.db.add(user)
        self.db.commit()

        self.db.refresh(user)
        return user

    def find_by_line_id(self, line_id: str) -> User:
        record = self.db.query(User).filter(User.line_user_id == line_id).first()
        self.db.close()
        return record