from pytest import raises

from doc_datatypes.mutable_datatypes import DocumentedDict, DocumentedList


def test_documented_list_general_cases():
    my_list = DocumentedList([1, 2, 3], ["First", "Second", "Third"])

    assert len(my_list) == 3
    del my_list[0]
    assert len(my_list) == 2
    my_list.insert(0, [1, "First"])
    assert my_list.get_with_doc(0) == "1 -> First"
    my_list.insert(3, 4)
    assert my_list.get_with_doc(3) == "4 -> no docs"
    my_list.insert(4, [5])
    assert my_list.get_with_doc(4) == "5 -> no docs"
    my_list[0] = "1"
    assert my_list.get_with_doc(0) == '"1" -> no docs'
    my_list[0] = ["1"]
    assert my_list.get_with_doc(0) == '"1" -> no docs'
    my_list.append(1)
    assert my_list.get_with_doc(-1) == "1 -> no docs"
    my_list.append([1, "My item"])
    assert my_list.get_with_doc(-1) == "1 -> My item"


def test_documented_list_case_1():
    my_list = DocumentedList([1, 2, 3], ["First", "Second", "Third"])
    assert repr(my_list) == "[1 -> First, 2 -> Second, 3 -> Third]"
    assert my_list[0] == 1
    assert my_list[1] == 2
    assert my_list[2] == 3
    assert my_list.get_with_doc(0) == "1 -> First"
    assert my_list.get_doc(0) == "First"

    my_list_second = DocumentedList([1, 2, 3], ["First", "Second"])
    assert repr(my_list_second) == "[1 -> First, 2 -> Second, 3 -> no docs]"
    assert my_list_second[0] == 1
    assert my_list_second[1] == 2
    assert my_list_second[2] == 3
    assert my_list_second.get_with_doc(2) == "3 -> no docs"
    assert my_list_second.get_doc(2) == "no docs"

    my_list_third = DocumentedList([])
    assert list(my_list_third) == []

    with raises(ValueError):
        DocumentedList([1], ["First", "Second"])


def test_documented_list_case_2():
    my_list: DocumentedList = DocumentedList(
        [[1, "First"], [2, "Second"], [3, "Third"]]
    )
    assert repr(my_list) == "[1 -> First, 2 -> Second, 3 -> Third]"
    assert my_list[0] == 1
    assert my_list[1] == 2
    assert my_list[2] == 3
    assert my_list.get_with_doc(0) == "1 -> First"
    assert my_list.get_doc(0) == "First"

    my_list_second = DocumentedList([[1, "First"], [2, "Second"], [3]])
    assert repr(my_list_second) == "[1 -> First, 2 -> Second, 3 -> no docs]"
    assert my_list_second[0] == 1
    assert my_list_second[1] == 2
    assert my_list_second[2] == 3
    assert my_list_second.get_with_doc(2) == "3 -> no docs"
    assert my_list_second.get_doc(2) == "no docs"


def test_documnted_dict_general_cases():
    my_dict = DocumentedDict({})

    assert my_dict == {}
    my_dict["name"] = "Alex"
    assert my_dict.get_with_doc("name") == '{"value": "Alex", "doc": "no docs"}'
    assert my_dict["name"] == "Alex"

    my_dict["name1"] = ["Alex", "My docs"]
    assert my_dict["name1"] == "Alex"
    assert my_dict.get_with_doc("name1") == '{"value": "Alex", "doc": "My docs"}'

    del my_dict["name1"]
    assert list(my_dict.keys()) == ["name"]


def test_documented_dict_case_1():
    my_dict = DocumentedDict({"name": "Alex"}, {"name": "Name field"})

    assert repr(my_dict) == """{'name': {"value": "Alex", "doc": "Name field"}}"""
    assert my_dict["name"] == "Alex"
    assert my_dict.get_with_doc("name") == '{"value": "Alex", "doc": "Name field"}'

    my_dict_second = DocumentedDict({"name": "Alex"}, {})

    assert repr(my_dict_second) == """{'name': {"value": "Alex", "doc": "no docs"}}"""
    assert my_dict_second["name"] == "Alex"
    assert my_dict_second.get_with_doc("name") == '{"value": "Alex", "doc": "no docs"}'

    with raises(ValueError):
        DocumentedDict({}, {"s": 1})


def test_documented_dict_case_2():
    my_dict = DocumentedDict({"name": "Alex", "name_doc": "Name field"})

    assert repr(my_dict) == """{'name': {"value": "Alex", "doc": "Name field"}}"""
    assert my_dict["name"] == "Alex"
    assert my_dict.get_with_doc("name") == '{"value": "Alex", "doc": "Name field"}'

    my_dict_second = DocumentedDict({"name": "Alex"})

    assert repr(my_dict_second) == """{'name': {"value": "Alex", "doc": "no docs"}}"""
    assert my_dict_second["name"] == "Alex"
