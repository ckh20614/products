products = []
while True:
	name = input('商品名稱: ')
	if name == 'q':
		break
	price = input('商品價格: ')
	p = []
	p.append(name)
	p.append(price)   
	products.append(p)  #一行寫法: products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])