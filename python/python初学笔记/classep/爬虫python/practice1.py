import re
# email = input('请输入你的qq邮箱')
# ex_email = re.compile(r'^[1-9][0-9]{5,12}@qq\.com')
# result = ex_email.match(email)
# if result:
#     print('输入正确')
# else:
#     print('输入错误')


phone = input('请输入你的手机号:')
ex_phone = re.compile(r'^[1][0-9]{10}')
result = ex_phone.match(phone)
if result:
    print('输入正确')
else:
    print('输入错误')