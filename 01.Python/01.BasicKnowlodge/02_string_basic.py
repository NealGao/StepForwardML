# 字符串
# 字符串单引号''或者是双引号""
# r''表示''内部的字符串默认不转义
# 如果字符串内部有很多换行，用 \n 写在一行不好阅读，可以用'''...''' 的格式表示多行内容。

#布尔值
# True False 严格区分大小写

# Python 整数除法是精确的
# / 除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数。
# // 地板除法（只取结果的整数部分）
# % 取余
# Python的整数没有大小限制
# Python的浮点数也没有大小限制，但超出一定范围就直接表示为inf(无限大)

# 字符编码
# 单个字符 ord()获取字符的整数表示，chr()把编码转换为对应的字符。

# Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示
# 'ABC'是字符串 ,b'ABC'
# >>> 'ABC'.encode('ascii')
# b'ABC'
# >>> '中文'.encode('utf-8')
# b'\xe4\xb8\xad\xe6\x96\x87'
# >>> '中文'.encode('ascii')
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     '中文'.encode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
# >>> b'ABC'.decode('ascii')
# 'ABC'

# 当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
































