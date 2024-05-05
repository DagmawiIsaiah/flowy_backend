from pydantic import BaseModel
from typing import Optional
import datetime


class User(BaseModel):
    id: Optional[str] = None  
    f_name: str
    l_name: str
    balance: float
    flowy_account_number: int
    phone_number: int
    password: str
    date_time: datetime.datetime
    
    class Config:
        from_attributes = True
        
         
class UserBankAccounts(BaseModel):
    id: Optional[str] = None  
    bank: str
    full_name: str
    account_number: int
    
    class Config:
        from_attributes = True
        
        
class SavedAccounts(BaseModel):
    id: Optional[str] = None  
    name: str
    account_number: int
    
    class Config:
        from_attributes = True
        
        
class DeveloperProject(BaseModel):
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
    amount: float
    fee: float
    tx_ref: str
    date_time: datetime.datetime
    
    class Config:
        from_attributes = True
        
        
class Deposit(BaseModel):
    id: Optional[str] = None  
    user_id: int
    full_name: str
    account_number: int
    target_account_number: int
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
        
