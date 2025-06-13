from typing import List, Optional, Iterator
from supabaseHelper.supabase_storage_item import SupabaseStorageItem

class SupabaseFolderListing:
    def __init__(self, folder_path: str, items: List[dict]):
        self.folder_path = folder_path
        self.items = [SupabaseStorageItem(**item) for item in items]

    def get_names(self) -> List[str]:
        return [item.name for item in self.items]

    def find_item(self, name: str) -> Optional[SupabaseStorageItem]:
        return next((item for item in self.items if item.name == name), None)
    
    def __iter__(self) -> Iterator[SupabaseStorageItem]:
        return iter(self.items)