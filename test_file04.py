class Test_a():

    def test_sum_01(self):
        a = 10
        b = 20
        sum = a + b
        if sum == 30:
            assert True
        else:
            assert False