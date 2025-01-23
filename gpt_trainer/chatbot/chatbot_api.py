from gpt_trainer.base import BaseAPI
from gpt_trainer.chatbot.chatbot_models import Chatbot
from gpt_trainer.chatbot.chatbot_properties import CHATBOT_PROPERTIES
from typing import List


class ChatbotAPI(BaseAPI):
    def __init__(self, token: str) -> None:
        """
        Initialize the Chatbot API client.
        :param token: Authorization token.
        """
        super().__init__(token)
        self.endpoint_prefix: str = '/chatbot'

    def get_properties(self) -> dict:
        """
        Retrieve chatbot properties metadata.
        :return: Dictionary containing property details.
        """
        return CHATBOT_PROPERTIES

    def get_chatbots(self) -> List[Chatbot]:
        """
        Retrieve a list of chatbots.
        :return: List of Chatbot objects.
        """
        endpoint = f'{self.endpoint_prefix}s'  # /chatbots
        response = self._call_api('GET', endpoint)
        chatbot_data = response.json()
        return [Chatbot.from_dict(item) for item in chatbot_data]

    def get_chatbot(self, chatbot_uuid: str) -> Chatbot:
        """
        Retrieve details of a specific chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :return: Chatbot object.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}'
        response = self._call_api('GET', endpoint)
        return Chatbot.from_dict(response.json())

    def create_chatbot(self, data: dict) -> Chatbot:
        """
        Create a new chatbot.
        :param data: Dictionary containing chatbot creation details.
        :return: Chatbot object.
        """
        endpoint = f'{self.endpoint_prefix}/create'
        response = self._call_api('POST', endpoint, data)
        return Chatbot.from_dict(response.json())

    def update_chatbot(self, chatbot_uuid: str, data: dict) -> Chatbot:
        """
        Update an existing chatbot.
        :param chatbot_uuid: UUID of the chatbot to update.
        :param data: Dictionary containing updated chatbot details.
        :return: Chatbot object.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/update'
        response = self._call_api('POST', endpoint, data)
        return Chatbot.from_dict(response.json())

    def delete_chatbot(self, chatbot_uuid: str) -> None:
        """
        Delete a chatbot.
        :param chatbot_uuid: UUID of the chatbot to delete.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/delete'
        self._call_api('DELETE', endpoint)
