from calc import add

def test_add():
    # This is our "Unit Test"
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10, 12) == 23
    print("All tests passed!")

if __name__ == "__main__":
    test_add()
  
