# 定义函数fight实现游戏逻辑
# 敌人的血量和攻击力使用传参方式定义
def fight(enemy_hp,enemy_power):
#定义变量存放数据
    my_hp=1000
    my_power=200
    # 使用循环来实现多回合战斗逻辑
    while True:
        my_hp=my_hp-enemy_power
        enemy_hp=enemy_hp-my_power
        if my_hp <= 0:
            print(f"我的剩余血量为：{my_hp}",f"敌人的剩余血量为：{enemy_hp}")
            print ("我输了")
            # 满足条件就跳出循环体，避免死循环
            break
        elif enemy_hp <= 0:
            print(f"我的剩余血量为：{my_hp}", f"敌人的剩余血量为：{enemy_hp}")
            print("我赢了")
            # 满足条件就跳出循环体，避免死循环
            break


if __name__ == "__main__":
     # 用列表推导式生成hp
    hp=[x for x in range(990,1020)]
    #  导入random库
    import random
    #  使用random来随机取敌人的血量
    enemy_hp= random.choice(hp)
    #  使用randint方法随机取敌人的攻击力
    enmy_power=random.randint(190,210)
    # 调用fight函数，传入敌人血量和攻击力
    fight(enemy_hp,enmy_power)