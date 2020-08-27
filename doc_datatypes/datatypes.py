from dataclasses import dataclass
from typing import Any


@dataclass
class DocumentedValue:
    value: Any
    doc: str

    def to_dict(self):
        return {"value": self.value, "doc": self.doc}

    def __repr__(self):
        return "{" f'"value": "{self.value}", ' f'"__doc__": "{self.doc}"' "}"


@dataclass
class DocumentedIndex:
    value: Any
    doc: str

    def __call__(self):
        return self.value

    def __repr__(self):
        return f"{self.value} -> {self.doc}"
