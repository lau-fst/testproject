from testproject.lib import hello

def test_hello():
    assert(type(hello())==str)
