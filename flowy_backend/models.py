from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, ForeignKey, text, Double
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(
        Integer, index=True, autoincrement=True, primary_key=True, nullable=False
    )
    f_name = Column(String(50), nullable=False)
    l_name = Column(String(50), nullable=False)
    balance = Column(Double, nullable=False)
    flowy_account_number = Column(Integer, nullable=False)
    phone_number = Column(String(150), unique=True, nullable=False)
    password = Column(String(10), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
    
    
class UserBankAccounts(Base):
    __tablename__ = "user_bank_accounts"
    
    id = Column(Integer, index=True, autoincrement=True, primary_key=True, nullable=False)
    bank = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    account_number = Column(Integer, nullable=False)
    
    
class SavedAccounts(Base):
    __tablename__ = "saved_accounts"
    
    id = Column(Integer, index=True, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    account_number = Column(Integer, nullable=False)
    
    
class DeveloperProject(Base):
    __tablename__ = "project"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    website_link = Column(String(200), nullable=True)
    fee_on_customer = Column(Boolean, nullable=False, default=True)
    api_key = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)


class Transfer(Base):
    __tablename__ = "transfer"
    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    sender_id = None
    reciver_id = None
    amount = Column(Double, nullable=False)
    tx_ref = Column(String(20), nullable=False)
    fee = Column(Double, nullable=False)
    date = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )


class Payment(Base):
    __tablename__ = "payment"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    payer_id = Column(Integer, nullable=False)
    developer_id = Column(Integer, nullable=False)
    fee = Column(Double, nullable=False)
    date_time = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    amount = Column(Double, nullable=False)
    tx_ref = Column(String(20), nullable=False)


class Deposit(Base):
    __tablename__ = "deposite"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    user_id = Column(Integer, nullable=False)
    full_name = Column(String(50), nullable=False)
    account_number = Column(Integer, nullable=False)
    target_account = Column(Integer, nullable=False)
    date_time = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    amount = Column(Double, nullable=False)
    tx_ref = Column(String(20), nullable=False)
    status = Column(Boolean, nullable=False, default=False)


class Withdrawal(Base):
    __tablename__ = "withdrawal"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    user_id = Column(Integer, nullable=False)
    account_number = Column(Integer, nullable=False)
    bank_name = Column(String(50), nullable=False)
    date_time = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    amount = Column(Double, nullable=False)
    tx_ref = Column(String(20), nullable=False)
        
