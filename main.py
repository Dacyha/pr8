from random import choices

lowercase ='abcdefghijklmnopqrstuvwxyz'
uppercase ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

chars = ''

pwd_length = int(input('Введите желаемую длину пароля: '))
pwd_auto = (input('Сгенерировать пароль автоматически? (y,n): ') == 'y')

for text,seq in (
		('Включить нижний регистр', lowecase),
		('Включить верхний регистр', uppercase),
	if pwd_auto or (input(text + '(y,n):') == 'y'):
	  chars += seq

password = ''.join(choices(chars, k=pwd_length))

print('\n', password, '\n', sep='')
