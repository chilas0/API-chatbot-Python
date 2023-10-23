from fastapi import APIRouter 
from app.schemas import Message
from app.nlp.nltk_utils import tokenize
from chat_ import get_response



router = APIRouter(
    prefix="/send",
    tags=["Send"]
)

@router.post('/')
def send(message:Message):
    message = message.message
    return get_response(message)