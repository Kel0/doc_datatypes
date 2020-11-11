from dataclasses import dataclass
from typing import Any, Dict, Generic, TypeVar, Union

T = TypeVar("T")


def _display_concrete_type(content: T) -> Any:
    """Display concrete type of var. i.e if
    provided content is str. type display 'provided content'

    :param content: Content for concrete display it's type
    :return content: Concrete displayed content"""
    if isinstance(content, str):
        return f'"{content}"'
    else:
        return content


@dataclass
class DocumentedValue(Generic[T]):
    """Docmented value class for dictionary type"""

    value: T
    doc: Union[str, Dict[Any, Any]]

    def to_dict(self) -> Dict[str, Any]:
        """Convert object's value & doc into dictionary

        :return value: Object's value
        :return doc: Object's doc. string"""
        return {"value": self.value, "doc": self.doc}

    def __call__(self) -> T:
        """Return object's value"""
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
    """Documented index class for list type"""

    value: T
    doc: Union[str, Dict[Any, Any]]

    def __call__(self) -> T:
        """Return object's value"""
        return self.value

    def __repr__(self) -> str:
        return f"{_display_concrete_type(self.value)} -> {self.doc}"
