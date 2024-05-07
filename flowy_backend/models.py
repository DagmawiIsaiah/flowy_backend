from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, ForeignKey, text, Double
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer, index=True, autoincrement=True, primary_key=True, nullable=False
    )
    f_name = Column(String(50), nullable=False)
    l_name = Column(String(50), nullable=False)
    balance = Column(Double, nullable=True)
    flowy_account_number = Column(Integer, nullable=True)
    email = Column(String(200), unique=True, nullable=True)
    phone_number = Column(String(10), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )
    
    
class BankAccounts(Base):
    __tablename__ = "bank_accounts"
    
    id = Column(Integer, index=True, autoincrement=True, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    bank = Column(String(50), nullable=False)
    full_name = Column(String(100), nullable=False)
    account_number = Column(Integer, nullable=False)
    
    
class Accounts(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, index=True, autoincrement=True, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    account_number = Column(Integer, nullable=False)
    
    
class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    website_link = Column(String(200), nullable=True)
    fee_on_customer = Column(Boolean, nullable=False, default=True)
    api_key = Column(String(20), nullable=False)
    user_id = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)


class Transfer(Base):
    __tablename__ = "transfers"
    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    sender_id = Column(Integer, nullable=False)
    reciver_id = Column(Integer, nullable=False)
    amount = Column(Double, nullable=False)
    tx_ref = Column(String(20), nullable=False)
    fee = Column(Double, nullable=False)
    date = Column(
        TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False
    )


class Payment(Base):
    __tablename__ = "payments"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    payer_id = Column(Integer, nullable=False)
    developer_id = Column(Integer, nullable=False)
    amount = Column(Double, nullable=False)
    fee = Column(Double, nullable=False)
    tx_ref = Column(String(20), nullable=False)
    status = Column(Boolean, nullable=True)
    date_time = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)


class Deposit(Base):
    __tablename__ = "deposits"

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
    __tablename__ = "withdrawals"

    id = Column(
        Integer, primary_key=True, index=True, autoincrement=True, nullable=False
    )
    user_id = Column(Integer, nullable=False)
    account_number = Column(Integer, nullable=False)
    bank_name = Column(String(50), nullable=False)
    date_time = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)
    amount = Column(Double, nullable=False)
    tx_ref = Column(String(20), nullable=False)
        
