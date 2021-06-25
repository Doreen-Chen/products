# 61. 建立記帳程式專案 (+二維清單 2 dimension)
# & 62. 寫入檔案
# & 63. 型別轉換提點
#
# 讓使用者重複輸入(購買過的)商品名稱, 不清楚購買商品種類,所以使用while loop

products = []
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
#    在開檔open()時, 要指定編號 UTF-8

# (1) txt
with open('products.txt', 'w') as f:
    for p in products:
        f.write('商品 : ' + p[0] + ', 價格是 ' + str(p[1]) + '\n') # 價格已在置入list時換成int型態

# (2) csv
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')  # 64. 寫入欄位名稱 + 編碼問題
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') # 價格已在置入list時換成int型態

