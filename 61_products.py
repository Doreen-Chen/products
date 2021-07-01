# 61. 建立記帳程式專案 (+二維清單 2 dimension)
# & 62. 寫入檔案
# & 63. 型別轉換提點
# & 64. 寫入欄位名稱 + 編碼問題
# & 65. 讀取檔案 + split()
# & 66. Continue - 跳過欄位名稱
# & 67. 檢查檔案在不在
#
# 讓使用者重複輸入(購買過的)商品名稱, 不清楚購買商品種類,所以使用while loop

import os  # operating system 作業系統


products = []
#67. 檢查檔案在不在
if os.path.isfile('products.csv'):  #非工作目錄要給絕對路徑
    print('file exists!')

    ### 將原來在 '讓使用者輸入' while迴圈前的'65. 讀取檔案'移到檢查檔案的If內

    #####  65. 讀取檔案 + split()
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            # 66. Continue - 跳過欄位名稱
            if '商品,價格' in line:
                continue  # 跳過欄位名稱, 下一筆
            ### 原始寫法
            #s = line.strip().split(',')  ### split 切割後是清單(s)
            #name = s[0]
            #price = s[1]
            ### 快寫法
            name, price = line.strip().split(',')
            #print('商品:' + name + ' 價格:' + price)
            products.append([name, price])  # 加進list裡
    print(products)

else:
    print('No such file : products.csv')


# 讓使用者輸入
while True:
    name = input('請輸入商品名稱 :')
    if name == 'q':  # quit
        break
    price = input('請輸入商品價格 :')
    price = int(price) # 63 型別轉換:這裡轉換成數字
    # Two dimension 
    #p = []
    #p.append(name)
    #p.append(price)  # line 12~14 可縮寫成第15行一行
    p = [name, price]
    #products.append(p)  # 可以直接將[name, price]取代p
    products.append([name, price])
print(products)

# 存取二維清單中指定位置
print('清單第2項商品的價格', str(products[1][1]))

# 印出所有購買記錄
for p in products:
    #print('您購買的是', p[0], ', 價格是', p[1])
    print('您購買的是', p[0], ', 價格是', str(p[1])) # 價格已在置入list時換成int型態

# 補充:字串的加法及乘法
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'


#####  62. 寫入檔案
#    參考 52. 讀取檔案
#####  64. 寫入欄位名稱 + 編碼問題
#    檔案寫入跟讀取都與編碼有關 
#       (到課程64, open('w') 是寫入新的檔案,原始資料會被覆蓋,所以課程65在讓使用者輸入前,先讀取檔案 )
#    在開檔open()時, 要指定編號 UTF-8

# 寫入檔案-(1) txt
with open('products.txt', 'w') as f:
    for p in products:
        f.write('商品 : ' + p[0] + ', 價格是 ' + str(p[1]) + '\n') # 價格已在置入list時換成int型態

# 寫入檔案-(2) csv
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')  # 64. 寫入欄位名稱 + 編碼問題
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') # 價格已在置入list時換成int型態