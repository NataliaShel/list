# завдання 1
name=str(input("Enter your name:"))
lastname=str(input("Enter your last name:"))
phone=int(input("Enter your phone number:"))
street=str(input("Enter the name of your street:"))
house=int(input("Enter the house number:"))
apartment=int(input("Enter your apartment number:"))
city=str(input("Enter the name of your city:"))
zipcode=int(input("Enter your zip code:"))
country=str(input("Enter the name of your country:"))

print(name, lastname)
print(phone)
print('Str.',(street),(house),", ap.",(apartment),',',(city))
print(zipcode)
print(country)

# завдання 2
x = float(input("Введіть значення магнітуди: "))
if 0 < x < 2:
    print("Дескриптор: Micro")
elif 2 <= x < 3:
    print("Дескриптор: Very minor")
elif 3 <= x < 4:
    print("Дескриптор: Minor")
elif 4 <= x < 5:
    print("Дескриптор: Light")
elif 5 <= x < 6:
    print("Дескриптор: Moderate")
elif 6 <= x < 7:
    print("Дескриптор: Strong")
elif 7 <= x < 8:
    print("Дескриптор: Major")
elif 8 <= x < 10:
    print("Дескриптор: Great")
else:
    print("Дескриптор: Meteoric") 

# завдання 3
while(True):
    a = int(input('Введіть число a:'))
    if 0 < a :
        break
    else:
        print("Помилка,правильно введіть дані")  
if 0 < a < 50:
    print("Вам доведеться сплатити 100 грн")
elif 50 < a < 100:
    print('Вам доведеться сплатити 150 грн')
else:
    x=a-100
    print("Вам доведеться сплатити" , 2*x+150, 'грн')

# завдання 4
products_list = [29.25, 48.99, 99.98, 124.30, 214.30, 543.90, 799.85]
products_list_zn=[value * 0.4 for value in products_list] 
products_list_zn_okr=[round(v,2) for v in products_list_zn]
print(str(products_list)[1:-1])
print(str(products_list_zn_okr)[1:-1])

# завдання 5
list_a = []
n = int(input("Ведіть кількість елементів які добавите в список: "))
if n < 0:
     print('Дані введено не правильно.')
else:
     for k in range(n):
         elm = input("Введіть елемент текстом:")
         list_a.append(elm)
if n == 1:
     print(f'{list_a[0]}')
elif n == 2:
     print(f'{list_a[0]} and {list_a[1]}')
else:
     joined_string = " ,".join(list_a)
     print(f'{list_a[:n-1]}, and {list_a[-1]}')
