from cmath import sqrt

#rownanie kwadratowe
list = input("<a> <b> <c>\n").strip().split()
if len(list) != 3:
    print("err")
else:
    a = b = c = 0
    try:
        a = int(list[0])
        b = int(list[1])
        c = int(list[2])
        if a == 0:
            print("err a=0")
        else:
            delta = (b**2) - (4*a*c)
            if delta == 0:
                res = -b/(2*a)
                print("Rozwiazanie: {}".format(res))
            else:
                res1 = (-b-sqrt(delta))/(2*a)
                res2 = (-b+sqrt(delta))/(2*a)
                print("Rozwiazania: {} i {}".format(res1, res2))
    except ValueError:
        print("err")
    

