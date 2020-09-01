# doc_datatypes
## Installation
```
git clone git@github.com:Kel0/doc_dict.git
```
```
pip install doc-datatypes
```
[pypi](https://pypi.org/project/doc-datatypes/)
## Usage
### Documentable list
```
from doc_datatypes.mutable_datatypes import DocumentedList


my_list: DocumentedList = DocumentedList(
    [1, 2, 3], ["First", "Second", "Third"]
)
my_list_2: DocumentedList = DocumentedList(
    [[1, "First"], [2, "Second"], [3, "Third"]]
)
```
### Documentable dict
```
from doc_datatypes.mutable_datatypes import DocumentedDict


my_dict: DocumentedDict = DocumentedDict(
    {"name": "Alex"}, {"name": "Name field"}
)

my_dict_2: DocumentedDict = DocumentedDict(
    {"name": "Alex", "name_doc": "Name field"}
)
```

To get more info see [tests](https://github.com/Kel0/doc_datatypes/tree/master/tests)
