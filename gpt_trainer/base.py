import requests
from typing import Optional, Dict, Any


class BaseAPI:
    API_VERSION: str = '/api/v1'
    BASE_URL: str = 'https://app.gpt-trainer.com'

    def __init__(self, token: str) -> None:
        """
        Initialize the API client.
        :param token: Authorization token.
        """
        self.base_url: str = self.BASE_URL.rstrip('/')  # Ensure no trailing slash
        self.token: str = token

    def _get_full_url(self, endpoint: str) -> str:
        """
        Construct the full URL for the API call.
        :param endpoint: API endpoint (e.g., '/chatbot/create').
        :return: Full API URL.
        """
        return f"{self.base_url}{self.API_VERSION}{endpoint}"

    def _call_api(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        stream: bool = False
    ) -> requests.Response:
        """
        A generic method for making API calls.
        :param method: HTTP method ('GET', 'POST', 'DELETE', etc.).
        :param endpoint: Endpoint of the API (e.g., '/chatbot/create').
        :param data: Payload for POST requests (optional).
        :param params: Query parameters for GET requests (optional).
        :param files: Files to upload for multipart POST requests (optional).
        :param stream: Boolean to enable streaming responses (default: False).
        :return: Response object.
        """
        url: str = self._get_full_url(endpoint)
        headers: Dict[str, str] = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json' if not files else None,
        }

        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, params=params, stream=stream)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=headers, json=data, params=params, files=files, stream=stream)
            elif method.upper() == 'DELETE':
                response = requests.delete(url, headers=headers, params=params, stream=stream)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            # Raise an HTTP error for non-2xx responses
            response.raise_for_status()
            return response

        except requests.HTTPError as http_err:
            error_details = response.json() if response.status_code == 400 else ""
            raise RuntimeError(f"HTTP error occurred: {http_err} {error_details}") from http_err
        except Exception as err:
            raise RuntimeError(f"An error occurred: {err}") from err
