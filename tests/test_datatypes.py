from doc_datatypes.datatypes import DocumentedIndex, DocumentedValue


def test_documented_value():
    name_value = DocumentedValue(value="Alex", doc="Name field")

    assert isinstance(name_value, DocumentedValue)
    assert name_value.value == "Alex"
    assert name_value.doc == "Name field"
    assert name_value.to_dict() == {"value": "Alex", "doc": "Name field"}
    assert repr(name_value) == '{"value": "Alex", "__doc__": "Name field"}'


def test_documented_index():
    name_index = DocumentedIndex(value="Alex", doc="Name field")

    assert name_index() == "Alex"
    assert name_index.value == "Alex"
    assert name_index.doc == "Name field"
    assert repr(name_index) == "Alex -> Name field"
