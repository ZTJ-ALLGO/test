
import math
import time
import sys

# 1111111111111111111111111111111111111
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

for x in range(1, 10):
    print('{0:3d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 2222222222222222222222222222222222222
import time
localtime = time.localtime()
print(time.strftime('%Y-%m-%d %a %H:%M:%S', localtime))
# git remote add my https://github.com/ZTJ-ALLGO/test.git 
# 33333333333333333333333333333333333333
# github tokey:    
# 三个"""表示的字符串，保留了全部格式
ss = ("""\
import math
import time
import sys
print('PI=%.3f' % math.pi)
a = (1,30,0xf0)
print('a[]= %02x %2x %2x' % a)
j = 0
for i in a:
    print('a[%d]=%02x' % (j, i))
    j += 1

""")

#git remote add origin https://github.com/ZTJ-ALLGO/test.git
print(ss)
print(ss.encode("utf-8"))
python_code = compile(ss, '', 'exec')
exec(python_code)
