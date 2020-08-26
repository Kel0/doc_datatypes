# doc_dict
## Installation
```
git clone git@github.com:Kel0/doc_dict.git
```
```
pip install doc-dict
```
## Usage
```
from doc_dict.factory import Factory


documented_dict = Factory()

my_dict = {
    "first_name": "Mike",
    "first_name_doc": "It's name field",
    "last_name": "Anderson",
}

my_doc_dict = documented_dict.load(my_dict)

my_doc_dict["first_name"].value  # Get value of key
my_doc_dict["first_name"].doc  # Get doc of key


my_dict = {
    "first_name": "Mike",
    "last_name": "Anderson",
}
my_dict_doc = {
    "first_name": "It's name field",
}

my_doc_dict = documented_dict.load(my_dict, my_dict_doc)
my_doc_dict["first_name"].value  # Get value of key
my_doc_dict["first_name"].doc  # Get doc of key

serialized_doc_dict = documented_dict.serialize(my_doc_dict) 
```

## Types
```
doc_dict.datastructures.DocumentedValue

doc_dict.factory.Factory().load() -> Dict[str, DocumentedValue]

doc_dict.factory.Factory().serialize() -> str
```
