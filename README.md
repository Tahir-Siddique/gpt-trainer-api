
# GPT Trainer API Python Client

A Python client library for interacting with the GPT Trainer API. This library provides an easy-to-use interface for managing chatbots, agents, sessions, messages, and data sources.

---

## Features

- **Chatbot Management**: Create, update, list, and delete chatbots.
- **Agent Management**: Manage agents associated with chatbots.
- **Session Management**: Create and manage chatbot sessions.
- **Message Management**: Retrieve and manage messages within sessions.
- **Data Source Management**: Upload, update, and delete chatbot data sources.

---

## Installation

Install the library via `pip`:

```bash
pip install gpt-trainer-api
```

Alternatively, if you're developing locally, clone this repository and install it:

```bash
git clone https://github.com/Tahir-Siddique/gpt-trainer-api.git
cd gpt-trainer-api
pip install .
```

---

## Usage

### Initialize the API

```python
from gpt_trainer.api import GPTTrainerAPI

# Initialize the GPT Trainer API client
api = GPTTrainerAPI(token="<your-api-token>")
```

---

### Chatbot API

#### List all chatbots

```python
chatbots = api.chatbot.get_chatbots()
for chatbot in chatbots:
    print(chatbot.name, chatbot.uuid)
```

#### Create a chatbot

```python
data = {
    "name": "My New Chatbot",
    "visibility": "private",
    "rate_limit": [20, 240],
    "rate_limit_message": "Too many messages. Try again later.",
    "show_citations": True,
}
new_chatbot = api.chatbot.create_chatbot(data)
print(new_chatbot.uuid, new_chatbot.name)
```

---

### Agent API

#### List all agents for a chatbot

```python
chatbot_uuid = "<chatbot-uuid>"
agents = api.agent.get_agents(chatbot_uuid)
for agent in agents:
    print(agent.name, agent.type)
```

#### Create an agent

```python
data = {
    "name": "Agent 1",
    "description": "Handles FAQs",
    "prompt": "Answer all FAQs concisely.",
    "type": "user-facing",
    "enabled": True,
}
new_agent = api.agent.create_agent(chatbot_uuid, data)
print(new_agent.uuid, new_agent.name)
```

---

### Session API

#### Create a new session

```python
new_session = api.session.create_session(chatbot_uuid)
print(new_session.uuid, new_session.created_at)
```

#### List sessions

```python
sessions = api.session.list_sessions(chatbot_uuid)
for session in sessions:
    print(session.uuid, session.meta)
```

---

### Message API

#### List messages in a session

```python
session_uuid = "<session-uuid>"
messages = api.message.list_messages(session_uuid)
for message in messages:
    print(message.query, message.response)
```

---

### Data Source API

#### List all data sources for a chatbot

```python
sources = api.data_source.list_sources(chatbot_uuid)
for source in sources:
    print(source.file_name, source.status)
```

#### Upload a file as a data source

```python
file_path = "/path/to/your/file.txt"
new_source = api.data_source.upload_file(chatbot_uuid, file_path)
print(new_source.uuid, new_source.title)
```

---

## Requirements

- Python >= 3.7
- `requests` library

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Support

If you encounter any issues or have questions, please open an issue in the [GitHub repository](https://github.com/Tahir-Siddique/gpt-trainer-api/issues).

---

## Authors

- **Tahir Siddique** - Python Developer - [Tahir Siddique](https://github.com/Tahir-Siddique)

### Key Sections

1. **Features**:
   - Highlights what the library can do.
2. **Installation**:
   - Instructions for installing the package.
3. **Usage**:
   - Code examples for common operations.
4. **Requirements**:
   - Dependencies for the library.
5. **Contributing**:
   - Instructions for contributing to the project.
6. **License**:
   - Licensing information.
7. **Support**:
   - Instructions for getting help or reporting issues.
8. **Authors**:
   - Credits to the creator(s).
