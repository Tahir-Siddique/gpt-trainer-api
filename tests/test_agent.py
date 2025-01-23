def test_create_agent(gpt_trainer_api, requests_mock_instance):
    chatbot_uuid = "chatbot-123"
    # Mock response for creating an agent
    endpoint = f"https://app.gpt-trainer.com/api/v1/chatbot/{chatbot_uuid}/agent/create"
    requests_mock_instance.post(
        endpoint,
        json={"uuid": "agent-123", "name": "Agent 1", "type": "user-facing"},
        status_code=200,
    )

    # Call the API
    response = gpt_trainer_api.agent.create_agent(chatbot_uuid, {
        "name": "Agent 1",
        "type": "user-facing",
        "description": "Test description",
        "prompt": "Test prompt",
        "model": "gpt-4o-mini-4k"
    })

    # Assert the response
    assert response.uuid == "agent-123"
    assert response.name == "Agent 1"
    assert response.type == "user-facing"

