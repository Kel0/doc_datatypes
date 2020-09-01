from dataclasses import dataclass
from typing import Any, Dict, Generic, TypeVar, Union

T = TypeVar("T")


@dataclass
class DocumentedValue(Generic[T]):
    value: T
    doc: Union[str, Dict[Any, Any]]

    def to_dict(self) -> Dict[str, Any]:
        return {"value": self.value, "doc": self.doc}

    def __call__(self) -> T:
        return self.value

    def __repr__(self) -> str:
        return "{" f'"value": "{self.value}", ' f'"doc": "{self.doc}"' "}"


@dataclass
class DocumentedIndex(Generic[T]):
    value: T
    doc: Union[str, Dict[Any, Any]]

    def __call__(self) -> T:
        return self.value

    def __repr__(self) -> str:
        return f"{self.value} -> {self.doc}"
