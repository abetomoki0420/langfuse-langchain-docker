from typing import List
from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    chat_history: List[Message]
    user_input: str


class ChatResponse(BaseModel):
    response: str 