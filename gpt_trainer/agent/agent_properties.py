AGENT_PROPERTIES = {
    "uuid": {
        "type": "string",
        "description": "Unique identifier of the agent."
    },
    "name": {
        "type": "string",
        "description": "Internal name for the agent in your list of agents."
    },
    "description": {
        "type": "string",
        "description": (
            "The description assists the AI in coordinating between user-facing agents by "
            "clarifying the purpose and functionality of each agent."
        )
    },
    "prompt": {
        "type": "string",
        "description": (
            "The prompt helps the AI understand what you want and how to respond. "
            "It guides the conversation and ensures relevant and coherent answers."
        )
    },
    "type": {
        "type": "select",
        "options": ["user-facing", "background", "human-escalation", "pre-canned", "spam-defense"],
        "description": (
            "The type of agent. Options are:\n"
            "- user-facing: Directly interacts with users conversationally in a Q&A fashion.\n"
            "- background: Monitors the conversation without direct interaction.\n"
            "- human-escalation: Routes the query to a human.\n"
            "- pre-canned: Returns a pre-canned response to the user’s query.\n"
            "- spam-defense: Enables spam-defending features."
        )
    },
    "enabled": {
        "type": "boolean",
        "description": "Indicates whether the agent is enabled or disabled."
    },
    "modified_at": {
        "type": "string",
        "description": "Timestamp indicating the last modification time (ISO 8601)."
    },
    "created_at": {
        "type": "string",
        "description": "Timestamp indicating the creation time (ISO 8601)."
    },
    "data_source_uuids": {
        "type": "List[string]",
        "description": (
            "List of data sources UUIDs that the agent uses. If `use_all_sources` in agent’s "
            "meta is set to true, this field will be disabled. Only for user-facing agents."
        )
    },
    "human_escalation_settings": {
        "type": "HumanEscalationSettings Object",
        "description": "Human escalation settings for the agent. Only for human-escalation agents."
    },
    "tool_functions": {
        "type": "List[ToolFunction]",
        "description": "List of tool functions that the agent uses. Only for user-facing and background agents."
    },
    "variables": {
        "type": "List[AgentVariable]",
        "description": "List of variables that the agent uses. Only for user-facing agents."
    },
    "meta": {
        "type": "meta Object",
        "description": "Agent meta properties."
    }
}
