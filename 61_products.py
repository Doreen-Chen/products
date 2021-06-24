# 61. 建立記帳程式專案 (+二維清單 2 dimension)
#
# 讓使用者重複輸入(購買過的)商品名稱, 不清楚購買商品種類,所以使用while loop

products = []
while True:
    name = input('請輸入商品名稱 :')
    if name == 'q':  # quit
        break
    price = input('請輸入商品價格 :')
    # Two dimension 
    #p = []
    #p.append(name)
    #p.append(price)  # line 12~14 可縮寫成第15行一行
    p = [name, price]
    #products.append(p)  # 可以直接將[name, price]取代p
    products.append([name, price])
print(products)

# 存取二維清單中指定位置
print('清單第2項商品的價格', products[1][1])

for p in products:
    print('您購買的是', p[0], ' ,價格是', p[1])    




