import os
f = open("serial_test.py", "r", encoding='UTF-8')
str = f.read()
f.close()

print(str)
python_code = compile(str, '', 'exec')
exec(python_code)
# print("-------------------")

