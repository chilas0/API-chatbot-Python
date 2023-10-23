from fastapi import FastAPI 
import uvicorn 
from app.routers import chat
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
app.include_router(chat.router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000,reload=True)

