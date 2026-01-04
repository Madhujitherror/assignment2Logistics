from fastapi import FastAPI
from routes.support import router

app = FastAPI(title="Logistics AI Support Agent")

app.include_router(router, prefix="/api/support")
