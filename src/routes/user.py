from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.index import get_db
from schemas.index import UserOut, UserAuth, ShowUserSchema, TokenDataSchema
from models.index import User
from services.jwt_token import create_access_token, verify_password, create_refresh_token, get_hashed_password
from midlewares.index import get_current_bearer_token

user = APIRouter(
    prefix="/api/user",
    tags=["Users"]
)

@user.get("/", response_model= List[ShowUserSchema])
async def read_all_users(
    db: Session = Depends(get_db),
    get_bearer_token: TokenDataSchema = Depends(get_current_bearer_token)
):
    """データベースから全てのユーザーを読み込む

    Args:
        db (Session):  使用するデータベースセッション

    Returns:
        List[ShowUserSchema]: 全ユーザのリスト

    Raises:
        HTTPException: データベースからユーザーを取得する際にエラーが発生した場合

    """
    user = db.query(User).filter(User.id == get_bearer_token.id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
            detail=f'Authorization is required'
        )

    users = db.query(User).all()
    return users


@user.get("/{id}", response_model=ShowUserSchema)
async def show_user(
    id: int,
    db: Session = Depends(get_db),
    get_bearer_token: TokenDataSchema = Depends(get_current_bearer_token)
):
    """
    ユーザーを表示

    データベースから特定のユーザーを取得する

    Args:
        id (int):  取得するユーザーのID
        db (Session): データベースセッション
        get_bearer_token (TokenDataSchema): The current bearer token.

    Returns:
        ShowUserSchema: 取得したユーザー

    Raises:
        HTTPException:  指定した ID のユーザがデータベースに存在しない場合
    """
    user = db.query(User).filter(User.id == get_bearer_token.id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED,
            detail=f'Authorization is required'
        )

    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with the id {id} is not available'
        )
    return user


@user.post('/signup', status_code=status.HTTP_201_CREATED, summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth, db: Session = Depends(get_db)):
    # querying database to check if user already exist
    user = db.query(User).filter(User.email == data.email).first()
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = User()
    user.email = data.email
    user.password = get_hashed_password(data.password)
    db.add(user)
    db.commit()
    response = UserOut(
        email=user.email,
        name=user.name,
        id=user.id,
        access_token=create_access_token(user.id),
        refresh_token=create_refresh_token(user.id),
        token_type="bearer"
    )
    db.refresh(user)
    return response