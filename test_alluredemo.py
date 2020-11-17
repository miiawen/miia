import allure   #导入allure模块
import pytest   #导入pytest模块
import yaml

from miia.core.calc import Calc


class TestCalc:
    #使用setup实例化Calc类
    def setup_class(self):
        print("setup_class")
        self.calc = Calc()
    # 优先执行，会override实例方法
    @classmethod
    def setup_class(cls):
        print("setup_class classmethod")

        cls.calc = Calc()

    def setup(self):
        pass

    @allure.step
    def simple_step(self, step_param1, step_param2=None):
        pass
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1]

    ])
    def test_mul(self, a, b, c):
        self.simple_step(f'{a} {b} {c}')
        assert self.calc.mul(a, b) == c
        # assert calc.mul(-1, -1) == 1
        # assert calc.mul(1, -1) == 1

    # # 正常值例子
    @pytest.mark.parametrize('a, b, c', [
        [2, 2, 1],
        [0.2, 0.1, 2],
        [0, 2, 0]
     ])

    def test_div_data(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常值例子
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0]
    ])
    def test_div(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 流程示例
    def test_process(self):
        r1 = self.calc.mul(1, 2)
        r2 = self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2