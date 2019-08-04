print("КАЛЬКУЛЯТОР")
print("+ - / * ")
what=input("что делаем:")
if what == "-":
	a=float(input("введите первое число:"))
	b=float(input("введите второе число:"))
	print("результат")
	print(a-b)

elif what == "+":
	a=float(input("введите первое число:"))
	b=float(input("введите второе число:"))
	print("результат")
	print(a+b)

elif what == "/":
	a=float(input("введите первое число:"))
	b=float(input("введите второе число:"))
	print("результат")
	print(a/b)



elif what == "*":
	a=float(input("введите первое число:"))
	b=float(input("введите второе число:"))
	print("результат")
	print(a*b)


else:
	print("я не знаю токого знака")
