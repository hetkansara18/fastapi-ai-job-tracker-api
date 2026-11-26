from typing import Annotated
from app.schemas.user import UserCreate, UserOut
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter, status
from app.db.session import get_db
from fastapi.concurrency import run_in_threadpool
from app.core.security import hash_password
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(user_in: UserCreate, db: Annotated[AsyncSession, Depends(get_db)]):
    hashed = await run_in_threadpool(hash_password, user_in.password)
    user = User(email=user_in.email, hashed_password=hashed, full_name=user_in.full_name)

    #staging before commiting to the "Users" table
    db.add(user)

    #saving/commiting to the "Users" table
    await db.commit()

    #refreshing the updated "Users" table
    await db.refresh(user)

    return user