import tempfile

def test_upload_file(gpt_trainer_api, requests_mock_instance):
    chatbot_uuid = "chatbot-123"
    # Mock response for uploading a file
    endpoint = f"https://app.gpt-trainer.com/api/v1/chatbot/{chatbot_uuid}/data-source/upload"
    requests_mock_instance.post(
        endpoint,
        json={"uuid": "source-123", "file_name": "example.pdf", "file_size": 1024},
        status_code=200,
    )

    # Use a temporary file for testing
    with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_file:
        temp_file.write(b"Dummy content")
        temp_file.flush()

        # Call the API
        source = gpt_trainer_api.data_source.upload_file(chatbot_uuid, temp_file.name)

    # Assert the response
    assert source.uuid == "source-123"
    assert source.file_name == "example.pdf"
    assert source.file_size == 1024
