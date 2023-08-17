from langchain.chat_models import ChatOpenAI


class BaseService:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo")
