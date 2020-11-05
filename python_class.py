"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""
# 1.定义一个公司员工类
class Staff:
    # 定义一个构造函数，赋予员工属性：工号，姓名，年龄，性别，职位
    def __init__(self,num,name,age,gender,position):
     self.num=num
     self.name=name
     self.age=age
     self.gender=gender
     self.position=position
    # 定义方法：工作
    def work(self):
        print('加油！打工人！！')
    # 定义方法：休息
    def rest(self):
        print('休息是为了更好的打工')
# 实例化类，员工”张三“
# zs=Staff('10001','zhangsan',25,'male','leader')
# print(zs.name)
# print(zs.age)
# zs.work()
# zs.rest()

# 2.定义一个水果类
class Frult:
     # 定义构造函数，赋予类属性:名称，颜色，价格
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
#   定义方法：零售
    def sale(self):
        print('零售不打折')
    #      定义方法：批发
    def wholesale(self):
        print('批发可打8折')
#  水果类的实例化：苹果
# apple=Frult('apple','red',5)
# print(apple.name)
# apple.sale()

# 3.定义一个衣服类
class Clothes:
    # 定义构造函数，赋予类属性:分类，尺码，季节，材料
    def __init__(self,fenlei,size,season,material):
        self.fenlei=fenlei
        self.size=size
        self.season=season
        self.material=material
    # 定义方法：穿戴
    def wear(self):
        print('这个衣服真好穿')
    # 定义方法：清洗
    def wash(self):
        print('请注意：羊毛材质不能机洗')
#  实例化类，裙子
# skirt=Clothes('女装','小码','冬装','羊毛')
# print(f'这件裙子材料为{skirt.material},不可机洗')
# skirt.wear()

# 4.定义一个咖啡类
class Coffee:
 # 定义构造函数，赋予属性：口味，甜度，温度
    def __init__(self,taste,sweet,temp):
        self.taste=taste
        self.sweet=sweet
        self.temp=temp
    # 定义方法：点单
    def order(self):
        print('你已下单成功')
    #  定义方法：配送
    def delivery(self):
        print('你的咖啡正在配送中')
#  实例化类
# cf=Coffee('卡布奇诺','少糖','hot')
# print(cf.sweet)
# cf.order()

# 5.定义一个手机类
class Phone:
#     定义构造函数，赋予属性：操作系统，内存，分辨率，屏幕尺寸
    def __init__(self,system,ram,resolution,screen):
        self.system=system
        self.ram=ram
        self.resolution=resolution
        self.screen=screen
    # 定义方法：开机
    def power_on(self):
        print('欢迎使用')
    # 定义方法：关机
    def power_off(self):
        print('是否确认要关机？')
# 实例化类
# iphone_xs_max=Phone('ios','256G','2688*1242','6.5英寸')
# print(f'iphone xs max 的分辨率为：{iphone_xs_max.resolution}')
# iphone_xs_max.power_off()

















