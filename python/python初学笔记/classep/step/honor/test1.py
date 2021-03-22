from random import randint
def resume():
    """
    回复魔法值 返回值测试
    :return: 喝药之后回复的魔法值
    """
    incr_point = randint(50,100)



    hp_point = randint(20,100)
    return incr_point,hp_point
print(resume()[0],resume()[1])


#一些注释
# def choHero(cho):
#     return {
#         '1' : ss1,
#         '2' : cxj,
#     }.get(cho,'non')

# LastHero = choHero(input('请输入你选择的英雄:1、孙尚香 2、程咬金'))
# print(LastHero)
# print(LastHero.skills)
# #随机选择了对手
# your_enemy = your_Enemy()
# print(your_enemy)
# print(your_enemy.skills)

# def main():
#     print('--------------------欢迎来到王者荣耀模拟对战系统---------------------')
#     #选择英雄
#     LastHero = choHero(input('请输入你选择的英雄:1、孙尚香 2、程咬金'))
#     print(LastHero)
#     print(LastHero.skills)
#     #随机出现敌人
#     your_enemy = your_Enemy()
#     print(your_enemy)
#     print(your_enemy.skills)


# if __name__ == '__main__':
# #     main()
#------------------------------------------sapcefight
# m1 = Monster('地狱魔兽',200,money = 40,attack = 45)
# m2 = Monster('邱扬',320,money= 60,attack = 40)
# m3 = Monster('黄志新')
# Mon_list = [m1,m2,m3]
# the_mon = choice(Mon_list)
# R = RedLotus()
# print(R)
# the_mon.Fir_attack(R)
# print(R)
# fight_round = 1
# def get_hero_skills(hero,cho):
#     return{
#         '1':hero.skills[0],
#         '2':hero.skills[1],
#         '3':hero.skills[2],
#     }.get(cho,'non')

# while R.alive and the_mon.m_isAlive():
#     print('----第%02d回合--------'%fight_round)
#     print('%s对%s使用了%s,造成了%d的伤害'%(the_mon.name,R.name,the_mon.skill,the_mon.Fir_attack(R)))
#     cho = input('请输入你释放的技能选项:1.%s\t2.%s\t3.%s'%(R.skills[0],R.skills[1],R.skills[2]))
#     if cho == '1':
#         print('%s对%s使用了%s,造成了%d伤害'%(R.name,the_mon.name,R.skills[0],R.common_Attack(the_mon)))
#     elif cho == '2':
#         if R.small_Attack(the_mon):
#             print('%s对%s使用了%s' % (R.name, the_mon.name, R.skills[1]))
#         else:
#             print('%s对%s使用了%s,造成了%d伤害' % (R.name, the_mon.name, R.skills[0], R.common_Attack(the_mon)))
#     elif cho == '3':
#         if R.big_Attack(the_mon):
#             print('%s对%s使用了%s' % (R.name, the_mon.name, R.skills[2], R.small_Attack(the_mon)))
#         else:
#             print('蓝量不足_释放技能失败')
#     display_info(R, the_mon)
#     fight_round += 1
#     time.sleep(2)
#
# if R.alive:
#     R.hero_add_exp(the_mon)
#     print('%s成功打败了%s,获得了%d金币,%d经验'%(R.name,the_mon.name,the_mon.money,the_mon.exp))
# print(R)
#---------------------------------------------------------------------------------
