from gpt_trainer.chatbot.chatbot_api import ChatbotAPI
from gpt_trainer.agent.agent_api import AgentAPI
from gpt_trainer.data_source.data_source_tag_api import DataSourceTagAPI
from gpt_trainer.session.session_api import SessionAPI
from gpt_trainer.session.message_api import MessageAPI
from gpt_trainer.data_source.source_api import SourceAPI


class GPTTrainerAPI:
    """
    Unified API client for all GPT Trainer components.
    """
    def __init__(self, token: str) -> None:
        """
        Initialize the unified API client.
        :param token: Authorization token.
        """
        self.token = token
        self.chatbot = ChatbotAPI(token)
        self.agent = AgentAPI(token)
        self.session = SessionAPI(token)
        self.message = MessageAPI(token)
        self.data_source = SourceAPI(token)
        self.data_source_tag = DataSourceTagAPI(token)

    def get_components(self) -> dict:
        """
        Get a list of all components available in the API.
        :return: Dictionary of API components.
        """
        return {
            "chatbot": self.chatbot,
            "agent": self.agent,
            "session": self.session,
            "message": self.message,
            "data_source": self.data_source,
        }
