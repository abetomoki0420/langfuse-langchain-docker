import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from langfuse import Langfuse
from langserve import add_routes

from .chat.schema import ChatRequest, ChatResponse
from .chat.chain import create_chat_chain, convert_to_langchain_messages


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Langfuseの初期化
    app.state.langfuse = Langfuse(
        public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
        secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
        host=os.getenv("LANGFUSE_HOST", "http://localhost:3000"),
    )
    yield
    await app.state.langfuse.aclose()


app = FastAPI(lifespan=lifespan)


@app.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    chain = create_chat_chain(
        system_prompt="You are a helpful AI assistant that provides clear and concise answers."
    )

    chat_history = convert_to_langchain_messages(request.chat_history)
    
    response = chain.invoke({
        "chat_history": chat_history,
        "input": request.user_input,
    })

    return ChatResponse(response=response.content)


# LangServeルートの追加
add_routes(app, create_chat_chain(os.getenv("SYSTEM_PROMPT", "You are a helpful assistant.")), path="/chain") 