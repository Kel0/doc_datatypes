# doc_datatypes [![Build Status](https://cloud.drone.io/api/badges/Kel0/doc_datatypes/status.svg?branch=master)](https://cloud.drone.io/Kel0/doc_datatypes/) [![BCH compliance](https://bettercodehub.com/edge/badge/Kel0/doc_datatypes?branch=master)](https://bettercodehub.com/results/Kel0/doc_datatypes)
## Installation
```
git clone https://github.com/Kel0/doc_datatypes.git
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
