from fastapi import FastAPI
from .routers import payment, users, transactions, bank_accounts, developer_project, deposit, saved_account, withdrawal

app = FastAPI()

app.include_router(users.router)
app.include_router(payment.router)
app.include_router(bank_accounts.router)
app.include_router(transactions.router)
app.include_router(deposit.router)
app.include_router(developer_project.router)
app.include_router(saved_account.router)
app.include_router(withdrawal.router)
