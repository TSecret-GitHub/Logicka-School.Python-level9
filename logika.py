name = input("Привет, как тебя зовут?")
print("Привет, [Человеко-Имя: " + name +"]")

password = input("Снова привет, теперь мы хотим заб... в смысле - проверить твой пароль: ")

symbols = len(password)

sympols_veroyatnost = 70**symbols
str(sympols_veroyatnost) 

print("Вариантов пароля: ")
print(sympols_veroyatnost)