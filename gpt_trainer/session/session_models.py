from typing import Dict, Optional


class Session:
    def __init__(
        self,
        uuid: str,
        modified_at: str,
        created_at: str,
        meta: Optional[Dict] = None
    ) -> None:
        self.uuid = uuid
        self.modified_at = modified_at
        self.created_at = created_at
        self.meta = meta or {}

    @classmethod
    def from_dict(cls, data: Dict) -> "Session":
        """
        Create a Session object from a dictionary.
        """
        return cls(
            uuid=data.get("uuid"),
            modified_at=data.get("modified_at", ""),
            created_at=data.get("created_at", ""),
            meta=data.get("meta", {})
        )

    def to_dict(self) -> Dict:
        """
        Convert a Session object back into a dictionary.
        """
        return {
            "uuid": self.uuid,
            "modified_at": self.modified_at,
            "created_at": self.created_at,
            "meta": self.meta
        }
