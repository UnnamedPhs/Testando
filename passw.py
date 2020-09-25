import string
import secrets

red = '\033[0;31m'
end = '\033[0;0m'

trace = '-'*50

print (f'\n{red}{trace}{end}')
digits = int(input('How Many Digits: '))
key = string.ascii_letters + string.digits
password = ''.join(secrets.choice(key)
for passoword in range(digits))
print ()
print (f'Password:{password}')
print (f'{red}{trace}{end}\n')
