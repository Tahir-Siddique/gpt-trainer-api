from typing import Optional, List, Dict


class Chatbot:
    def __init__(
        self,
        uuid: str,
        name: str,
        visibility: str,
        rate_limit: List[int],
        rate_limit_message: str,
        show_citations: bool,
        modified_at: str,
        created_at: str
    ) -> None:
        self.uuid = uuid
        self.name = name
        self.visibility = visibility
        self.rate_limit = rate_limit
        self.rate_limit_message = rate_limit_message
        self.show_citations = show_citations
        self.modified_at = modified_at
        self.created_at = created_at

    @classmethod
    def from_dict(cls, data: Dict) -> "Chatbot":
        """
        Create a Chatbot object from a dictionary.
        """
        return cls(
            uuid=data.get("uuid"),
            name=data.get("name"),
            visibility=data.get("visibility"),
            rate_limit=data.get("rate_limit", []),
            rate_limit_message=data.get("rate_limit_message", ""),
            show_citations=data.get("show_citations", False),
            modified_at=data.get("modified_at", ""),
            created_at=data.get("created_at", "")
        )

    def to_dict(self) -> Dict:
        """
        Convert a Chatbot object back into a dictionary.
        """
        return {
            "uuid": self.uuid,
            "name": self.name,
            "visibility": self.visibility,
            "rate_limit": self.rate_limit,
            "rate_limit_message": self.rate_limit_message,
            "show_citations": self.show_citations,
            "modified_at": self.modified_at,
            "created_at": self.created_at
        }
