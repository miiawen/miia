"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
# 从模块tonglao导入Tonglao类
from tonglao import Tonglao
# 定义一个子类Xuzhu，继承父类Tonglao
class Xuzhu(Tonglao):
    # 定义read方法
    def read(self):
        print('罪过罪过！')
# 采用main方法，防止实例化部分代码被其他模块调用执行
if __name__=='__main__':
    xz=Xuzhu(200,50,150,55)
    xz.read()
