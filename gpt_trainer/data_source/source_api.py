from gpt_trainer.base import BaseAPI
from gpt_trainer.data_source.source_models import Source
from gpt_trainer.data_source.source_properties import SOURCE_PROPERTIES
from typing import List


class SourceAPI(BaseAPI):
    def __init__(self, token: str) -> None:
        """
        Initialize the Source API client.
        :param token: Authorization token.
        """
        super().__init__(token)
        self.endpoint_prefix: str = '/chatbot'

    def get_properties(self) -> dict:
        """
        Retrieve source properties metadata.
        :return: Dictionary containing property details.
        """
        return SOURCE_PROPERTIES

    def list_sources(self, chatbot_uuid: str) -> List[Source]:
        """
        List all data sources for a chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :return: List of Source objects.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/data-sources'
        response = self._call_api('GET', endpoint)
        source_data = response.json()
        return [Source.from_dict(item) for item in source_data]

    def get_source(self, source_uuid: str) -> Source:
        """
        Retrieve details of a specific source.
        :param source_uuid: UUID of the source.
        :return: Source object.
        """
        endpoint = f'/data-source/{source_uuid}'
        response = self._call_api('GET', endpoint)
        return Source.from_dict(response.json())

    def update_source(self, source_uuid: str, title: str) -> Source:
        """
        Update the title of a specific source.
        :param source_uuid: UUID of the source.
        :param title: New title for the source.
        :return: Updated Source object.
        """
        endpoint = f'/data-source/{source_uuid}/update'
        data = {"title": title}
        response = self._call_api('POST', endpoint, data)
        return Source.from_dict(response.json())

    def delete_source(self, source_uuid: str) -> None:
        """
        Delete a specific source.
        :param source_uuid: UUID of the source to delete.
        """
        endpoint = f'/data-source/{source_uuid}/delete'
        self._call_api('POST', endpoint)

    def bulk_delete_sources(self, uuids: List[str]) -> None:
        """
        Delete multiple sources in bulk.
        :param uuids: List of source UUIDs to delete.
        """
        endpoint = '/data-sources/delete'
        data = {"uuids": uuids}
        self._call_api('POST', endpoint, data)
