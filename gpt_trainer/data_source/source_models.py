from typing import Dict, Optional


class Source:
    def __init__(
        self,
        uuid: str,
        modified_at: str,
        created_at: str,
        title: Optional[str] = None,
        tokens: Optional[int] = None,
        file_size: Optional[int] = None,
        file_name: Optional[str] = None,
        type: Optional[str] = None,
        status: Optional[str] = None,
        meta_json: Optional[str] = None,
    ) -> None:
        self.uuid = uuid
        self.modified_at = modified_at
        self.created_at = created_at
        self.title = title
        self.tokens = tokens
        self.file_size = file_size
        self.file_name = file_name
        self.type = type
        self.status = status
        self.meta_json = meta_json

    @classmethod
    def from_dict(cls, data: Dict) -> "Source":
        """
        Create a Source object from a dictionary.
        """
        return cls(
            uuid=data.get("uuid"),
            modified_at=data.get("modified_at", ""),
            created_at=data.get("created_at", ""),
            title=data.get("title"),
            tokens=data.get("tokens"),
            file_size=data.get("file_size"),
            file_name=data.get("file_name"),
            type=data.get("type"),
            status=data.get("status"),
            meta_json=data.get("meta_json"),
        )

    def to_dict(self) -> Dict:
        """
        Convert a Source object back into a dictionary.
        """
        return {
            "uuid": self.uuid,
            "modified_at": self.modified_at,
            "created_at": self.created_at,
            "title": self.title,
            "tokens": self.tokens,
            "file_size": self.file_size,
            "file_name": self.file_name,
            "type": self.type,
            "status": self.status,
            "meta_json": self.meta_json,
        }
