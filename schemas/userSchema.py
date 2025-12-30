from pydantic import EmailStr,BaseModel
from typing import Union,Literal

class UserCreate(BaseModel):

    username:str
    email:EmailStr
    hashed_password:str

class UserOutput(BaseModel):
    id:int
    username:str
    email:EmailStr

class UserInLogin(BaseModel):
    email:EmailStr
    hashed_password:str

class UserWithToken(BaseModel):
    token:str
    token_type: Literal["bearer"] = "bearer"