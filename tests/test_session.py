def test_create_session(gpt_trainer_api, requests_mock_instance):
    chatbot_uuid = "chatbot-123"
    # Mock response for creating a session
    endpoint = f"https://app.gpt-trainer.com/api/v1/chatbot/{chatbot_uuid}/session/create"
    requests_mock_instance.post(
        endpoint,
        json={"uuid": "session-123"},
        status_code=200,
    )

    # Call the API
    session = gpt_trainer_api.session.create_session(chatbot_uuid)

    # Assert the response
    assert session.uuid == "session-123"


def test_list_sessions(gpt_trainer_api, requests_mock_instance):
    chatbot_uuid = "chatbot-123"
    # Mock response for listing sessions
    endpoint = f"https://app.gpt-trainer.com/api/v1/chatbot/{chatbot_uuid}/sessions"
    requests_mock_instance.get(
        endpoint,
        json=[
            {"uuid": "session-123", "created_at": "2023-01-01T00:00:00Z"},
            {"uuid": "session-456", "created_at": "2023-01-02T00:00:00Z"}
        ],
        status_code=200,
    )

    # Call the API
    sessions = gpt_trainer_api.session.list_sessions(chatbot_uuid)

    # Assert the response
    assert len(sessions) == 2
    assert sessions[0].uuid == "session-123"
    assert sessions[1].created_at == "2023-01-02T00:00:00Z"
