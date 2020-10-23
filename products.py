import os #載入作業系統

#讀取檔案
def read_file(filename):
	products = [] #不管是否讀取到檔案，都得先有空清單，否則下面代碼(讓使用者輸入/寫入檔案）時無法使用空清單
	with open(filename, 'r', encoding = 'utf-8') as f: 
		for line in f:
			if '商品,價格' in line:
				continue #繼續（跳過這回，繼續下一回）
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
	return products

#使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		products.append([name, price])
	print(products)
	return products

#列出所有購買紀錄
def print_file(products):
	for p in products:
		print(p[0], '的價格為', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('找到檔案了！')
		products = read_file(filename)
	else:
		print('找不到檔案')
	
	products = user_input(products)
	print_file(products)
	write_file(filename, products)

main()