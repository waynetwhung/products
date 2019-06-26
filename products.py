products = []
# 讀取檔案
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		#跳過欄位名稱
		if '品項,價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	# p = []
	# p.append(name)
	# p.append(price)

	# p = [name, price]

	# products.append(p)

	products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print('品項 ', p[0], '的價格為 ', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('品項,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
