from typing import List
import os

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain.schema import BaseMessage
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
from pydantic import SecretStr

from .schema import Message

# 環境変数の読み込み
load_dotenv()

def convert_to_langchain_messages(messages: List[Message]) -> List[BaseMessage]:
    message_map = {
        "system": SystemMessage,
        "human": HumanMessage,
        "ai": AIMessage,
    }
    return [message_map[m.role](content=m.content) for m in messages]


def create_chat_chain(system_prompt: str):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ])

    model = ChatOpenAI(
        api_key=SecretStr(os.getenv("OPENAI_API_KEY", "")),
        temperature=0.7
    )
    chain = prompt | model

    return chain