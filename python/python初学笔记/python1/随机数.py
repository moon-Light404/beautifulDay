'''
1.导入模块
   import random
2. 使用这个模块中的功能
   random.randint()
'''

import random

num = random.randint(0,9)

print(num)

player = int(input('请出拳：0--石头：1--剪刀：2--布'))

computer =random.randint(0,2)
print(computer)
if((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
elif player == computer:
    print('平局，再来一局')
else:
    print('电脑获胜')


