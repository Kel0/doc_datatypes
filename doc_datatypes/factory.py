# from __future__ import annotations
#
# import json
# from typing import Any, Dict
#
# from .datatypes import DocumentedValue
# from .mutable_datatypes import documented_dict
#
#
# class Factory:
#     def load(
#         self, content: Dict[str, Any], content_doc_dict: Dict[str, str] = None
#     ) -> Dict[str, DocumentedValue]:
#         return documented_dict(content, content_doc_dict)
#
#     def serialize(self, content: Dict[str, DocumentedValue]) -> str:
#         return json.dumps({key: value.to_dict() for key, value in content.items()})
