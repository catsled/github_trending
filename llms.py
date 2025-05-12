from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


BASE_URL = ""
OLLAMA_MODEL = "qwen2.5:32b"
REMOTE_MODEL = ""
API_KEY = "empty"
TEMPERATURE = 0.5


def get_llm():
    try:
        llm = ChatOllama(
            base_url=BASE_URL,
            model=OLLAMA_MODEL,
            temperature=TEMPERATURE
        )
        llm.invoke("hello")
        return llm
    except Exception as e:
        llm = ChatOpenAI(
            base_url = BASE_URL,
            model=REMOTE_MODEL,
            api_key=API_KEY,
            temperature=TEMPERATURE
        )
        return llm
