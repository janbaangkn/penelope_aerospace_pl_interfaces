from typing import List, Any


class NoObjectFoundWithUID(Exception):
    """Raised if no object was found that matches a specified uid."""

    def __init__(self):
        message = "No object was found that matches the specified uid."
        super().__init__(message)


def collect_object_with_uid(uid: str, object_list: List[Any]) -> Any:
    for element in object_list:
        if element.uid == uid:
            return element
    raise NoObjectFoundWithUID()
