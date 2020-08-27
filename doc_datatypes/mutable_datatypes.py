import collections
from typing import Any, Dict, List

from .datatypes import DocumentedIndex, DocumentedValue


class DocumentedList(collections.abc.MutableSequence):
    def __init__(self, content: list, docs_content: list = None):
        self._inner_list = list()
        content, docs = self.__validate_docs_content(content, docs_content)

        for value, doc in zip(content, docs):
            self._inner_list.append(DocumentedIndex(value=value, doc=doc))

    def __validate_docs_content(self, content: list, docs_content: list = None):
        if docs_content is not None:
            if len(content) >= len(docs_content):
                for doc in range(len(content) - len(docs_content)):
                    docs_content.append("no docs")
                return content, docs_content

            elif len(content) < len(docs_content):
                raise ValueError("Content length less than docs content")

        elif docs_content is None:
            temp_content_arr = []
            temp_docs_arr = []

            for item in content:
                if len(item) == 1:
                    temp_content_arr.append(item[0])
                    temp_docs_arr.append("no docs")
                    continue
                temp_content_arr.append(item[0])
                temp_docs_arr.append(item[1])

            return temp_content_arr, temp_docs_arr

    def get_with_doc(self, index: int):
        return f"{self._inner_list.__getitem__(index)}"

    def get_doc(self, index: int):
        return f"{self._inner_list.__getitem__(index).doc}"

    def __len__(self):
        return len(self._inner_list)

    def __delitem__(self, index):
        self._inner_list.__delitem__(index)

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(value, list):
            value = [value, "no docs"]
        elif len(value) == 1:
            value.append("no docs")

        self._inner_list.insert(index, DocumentedIndex(value=value[0], doc=value[1]))

    def __setitem__(self, index: int, value: Any):  # type: ignore
        if not isinstance(value, list):
            value = [value, "no docs"]
        elif len(value) == 1:
            value.append("no docs")

        self._inner_list.__setitem__(
            index, DocumentedIndex(value=value[0], doc=value[1])
        )

    def __getitem__(self, index):
        return self._inner_list.__getitem__(index)()

    def append(self, value: Any):
        self.insert(len(self) + 1, value)

    def __repr__(self):
        return f"{self._inner_list}"


def documented_dict(  # pragma: no cover; todo
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
