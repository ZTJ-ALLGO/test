import re

phone = "2004-959-559 # 这是一个国外电话号码"
# phone = "2004-959-559 #"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

r = re.findall('\d+','111aaa222bbb333ccc')  #提取
print(r)

r = re.split(',','111,222,333')     #分割
print(r)

r='111,222,333'
r=r.split(',')
print(r)