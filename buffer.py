"""
buffer.py 文件读写缓冲机制演示

缓冲刷新条件：
1. 缓冲区满了
2. 行缓冲换行时会自动刷新
3. 程序运行结束或者文件close关闭
4. 调用flush()函数
"""

f = open('test','w',1)  # 1表示行缓冲

while True:
    data = input(">>")
    if not data:
        break
    f.write(data)
    f.flush()  #　刷新缓冲

f.close()
