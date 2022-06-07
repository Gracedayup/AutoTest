import mock


class TestMock:
    def add(a, b):
        return a + b

    def test2(self):
        add = mock.Mock(return_value=12, side_effect=TestMock().add(1, 3))
        result = add(5, 10)
        print(result)
        assert result == 10


if __name__ == '__main__':
    TestMock().test2()

