from typing import List, Dict, Optional


class Agent:
    def __init__(
        self,
        uuid: str,
        name: str,
        description: str,
        prompt: str,
        type: str,
        enabled: bool,
        modified_at: str,
        created_at: str,
        data_source_uuids: Optional[List[str]] = None,
        human_escalation_settings: Optional[Dict] = None,
        tool_functions: Optional[List[Dict]] = None,
        variables: Optional[List[Dict]] = None,
        meta: Optional[Dict] = None
    ) -> None:
        self.uuid = uuid
        self.name = name
        self.description = description
        self.prompt = prompt
        self.type = type
        self.enabled = enabled
        self.modified_at = modified_at
        self.created_at = created_at
        self.data_source_uuids = data_source_uuids or []
        self.human_escalation_settings = human_escalation_settings
        self.tool_functions = tool_functions or []
        self.variables = variables or []
        self.meta = meta

    @classmethod
    def from_dict(cls, data: Dict) -> "Agent":
        """
        Create an Agent object from a dictionary.
        """
        return cls(
            uuid=data.get("uuid"),
            name=data.get("name"),
            description=data.get("description"),
            prompt=data.get("prompt"),
            type=data.get("type"),
            enabled=data.get("enabled", False),
            modified_at=data.get("modified_at", ""),
            created_at=data.get("created_at", ""),
            data_source_uuids=data.get("data_source_uuids"),
            human_escalation_settings=data.get("human_escalation_settings"),
            tool_functions=data.get("tool_functions"),
            variables=data.get("variables"),
            meta=data.get("meta"),
        )

    def to_dict(self) -> Dict:
        """
        Convert an Agent object back into a dictionary.
        """
        return {
            "uuid": self.uuid,
            "name": self.name,
            "description": self.description,
            "prompt": self.prompt,
            "type": self.type,
            "enabled": self.enabled,
            "modified_at": self.modified_at,
            "created_at": self.created_at,
            "data_source_uuids": self.data_source_uuids,
            "human_escalation_settings": self.human_escalation_settings,
            "tool_functions": self.tool_functions,
            "variables": self.variables,
            "meta": self.meta,
        }
