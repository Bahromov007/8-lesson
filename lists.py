cities = ['Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus','Termes','Namangan', 'Andijan']
three_cities = cities[3:6]
# print(three_cities)
reversed_cities = cities[::-1]
# print(reversed_cities)
# print('Fergana' in cities)
# print('Chirchik' in cities)
# print(cities)

# for city in cities:
#     print(city)

text = 'My name is Abdulhakim. I am 15 years old'
for letter in text:
    print(letter)

# cities = ('Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus','Termes','Namangan', 'Andijan')
# for city in cities:
#     print(city)

# print(range(10))
# (0,1,2,3,4,5,6,7,8,9)

# for num in range(10, 20, 2):
#     print(num)


# for num in range(20, 10, -1):
    # print(num)

# Iterables
# 1. lists - [] 
# 2. tuples - ()
# 3. strings - "", ''
# 4. range object()

# цикл FOR нужен для тог, чтобы прогонять через цикл интерируемые сущности

# for i in range(11):
#     print(i ** 2, i ** 3)

# for i in [0,1,2,3,4,5,6,7,8,9,10]:
#     print(i ** 2, i ** 3)

# for i in (0,1,2,3,4,5,6,7,8,9,10):
#     print(i ** 2, i ** 3)

# # acc = sum
# acc = 0
# for num in range(1,11):
#     acc = acc + num
#     print(acc)
# print(acc)

# acc = 1
# for num in range(1,11):
#     acc = acc * num
# print(acc)

# acc = 0
# for num in range(0,21,2):
#     acc = acc + num
# print(acc)

cities = ['Tashkent', 'Bukhara', 'Samarkand', 'Khorezm', 'Fergana', 'Karshi', 'Nukus','Termes','Namangan', 'Andijan']
# for i in range(5):
#     print(cities[i])

# for i in range(len(cities)):
# #     print(cities[i])

# acc = ''
# cities_len = len(cities)
# for i in range(len(cities)):
#     if i != cities_len - 1:
#         acc += cities[i] + ', '
#     else :acc += cities[i] + ', '
# print(acc)