from __future__ import annotations

from typing import Any, Dict, List, Union

from .datastructures import DocumentedValue


def documented_dict(content: Dict[str, Any]) -> Dict[str, DocumentedValue]:
    dict_: Dict[str, DocumentedValue] = {}

    value_keys: List[Union[str]] = [
        value_key for value_key in content if "_doc" not in value_key
    ]
    value_key: str

    for value_key in value_keys:
        documented_value: DocumentedValue = DocumentedValue(
            value=content[value_key], doc=content.get(f"{value_key}_doc", "no docs")
        )
        dict_.update({value_key: documented_value})

    return dict_
