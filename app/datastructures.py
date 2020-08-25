from dataclasses import dataclass


@dataclass
class DocumentedValue:
    value: str
    doc: str

    def __repr__(self):  # pragma: no cover
        return "{" f'"value": "{self.value}", ' f'"__doc__": "{self.doc}"' "}"
