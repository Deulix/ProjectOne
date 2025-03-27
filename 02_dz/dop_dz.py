import random

# 1)
print("\nHello, world!\n")

# 2)
string = "Это первая строка. \nЭто вторая строка. \nЭто третья строка.\n" 
print(string)

# 3)
name = "Артур"
print("Привет,", name, end="\n\n")

# 4)
age = 28
print(str(age + 5), "\n")

# 5)
city = "Минск"
country = "Беларусь"
print("Я живу в городе", city, ", страна", country + ".\n")

# 6)
first_name = "Артур"
last_name = "Русинов"
print(first_name + " " + last_name + "\n")

# 7)
print(f"Меня зовут {first_name} {last_name}. Мне {age} лет.\n")

# 8)
number = random.randint(0, 100)
print(f"Моё любимое число: {number}.\n")

# 9)
a = random.randint(0, 1000)
b = random.randint(0, 1000)
print(f"Сумма чисел {a} и {b} равна", str(a + b) + f". Разность между {a} и {b} равна", str(a - b) + f". Умножение чисел {a} и {b} равно", str(a * b) + f". Деление числа {a} на число {b} равняется", str(round((a / b), 3)) + ".\n")

# 10)
name = input("Чтобы продолжить, введите ваше имя: ")
print(f"Привет, {name}!\n")

# 11)
product = 'Батончик "Snickers"' 
price = "3"
print(f"Товар: {product}, цена: {price} руб.\n")

# 12)
print('"""\n',  string, '\n"""\n', sep = "")

# 13)
print("Python", "это", "круто", sep = "-", end = "!\n")