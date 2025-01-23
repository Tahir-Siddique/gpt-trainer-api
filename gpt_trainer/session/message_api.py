from gpt_trainer.base import BaseAPI
from gpt_trainer.session.message_models import Message
from gpt_trainer.session.message_properties import MESSAGE_PROPERTIES
from typing import List


class MessageAPI(BaseAPI):
    def __init__(self, token: str) -> None:
        """
        Initialize the Message API client.
        :param token: Authorization token.
        """
        super().__init__(token)
        self.endpoint_prefix: str = '/session'

    def get_properties(self) -> dict:
        """
        Retrieve message properties metadata.
        :return: Dictionary containing property details.
        """
        return MESSAGE_PROPERTIES

    def list_messages(self, session_uuid: str) -> List[Message]:
        """
        List all messages for a session.
        :param session_uuid: UUID of the session.
        :return: List of Message objects.
        """
        endpoint = f'{self.endpoint_prefix}/{session_uuid}/messages'
        response = self._call_api('GET', endpoint)
        message_data = response.json()
        return [Message.from_dict(item) for item in message_data]

    def get_message(self, message_uuid: str) -> Message:
        """
        Retrieve details of a specific message.
        :param message_uuid: UUID of the message.
        :return: Message object.
        """
        endpoint = f'/message/{message_uuid}'
        response = self._call_api('GET', endpoint)
        return Message.from_dict(response.json())

    def delete_message(self, message_uuid: str) -> None:
        """
        Delete a specific message.
        :param message_uuid: UUID of the message to delete.
        """
        endpoint = f'/message/{message_uuid}/delete'
        self._call_api('POST', endpoint)

    def bulk_delete_messages(self, uuids: List[str]) -> None:
        """
        Delete multiple messages in bulk.
        :param uuids: List of message UUIDs to delete.
        """
        endpoint = '/messages/delete'
        data = {"uuids": uuids}
        self._call_api('POST', endpoint, data)
