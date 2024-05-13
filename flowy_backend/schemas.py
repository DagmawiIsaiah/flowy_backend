from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime


class Login(BaseModel):
    phone_number: str
    password: str
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class UserBase(BaseModel):
    f_name: str
    l_name: str
    email: EmailStr
    phone_number: str
    
    class Config:
        from_attributes = True
        
        
class User(UserBase):
    id: str
    balance: Optional[float] = None
    flowy_account_number: Optional[int] = None
    password: str
    created_at: datetime.datetime
    
    class Config:
        from_attributes = True
        
        
class UserResponse(BaseModel):
    f_name: str
    l_name: str
    balance: float
    flowy_account_number: int
    
    class Config:
        from_attributes = True
        
         
class BankAccounts(BaseModel):
    id: Optional[str] = None  
    bank: str
    full_name: str
    account_number: int
    
    class Config:
        from_attributes = True
        
        
class Bank(BaseModel):
    id: Optional[str] = None  
    name: str
    
    class Config:
        from_attributes = True
        
        
class Project(BaseModel):
    id: Optional[str] = None  
    name: str
    description: str
    website_link: str
    fee_on_customer: bool
    api_key: str
    user_id: int
    status: bool
    date_time: datetime.datetime
    
    class Config:
        from_attributes = True
   
   
class Transfer(BaseModel):
    id: Optional[str] = None  
    sender_id: int
    reciver_id: int
    amount: float
    fee: float
    tx_ref: str
    date_time: datetime.datetime
    
    class Config:
        from_attributes = True
                

class Payment(BaseModel):
    id: Optional[str] = None  
    payer_id: int
    developer_id: int
    fee: float
    amount: float
    tx_ref: str
    status: Optional[bool] = None
    date_time: datetime.datetime
    
    class Config:
        from_attributes = True
        
        
class Deposit(BaseModel):
    id: Optional[str] = None  
    user_id: Optional[int] = None
    full_name: str
    account_number: int
    target_account: int
    amount: float
    tx_ref: str
    status: bool
    date_time: datetime.datetime
    
    class Config:
        from_attributes = True
        
        
class Withdrawal(BaseModel):
    id: Optional[str] = None
    user_id: int
    account_number: int
    bank_name: str
    amount: float
    tx_ref: str
    date_time: datetime.datetime
    
    class Config:
        from_attributes = True
        
