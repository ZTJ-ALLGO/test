import json
#!/usr/bin/python3
'''
注释 CTRL+/
'''
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}

json_obj = json.dumps(data)
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_obj)

json_dit=json.loads(json_obj)
print("json str:",json_dit)
# --------------------------------------
# --------------------------------------
def fun(a,b):
    #"返回多个值，结果以元组形式表示"
    return a,b,a+b,100,"asc"

print("多值返回:",fun(1,2))
