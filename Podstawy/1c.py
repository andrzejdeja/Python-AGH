print("Zamek")
code = ""
while True:
    print("Podaj nowy kod")
    code = input()
    if code.isnumeric():
        break
    else:
        print("err")
print("=======================")
while True:
    print("Podaj kod")
    ans = input()
    if ans == code:
        print("Poprawny kod")
        break
    else:
        print("Niepoprawny kod")
