from .abstruct import AbstractUserDatabaseNotify
from models.index import User
from config.index import get_db
from sqlalchemy.orm import Session
from schemas.index import UserOut, UserAuth
from services.jwt_token import create_access_token, verify_password, create_refresh_token, get_hashed_password

class UserRDBMS(AbstractUserDatabaseNotify):
    user = User

    def __init__(self):
        self.db: Session = next(get_db())

    def save(self, data: UserAuth) -> UserOut:
        user = User()
        user.email = data.email
        user.password = get_hashed_password(data.password)
        user.line_user_id = data.line_id
        user.picture_url = data.image_url
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
        return self.db.query(User).filter(User.line_user_id == line_id).first()