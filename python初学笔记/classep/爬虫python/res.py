import re
# match只在开头匹配
print(re.match('abc','abcabcd'))
print(re.match('abc','abcabcd'))
print(re.search('a','abcda'))
print(re.findall('a','abcda'))

#
# # print(re.search((r'^ab'),'aabcdef'))#匹配某个字符开头
# # print(re.search((r'.com$'),'abcdab@qq.com'))
# # print(re.search((r'.ad'),'abcadabcd'))
# # print(re.search((r'[Pp]ython'),'I like aython'))
# # print(re.search((r'[^Pp]ython'),'I like aython'))
# # print(re.search((r'ca*b'),'bbbcbaaaaaab'))
# # print(re.search((r'ca+b'),'bbbcbcaaaaab'))
# # print(re.search((r'ca?b'),'bbbcabcaaaaaab'))
#
# s = 'aa11aa,bb22,cc33,dd44dd,ee55ff'
# searchObj = re.search((r'([a-z]+)\d+([a-z]+)'),s)
# print(searchObj.group(0))
# print(searchObj.group(1))
# print(searchObj.group(2))
#
# s1 = '6807234@qq.com'
# sObj = re.search((r'(\d+)@qq\.com$'),s1)
# print(sObj)
# print(sObj.group())

phone = '2004-945-568'
num1 = re.sub(r'#.$','',phone)
print(num1)
num2 = re.sub(r'\D','',phone)
print(num2)
