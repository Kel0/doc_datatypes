# doc_datatypes
## Installation
```
git clone git@github.com:Kel0/doc_dict.git
```
```
pip install doc-dict
```
## Usage
```
from doc_datatypes.mutable_datatypes import DocumentedList
from doc_datatypes.datatypes import DocumentedIndex


my_list: List[DocumentedIndex] = DocumentedList(
    [1, 2, 3], ["First", "Second", "Third"]
)
my_list_2: List[DocumentedIndex] = DocumentedList(
    [[1, "First"], [2, "Second"], [3, "Third"]]
)
```

To get more info see [tests](https://github.com/Kel0/doc_datatypes/tree/master/tests)

# Contacts
@dead_lynxx
