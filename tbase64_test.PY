'''
base64是使用 A-Z,a-z,0-9,+,/这64个字符来表示任意二进制数据，一般用来对路径（url）进行编码，将非ASCII码的
字符数据转换为ASCII码。将不可打印的二进制数据转换为可以打印的字符串
'''
# ------------对二进制进行编码解码-----------------------
import base64
ss = ("base64是使用 A-Z,a-z,0-9,+,/这64个字符来表示任意二进制数据，一般用来对路径（url）进行编码，"
      "将非ASCII码的字符数据转换为ASCII码。将不可打印的二进制数据转换为可以打印的字符串"
      )
sss="中国"
print(type(sss))
aaa = ss.encode()  # 二进制
print("aaa="+str(aaa))
result = base64.b64encode(aaa)  # 使用base64编码
print("-------------------------------------------")
print(result)
bbb = base64.b64decode(result)
print(bbb.decode())
