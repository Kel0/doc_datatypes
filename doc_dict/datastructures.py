from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class DocumentedValue:
    value: str
    doc: str

    def serialize(self):
        return {"value": self.value, "doc": self.doc}

    def __repr__(self):  # pragma: no cover
        return "{" f'"value": "{self.value}", ' f'"__doc__": "{self.doc}"' "}"


def documented_dict(
    content: Dict[str, Any], content_doc_dict: Dict[str, str] = None
) -> Dict[str, DocumentedValue]:
    dict_: Dict[str, DocumentedValue] = {}
    value_key: str
    documented_value: DocumentedValue

    if not content_doc_dict:
        value_keys: List[str] = [
            value_key for value_key in content if "_doc" not in value_key
        ]

        for value_key in value_keys:
            documented_value = DocumentedValue(
                value=content[value_key], doc=content.get(f"{value_key}_doc", "no docs")
            )
            dict_.update({value_key: documented_value})

    elif content_doc_dict:
        for value_key in content:
            documented_value = DocumentedValue(
                value=content[value_key], doc=content_doc_dict.get(value_key, "no docs")
            )
            dict_.update({value_key: documented_value})

    return dict_
