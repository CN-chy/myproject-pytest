class Test_User:
    def setup_class(self):
        print('setup_class')

    def teardown_class(self):
        print('teardown_class')

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('teardown_method')

    def test_user_1(self):
        assert 1 == 1
        print('test_user_1')

    def test_user_2(self):
        assert 1 == 1
        print('test_user_2')

