from fastapi import FastAPI
from contextlib import asynccontextmanager
from utils.init import create_tables
from routes.userRoutes import authRouter
from routes.BillRoute import Billrouter
from routes.BillPartRoute import router as bill_participant_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Created")
    create_tables()
    yield
    print("App shutting down")

app = FastAPI(lifespan= lifespan)

app.include_router(bill_participant_router)
app.include_router(router=Billrouter,tags=["Bill"],prefix="/bill")
app.include_router(router= authRouter,tags=["auth"],prefix="/auth")

@app.get("/")
def read_root():
    return "Welcome to SplitAppBill"