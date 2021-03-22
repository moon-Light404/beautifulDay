''''
for letter in 'Python':
    if letter == 'h':
        break
    print(f'当前字母{letter}')
var = 10
while var > 0 :
    print(f'当前变量值:{var}')
    var -= 1
    if var == 5:
        break
print('over')

'''

for letter in 'Python':
    if letter == 'h':
        continue
    print(f'当前字母:{letter}')
var = 10
while var > 0:
    var -= 1
    if var == 5:
        continue
    print (f'当前变量值:{var}')
print('over!')
