# 注释：ctr+/
# 缩进：ctr+[  ctr+]

import os
import shutil           # 高级的文件、文件夹、压缩包处理模块
os.makedirs('tmp/python/fileop',exist_ok=True)
# os.remove('test.py')  # 删除文件
shutil.rmtree('tmp')    # 可以递归的删除某个目录所有的子目录和子文件 

