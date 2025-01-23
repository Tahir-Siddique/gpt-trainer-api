def test_create_chatbot(gpt_trainer_api, requests_mock_instance):
    # Mock response for creating a chatbot
    endpoint = "https://app.gpt-trainer.com/api/v1/chatbot/create"
    requests_mock_instance.post(
        endpoint,
        json={"uuid": "chatbot-123", "name": "Test Chatbot"},
        status_code=200,
    )

    # Call the API
    response = gpt_trainer_api.chatbot.create_chatbot({
        "name": "Test Chatbot",
        "visibility": "private",
        "rate_limit": [20, 240],
        "rate_limit_message": "Rate limit reached",
        "show_citations": True
    })

    # Assert the response
    assert response.uuid == "chatbot-123"
    assert response.name == "Test Chatbot"


def test_list_chatbots(gpt_trainer_api, requests_mock_instance):
    # Mock response for listing chatbots
    endpoint = "https://app.gpt-trainer.com/api/v1/chatbots"
    requests_mock_instance.get(
        endpoint,
        json=[
            {"uuid": "chatbot-123", "name": "Chatbot 1"},
            {"uuid": "chatbot-456", "name": "Chatbot 2"}
        ],
        status_code=200,
    )

    # Call the API
    chatbots = gpt_trainer_api.chatbot.get_chatbots()

    # Assert the response
    assert len(chatbots) == 2
    assert chatbots[0].uuid == "chatbot-123"
    assert chatbots[1].name == "Chatbot 2"
