from dataclasses import dataclass
from typing import Any, Dict, Generic, TypeVar, Union

T = TypeVar("T")


def _display_concrete_type(content: T) -> Any:
    if isinstance(content, str):
        return f'"{content}"'
    else:
        return content


@dataclass
class DocumentedValue(Generic[T]):
    value: T
    doc: Union[str, Dict[Any, Any]]

    def to_dict(self) -> Dict[str, Any]:
        return {"value": self.value, "doc": self.doc}

    def __call__(self) -> T:
        return self.value

    def __repr__(self) -> str:
        return (
            "{"
            f'"value": {_display_concrete_type(self.value)}, '
            f'"doc": {_display_concrete_type(self.doc)}'
            "}"
        )


@dataclass
class DocumentedIndex(Generic[T]):
    value: T
    doc: Union[str, Dict[Any, Any]]

    def __call__(self) -> T:
        return self.value

    def __repr__(self) -> str:
        return f"{_display_concrete_type(self.value)} -> {self.doc}"
