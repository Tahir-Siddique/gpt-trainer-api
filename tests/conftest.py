import pytest
import requests_mock
from gpt_trainer.api import GPTTrainerAPI


@pytest.fixture
def gpt_trainer_api():
    """
    Fixture to initialize GPTTrainerAPI with a dummy token.
    """
    return GPTTrainerAPI(token="dummy-token")


@pytest.fixture
def requests_mock_instance():
    """
    Fixture to set up a requests-mock instance for API call mocking.
    """
    with requests_mock.Mocker() as mocker:
        yield mocker
