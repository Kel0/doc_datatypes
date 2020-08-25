# doc_dict
## Installation
```
pip install invoke
inv install
```
## Usage
```
from app.factory import documented_dict


my_dict = {
    "first_name": "Mike",
    "first_name_doc": "It's name field",
    "last_name": "Anderson",
}

my_doc_dict = documented_dict(my_dict)
```