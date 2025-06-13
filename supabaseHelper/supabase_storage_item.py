from typing import List, Optional

class SupabaseStorageItem:
    def __init__(self, name: str, id: Optional[str] = None, updated_at: Optional[str] = None,
                 created_at: Optional[str] = None, last_accessed_at: Optional[str] = None,
                 metadata: Optional[dict] = None):
        self.name = name
        self.id = id
        self.updated_at = updated_at
        self.created_at = created_at
        self.last_accessed_at = last_accessed_at
        self.metadata = metadata

    def __str__(self):
        fields = vars(self)
        return f"SupabaseStorageItem({', '.join(f'{k}={repr(v)}' for k, v in fields.items())})"

