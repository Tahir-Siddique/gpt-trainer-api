from gpt_trainer.base import BaseAPI
from gpt_trainer.session.session_models import Session
from gpt_trainer.session.session_properties import SESSION_PROPERTIES
from typing import List


class SessionAPI(BaseAPI):
    def __init__(self, token: str) -> None:
        """
        Initialize the Session API client.
        :param token: Authorization token.
        """
        super().__init__(token)
        self.endpoint_prefix: str = '/chatbot'

    def get_properties(self) -> dict:
        """
        Retrieve session properties metadata.
        :return: Dictionary containing property details.
        """
        return SESSION_PROPERTIES

    def create_session(self, chatbot_uuid: str) -> Session:
        """
        Create a new session for a chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :return: Session object.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/session/create'
        response = self._call_api('POST', endpoint)
        return Session.from_dict(response.json())

    def get_session(self, session_uuid: str) -> Session:
        """
        Retrieve details of a specific session.
        :param session_uuid: UUID of the session.
        :return: Session object.
        """
        endpoint = f'/session/{session_uuid}'
        response = self._call_api('GET', endpoint)
        return Session.from_dict(response.json())

    def list_sessions(self, chatbot_uuid: str) -> List[Session]:
        """
        List all sessions for a chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :return: List of Session objects.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/sessions'
        response = self._call_api('GET', endpoint)
        session_data = response.json()
        return [Session.from_dict(item) for item in session_data]

    def delete_session(self, session_uuid: str) -> None:
        """
        Delete a specific session.
        :param session_uuid: UUID of the session to delete.
        """
        endpoint = f'/session/{session_uuid}/delete'
        self._call_api('POST', endpoint)
