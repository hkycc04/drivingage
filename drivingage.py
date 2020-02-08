country = input('請輸入您的國籍: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('您可以考駕照')
	else:
		print('您還不能考駕照')
elif country == '美國':
	if age >= 16:
		print('您可以考駕照')
	else:
		print('您還不能考駕照')
else:
	print('國籍僅適用台灣及美國')
