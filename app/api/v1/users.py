from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app.schemas.user import UserOut,UserCreate
from app.services.user_service import UserService

router = APIRouter(prefix='/users',tags=['users'])

@router.post('/',response_model=UserOut,status_code=status.HTTP_201_CREATED)
async def register_user(data:UserCreate,db: AsyncSession =  Depends(get_db)):
    # you might want to check for duplicate email here
    return await UserService.create(db,data)

@router.get("/",response_model=List[UserOut])
async def list_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await UserService.list(db,skip,limit)

@router.get('/{user_id}',response_model=UserOut)
async def get_user(user_id: int, db: AsyncSession =  Depends(get_db)):
    user = await UserService.get(db,user_id)
    if not user:
        raise HTTPException(status_code=404,detail='User not found')
    return user