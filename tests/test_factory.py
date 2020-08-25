from app.factory import documented_dict


def test_documented_value():
    my_dict = {
        "first_name": "Mike",
        "first_name_doc": "It's name field",
        "last_name": "Anderson",
    }

    my_doc_dict = documented_dict(my_dict)
    assert my_doc_dict == {
        "first_name": {"value": "Mike", "__doc__": "It's name field"},
        "last_name": {"value": "Anderson", "__doc__": "no docs"},
    }