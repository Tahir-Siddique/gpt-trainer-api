CHATBOT_PROPERTIES = {
    "uuid": {
        "type": "string",
        "description": "Unique identifier of the chatbot."
    },
    "name": {
        "type": "string",
        "description": "Internal name for the chatbot. Not visible to users."
    },
    "visibility": {
        "type": "select",
        "options": ["private", "public", "hybrid"],
        "description": (
            "Defines who can access the chatbot:\n"
            "- private: Only you (your account) can access it.\n"
            "- public: Accessible via link or embedding on your website.\n"
            "- hybrid: Embedded on your website, no link sharing."
        )
    },
    "rate_limit": {
        "type": "[number, number]",
        "description": (
            "Limits messages sent from one device on iframe or chat bubble:\n"
            "- First number: Number of messages (min: 1, max: 100).\n"
            "- Second number: Time interval in seconds (min: 1, max: 360)."
        )
    },
    "rate_limit_message": {
        "type": "string",
        "description": "Message displayed when the rate limit is reached."
    },
    "show_citations": {
        "type": "boolean",
        "description": (
            "Indicates whether the AI bot credits sources and includes links "
            "to specific information used from trained data."
        )
    },
    "modified_at": {
        "type": "string",
        "description": "Timestamp indicating the last modification time (ISO 8601)."
    },
    "created_at": {
        "type": "string",
        "description": "Timestamp indicating the creation time (ISO 8601)."
    }
}
