print("Podaj imię, nazwisko i date urodzenia")
ans = input("<Name> <Surname> <DOB>\n").strip().split()
if len(ans) == 3:
    print(ans)
else:
    print("err")
