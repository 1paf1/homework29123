n = float(input("Введіть число в метрах:"))
choice = input("Оберіть одиницю вимірювання (1 - милі, 2 - дюйми, 3 - ярди): ")
if choice == 1:
    print(n / 1.609344)
elif choice == 2:
    print(n / 0.0254)
else:
    print(n / 0.9144)
