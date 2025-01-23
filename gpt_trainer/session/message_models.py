from typing import Dict, Optional


class Message:
    def __init__(
        self,
        uuid: str,
        created_at: str,
        modified_at: str,
        finish_reason: str,
        cite_data_json: Optional[str] = None,
        meta_json: Optional[str] = None,
        query: Optional[str] = None,
        response: Optional[str] = None,
    ) -> None:
        self.uuid = uuid
        self.created_at = created_at
        self.modified_at = modified_at
        self.finish_reason = finish_reason
        self.cite_data_json = cite_data_json
        self.meta_json = meta_json
        self.query = query
        self.response = response

    @classmethod
    def from_dict(cls, data: Dict) -> "Message":
        """
        Create a Message object from a dictionary.
        """
        return cls(
            uuid=data.get("uuid"),
            created_at=data.get("created_at", ""),
            modified_at=data.get("modified_at", ""),
            finish_reason=data.get("finish_reason", ""),
            cite_data_json=data.get("cite_data_json"),
            meta_json=data.get("meta_json"),
            query=data.get("query"),
            response=data.get("response"),
        )

    def to_dict(self) -> Dict:
        """
        Convert a Message object back into a dictionary.
        """
        return {
            "uuid": self.uuid,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
            "finish_reason": self.finish_reason,
            "cite_data_json": self.cite_data_json,
            "meta_json": self.meta_json,
            "query": self.query,
            "response": self.response,
        }
