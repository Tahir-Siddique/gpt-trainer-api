from gpt_trainer.base import BaseAPI
from gpt_trainer.data_source.source_models import Source
from gpt_trainer.data_source.source_properties import SOURCE_PROPERTIES
from typing import List, Dict


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

    def upload_file(self, chatbot_uuid: str, file_path: str) -> Source:
        """
        Upload a file as a data source for a chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :param file_path: Path to the file to upload.
        :return: Source object.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/data-source/upload'
        with open(file_path, 'rb') as f:
            files = {'file': (file_path, f)}
            response = self._call_api('POST', endpoint, files=files)
        return Source.from_dict(response.json())

    def upload_qa(self, chatbot_uuid: str, question: str, answer: str) -> Source:
        """
        Upload a QA pair as a data source for a chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :param question: The question for the QA pair.
        :param answer: The answer for the QA pair.
        :return: Source object.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/data-source/qa'
        data = {"question": question, "answer": answer}
        response = self._call_api('POST', endpoint, data)
        return Source.from_dict(response.json())

    def add_url(self, chatbot_uuid: str, url: str) -> Source:
        """
        Add a URL as a data source for a chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :param url: The URL to add.
        :return: Source object.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/data-source/url'
        data = {"url": url}
        response = self._call_api('POST', endpoint, data)
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

    def re_scrape_sources(self, uuids: List[str]) -> None:
        """
        Re-scrape URLs for multiple data sources.
        :param uuids: List of source UUIDs to re-scrape.
        """
        endpoint = '/data-sources/url/re-scrape'
        data = {"uuids": uuids}
        self._call_api('POST', endpoint, data)
