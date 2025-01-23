from gpt_trainer.base import BaseAPI
from gpt_trainer.agent.agent_models import Agent
from gpt_trainer.agent.agent_properties import AGENT_PROPERTIES
from typing import List


class AgentAPI(BaseAPI):
    def __init__(self, token: str) -> None:
        """
        Initialize the Agent API client.
        :param token: Authorization token.
        """
        super().__init__(token)
        self.endpoint_prefix: str = '/chatbot'

    def get_properties(self) -> dict:
        """
        Retrieve agent properties metadata.
        :return: Dictionary containing property details.
        """
        return AGENT_PROPERTIES

    def get_agents(self, chatbot_uuid: str) -> List[Agent]:
        """
        Retrieve a list of agents for a chatbot.
        :param chatbot_uuid: UUID of the chatbot.
        :return: List of Agent objects.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/agents'
        response = self._call_api('GET', endpoint)
        agent_data = response.json()
        return [Agent.from_dict(item) for item in agent_data]

    def get_agent(self, agent_uuid: str) -> Agent:
        """
        Retrieve details of a specific agent.
        :param agent_uuid: UUID of the agent.
        :return: Agent object.
        """
        endpoint = f'/agent/{agent_uuid}'
        response = self._call_api('GET', endpoint)
        return Agent.from_dict(response.json())

    def create_agent(self, chatbot_uuid: str, data: dict) -> Agent:
        """
        Create a new agent.
        :param chatbot_uuid: UUID of the chatbot.
        :param data: Dictionary containing agent creation details.
        :return: Agent object.
        """
        endpoint = f'{self.endpoint_prefix}/{chatbot_uuid}/agent/create'
        response = self._call_api('POST', endpoint, data)
        return Agent.from_dict(response.json())

    def update_agent(self, agent_uuid: str, data: dict) -> Agent:
        """
        Update an existing agent.
        :param agent_uuid: UUID of the agent to update.
        :param data: Dictionary containing updated agent details.
        :return: Agent object.
        """
        endpoint = f'/agent/{agent_uuid}/update'
        response = self._call_api('POST', endpoint, data)
        return Agent.from_dict(response.json())

    def delete_agent(self, agent_uuid: str) -> None:
        """
        Delete an agent.
        :param agent_uuid: UUID of the agent to delete.
        """
        endpoint = f'/agent/{agent_uuid}/delete'
        self._call_api('DELETE', endpoint)
