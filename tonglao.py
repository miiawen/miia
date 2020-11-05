"""
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""
# 定义一个天山童姥类
class Tonglao:
    # 定义构造函数，进行传参：血量，攻击力，敌人血量，敌人攻击力
    def __init__(self,my_hp,my_power,enemy_hp,enemy_power):
        self.my_hp=my_hp
        self.my_power=my_power
        self.enemy_hp=enemy_hp
        self.enemy_power=enemy_power
    # 定义see_people方法，实现打印功能
    def see_people(self,name):
        # 使用if分支语句实现不同情况的打印
        if name=='无崖子':
             print('师弟！')
        elif name=='李秋水':
            print('师弟是我的！')
        elif name=='丁春秋':
            print('叛徒，我杀了你')
    # 定义fight_zms(天山折梅手)方法，实现战斗逻辑
    def fight_zms(self):
        self.my_hp=self.my_hp/2 #调用此方法时，自己的血量缩减2倍
        self.my_power=self.my_power*10 #调用方法时，自己的战斗力提升10倍
        # 计算战斗后的剩余血量
        self.my_hp=self.my_hp-self.enemy_power
        self.enemy_hp=self.enemy_hp-self.my_power
        # 使用if分支语句，判断战斗后的属于，实现不同情况的结果打印
        if self.my_hp>self.enemy_hp:
            print(f'我的剩余血量为:{self.my_hp},敌人的剩余血量为{self.enemy_hp}')
            print('我赢了！')
        elif self.my_hp<self.enemy_hp:
            print(f'我的剩余血量为：{self.my_hp},敌人的剩余血量为：{self.enemy_hp}')
            print('我输了')
# 为了防止实例化部分代码被其他模块调用执行，采用main方法
if __name__=='__main__':
 # 实例化天山童姥类，采用传参的方式
 tl=Tonglao(200,50,120,55)
# 实例调用fight_zms方法
 tl.fight_zms()
# 传参调用see_people方法
 tl.see_people('无崖子')