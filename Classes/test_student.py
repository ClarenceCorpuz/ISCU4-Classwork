def test_get_name():
    s = Student("John", "johnsmith@ycdsbk12.ca", 12)
    assert s.get_name() == "John"
