# -*- coding: utf-8 -*-

f = open('fread1.py', 'r')
data1 = f.read()  # ファイル全部を1つの文字列に読み込む
f.close()


# 改行マークで分割
lst = data1.split('\n') 

# 行番号つけて表示してみる
lno = 1
for l in lst:
    print ('%03d: ' % (lno), l)
    lno += 1
