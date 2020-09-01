from collections.abc import MutableMapping, MutableSequence
from typing import Any, Dict, List, Optional, Tuple, Union

from .datatypes import DocumentedIndex, DocumentedValue

DICT_CONTENT_TYPE = Dict[Union[str, int, float], Any]
DOC_LIST_CONTENT_TYPE = Union[List[Any], List[list]]


class DocumentedList(MutableSequence):
    def __init__(
        self, content: DOC_LIST_CONTENT_TYPE, docs_content: List[str] = None
    ) -> None:
        self._inner_list: List[DocumentedIndex[Any]] = []
        content, docs = self.__validate_docs_content(content, docs_content)

        for value, doc in zip(content, docs):
            self._inner_list.append(DocumentedIndex(value=value, doc=doc))

    def __validate_docs_content(  # type: ignore
        self, content: DOC_LIST_CONTENT_TYPE, docs_content: Optional[List[str]] = None
    ) -> Tuple[List[Any], List[str]]:
        """Validate content & docs_content data

        :param content: List of main content
        :param docs_content: List of doc strings

        if docs_content is None
        :param content[counter][0]: Main content
        :param content[counter][1]: Doc strings

        if docs_content is not None
        :return content: List[Any] -> Main content
        :return docs_content: List[str] -> Doc strings

        if docs_content is None
        :return temp_content_arr: List[Any] -> Main content
        :return temp_docs_arr: List[str] -> Doc strings"""
        if docs_content is not None:
            if len(content) >= len(docs_content):
                for doc in range(len(content) - len(docs_content)):
                    docs_content.append("no docs")
                return content, docs_content  # type: ignore

            elif len(content) < len(docs_content):
                raise ValueError("Content length less than docs content")

        elif docs_content is None:
            temp_content_arr: List[Any] = []
            temp_docs_arr: List[str] = []

            for item in content:
                if len(item) == 1:
                    temp_content_arr.append(item[0])
                    temp_docs_arr.append("no docs")
                    continue
                temp_content_arr.append(item[0])
                temp_docs_arr.append(item[-1])

            return temp_content_arr, temp_docs_arr

    def get_with_doc(self, index: int) -> str:
        return f"{self._inner_list.__getitem__(index)}"

    def get_doc(self, index: int) -> str:
        return f"{self._inner_list.__getitem__(index).doc}"

    def __len__(self) -> int:
        return len(self._inner_list)

    def __delitem__(self, index: int) -> None:  # type: ignore
        self._inner_list.__delitem__(index)

    def insert(self, index: int, value: Union[str, int, list]) -> None:
        if not isinstance(value, list):
            value = [value, "no docs"]
        elif len(value) == 1:
            value.append("no docs")
        self._inner_list.insert(index, DocumentedIndex(value=value[0], doc=value[1]))

    def __setitem__(self, index: int, value: Union[str, int, list]) -> None:  # type: ignore
        if not isinstance(value, list):
            value = [value, "no docs"]
        elif len(value) == 1:
            value.append("no docs")
        self._inner_list.__setitem__(
            index, DocumentedIndex(value=value[0], doc=value[1])
        )

    def __getitem__(self, index: int) -> Any:  # type: ignore
        return self._inner_list.__getitem__(index)()

    def append(self, value: Union[str, int, list]) -> None:
        self.insert(len(self) + 1, value)

    def __repr__(self) -> str:
        return f"{self._inner_list}"


class DocumentedDict(MutableMapping):
    def __init__(
        self,
        content: DICT_CONTENT_TYPE,
        content_docs: Optional[DICT_CONTENT_TYPE] = None,
    ) -> None:
        self._inner_doc = {}
        content, content_docs = self.__validate_docs_content(content, content_docs)

        for value_key, doc_key in zip(content.keys(), content_docs.keys()):
            self._inner_doc.update(
                {
                    value_key: DocumentedValue(
                        value=content[value_key], doc=content_docs[doc_key]
                    )
                }
            )

    def __validate_docs_content(
        self, content: DICT_CONTENT_TYPE, content_docs: Optional[DICT_CONTENT_TYPE],
    ) -> Tuple[DICT_CONTENT_TYPE, DICT_CONTENT_TYPE]:
        if content_docs is not None:
            if len(content) < len(content_docs):
                raise ValueError()

            for key, value in content.items():
                doc: Optional[str] = content_docs.get(key, None)
                if doc is None:
                    content_docs[key] = "no docs"
            return content, content_docs

        elif content_docs is None:
            temp_content_dict = {}
            temp_content_doc_dict = {}

            for content_key in [key for key in content.keys() if "_doc" not in key]:  # type: ignore
                temp_content_dict[content_key] = content[content_key]
                temp_content_doc_dict[content_key] = content.get(
                    f"{content_key}_doc", "no docs"
                )

            return temp_content_dict, temp_content_doc_dict

    def get_with_doc(
        self, key: Union[str, int, float], placeholder: Optional[Any] = None
    ) -> str:
        return f"{self._inner_doc.get(key, placeholder)}"

    def __getitem__(self, key) -> Any:
        return self._inner_doc[key]()

    def __setitem__(self, key, value) -> None:
        if isinstance(value, list):
            value = DocumentedValue(value=value[0], doc=value[1])
        elif not isinstance(value, list):
            value = DocumentedValue(value=value, doc="no docs")
        self._inner_doc[key] = value

    def __delitem__(self, key) -> None:
        del self._inner_doc[key]

    def __iter__(self) -> Any:
        return iter(self._inner_doc)

    def __len__(self) -> int:
        return len(self._inner_doc)

    def __repr__(self) -> str:
        return f"{self._inner_doc}"
