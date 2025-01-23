MESSAGE_PROPERTIES = {
    "uuid": {
        "type": "string",
        "description": "Unique identifier of the message."
    },
    "created_at": {
        "type": "string",
        "description": "Timestamp indicating the creation time of the message (ISO 8601)."
    },
    "modified_at": {
        "type": "string",
        "description": "Timestamp indicating the last modification time of the message (ISO 8601)."
    },
    "finish_reason": {
        "type": "string",
        "description": (
            "The reason the model stopped generating the message. This will be `stop` if the model hit "
            "a natural stop point or a provided stop sequence, or `length` if the maximum number of tokens "
            "specified in the request was reached."
        )
    },
    "cite_data_json": {
        "type": "string",
        "description": (
            "AI bot credits sources and includes links to specific information it used from your trained data. "
            "Enable `show_citations` property for your Chatbot to make this work."
        )
    },
    "meta_json": {
        "type": "string",
        "description": "Message metadata."
    },
    "query": {
        "type": "string",
        "description": "User's query."
    },
    "response": {
        "type": "string",
        "description": "AI response for the user's query."
    }
}
