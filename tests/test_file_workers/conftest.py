import pytest

cnt = 0


@pytest.fixture(autouse=True)
def clean_test_file():
    with open('testfile.txt', 'w'):
        pass
    global cnt
    print(cnt)
    cnt += 1
