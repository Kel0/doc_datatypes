from doc_dict.factory import documented_dict


def test_documented_dict():
    my_dict = {
        "first_name": "Mike",
        "first_name_doc": "It's name field",
        "last_name": "Anderson",
    }

    my_doc_dict = documented_dict(my_dict)
    assert my_doc_dict["first_name"].value == "Mike"
    assert my_doc_dict["first_name"].doc == "It's name field"
    assert my_doc_dict["last_name"].value == "Anderson"
    assert my_doc_dict["last_name"].doc == "no docs"

    my_dict = {
        "first_name": "Mike",
        "last_name": "Anderson",
    }
    my_dict_doc = {
        "first_name": "It's name field",
    }

    my_doc_dict = documented_dict(my_dict, my_dict_doc)
    assert my_doc_dict["first_name"].value == "Mike"
    assert my_doc_dict["first_name"].doc == "It's name field"
    assert my_doc_dict["last_name"].value == "Anderson"
    assert my_doc_dict["last_name"].doc == "no docs"

    my_doc_dict = documented_dict(my_dict, {})
    assert my_doc_dict["first_name"].value == "Mike"
    assert my_doc_dict["first_name"].doc == "no docs"
    assert my_doc_dict["last_name"].value == "Anderson"
    assert my_doc_dict["last_name"].doc == "no docs"

    my_doc_dict = documented_dict(my_dict, {})
    assert my_doc_dict["first_name"].value == "Mike"
    assert my_doc_dict["first_name"].doc == "no docs"
    assert my_doc_dict["last_name"].value == "Anderson"
    assert my_doc_dict["last_name"].doc == "no docs"
