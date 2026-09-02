from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
import bcrypt

from backend.database import get_db
from backend.models.user import User
from backend.schemas.user import UserCreate, UserResponse
from backend.schemas.auth import loginRequest


router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    hashed_password = bcrypt.hashpw(
    user.password.encode("utf-8"),
    bcrypt.gensalt()
    ).decode("utf-8")

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login (user:loginRequest, db:Session=Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user is None:
        raise HTTPException (status_code= 404, detail="User Not Found")
    if not bcrypt.checkpw(
        user.password.encode("utf-8"),
        existing_user.password.encode("utf-8")
    ):
        raise HTTPException (status_code=401, detail="Incorrect Password")
    return {'message':'Login Successful'}