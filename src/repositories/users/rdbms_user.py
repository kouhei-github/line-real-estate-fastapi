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

    def save(self, data: UserAuth, company: Company) -> UserOut:
        user = User(name=data.name, line_user_id=data.line_id, picture_url=data.image_url)

        user.companies.append(company)
        self.db.add(user)
        self.db.commit()
        response = UserOut(
            email=user.email,
            name=user.name,
            id=user.id,
            access_token=create_access_token(user.id),
            refresh_token=create_refresh_token(user.id),
            token_type="bearer"
        )
        self.db.refresh(user)
        return response

    def find_by_line_id(self, line_id: str) -> User:
        record = self.db.query(User).filter(User.line_user_id == line_id).first()
        self.db.close()
        return record