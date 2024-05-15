a = int(input('Введите длину '))
b = int(input('Введите ширину '))
c = int(input('Размер куска '))
if c < a*b and (c%a==0 or c%b==0):
 print(True)
else:
 print(False);
