from gpt_trainer.base import BaseAPI
from typing import Dict, Any
import requests


class DataSourceTagAPI(BaseAPI):
    def __init__(self, token: str) -> None:
        """
        Initialize the DataSourceTag API client.
        :param token: Authorization token.
        """
        super().__init__(token)
        self.endpoint_prefix: str = '/chatbot'

    def create_tag(self, chatbot_uuid: str, name: str, color: str) -> requests.Response:
        """
        Create a new data source tag.
        :param chatbot_uuid: UUID of the chatbot.
        :param name: Name of the tag.
        :param color: Color of the tag in HEX format.
        :return: Response object.
        """
        endpoint: str = f'{self.endpoint_prefix}/{chatbot_uuid}/source-tag/create'
        data: Dict[str, Any] = {"name": name, "color": color}
        return self._call_api('POST', endpoint, data)

    def list_tags(self, chatbot_uuid: str) -> requests.Response:
        """
        List all tags for a chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :return: Response object.
        """
        endpoint: str = f'{self.endpoint_prefix}/{chatbot_uuid}/source-tags'
        return self._call_api('GET', endpoint)

    def update_tag(self, tag_uuid: str, name: str) -> requests.Response:
        """
        Update a data source tag.
        :param tag_uuid: UUID of the tag.
        :param name: Updated name of the tag.
        :return: Response object.
        """
        endpoint: str = f'/source-tag/{tag_uuid}/update'
        data: Dict[str, Any] = {"name": name}
        return self._call_api('POST', endpoint, data)

    def delete_tag(self, tag_uuid: str) -> requests.Response:
        """
        Delete a data source tag.
        :param tag_uuid: UUID of the tag.
        :return: Response object.
        """
        endpoint: str = f'/source-tag/{tag_uuid}/delete'
        return self._call_api('DELETE', endpoint)
