def test_stream_message(gpt_trainer_api, requests_mock_instance):
    session_uuid = "session-123"
    query = "What is AI?"

    # Mock API response
    streamed_response = "Artificial Intelligence is..."
    requests_mock_instance.post(
        f"https://app.gpt-trainer.com/api/v1/session/{session_uuid}/message/stream",
        text=streamed_response,
        status_code=200,
    )

    # Call the API
    response = gpt_trainer_api.message.stream_message(session_uuid, query)

    # Assert response
    assert response == streamed_response


def test_list_messages(gpt_trainer_api, requests_mock_instance):
    session_uuid = "session-123"
    # Mock API response
    requests_mock_instance.get(
        f"https://app.gpt-trainer.com/api/v1/session/{session_uuid}/messages",
        json=[
            {"uuid": "msg-1", "query": "What is AI?", "response": "AI stands for..."},
            {"uuid": "msg-2", "query": "Define ML", "response": "ML is Machine Learning..."},
        ],
        status_code=200,
    )

    # Call the API
    messages = gpt_trainer_api.message.list_messages(session_uuid)

    # Assert response
    assert len(messages) == 2
    assert messages[0].query == "What is AI?"
    assert messages[1].response == "ML is Machine Learning..."
