from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


BASE_URL = ""
OLLAMA_MODEL = "qwen3:4b"
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
        response = llm.invoke("hello")
        print(response)
        return llm
    except Exception as e:
        llm = ChatOpenAI(
            base_url = BASE_URL,
            model=REMOTE_MODEL,
            api_key=API_KEY,
            temperature=TEMPERATURE
        )
        return llm


if __name__ == "__main__":
    llm = get_llm()
