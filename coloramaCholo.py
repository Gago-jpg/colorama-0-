#!/usr/bin/python
from colorama import init, Fore, Back, Style


init()
while True:
    print("\n")
    print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"primero :")
    print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"segundo :")
    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\nsalir :")
    user_input = input(": ")

    if user_input == "salir":
        break
    elif user_input == "1":
        print(Fore.CYAN+Style.BRIGHT+"\nPrimero")
        print(Fore.CYAN+Style.BRIGHT+"\n\t\tconjunto vacio con entradas de usuario(append)y eliminacion(pop)")
        print(Fore.LIGHTGREEN_EX+"  ")
        u = []
        a = input("itme #1 :")
        b = input("item #2 :")
        c = input("item #3 :")
        aa = input("item#4 :")
        bb = input("item#5 :")
        cc = input("item#6 :")
        print("  ")
        #entrada de datos.
        u.append(a)
        u.append(b)
        u.append(c)
        u.append(aa)
        u.append(bb)
        u.append(cc)
        print(Fore.LIGHTYELLOW_EX+"  ")
        for i in range(len(u)):
            print(i," = ",u[i])
        #eliminar datos
        print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\ndesea eliminar algun item:")
        user_input = input(": ")
        #pop eliminar item.
        if user_input == "si":
            print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\nsolo se eliminaran 3.")
            x = int(input("elimine: " + " :"))
            y = int(input("elimine: " + " :"))
            yy = int(input("elimine: " + " :"))
            u.pop(x)
            u.pop(y)
            print(Fore.LIGHTGREEN_EX+"  ")
            for t in range(len(u)):
                print(t," = ",u[t])

        elif user_input == "no":
            break
        
        else:
            print("")

    elif user_input == "2":
        print(Fore.CYAN+Style.BRIGHT+"\nsegundo")
        print(Fore.CYAN+Style.BRIGHT+"\n\t\tutilizar insert (x,y) X=conrdenada , y = item ")
        
        a = ['audi','toyota','me','chupa','un huevo']
        print(Fore.LIGHTYELLOW_EX+"  ")
        print(a,"   ")

        print(Fore.LIGHTYELLOW_EX+" ")#color al item
        q = input("item# 1: ")
        print(Fore.LIGHTGREEN_EX+" ")#color a la coordenada
        qq = int(input("coordenada : "))
        print(Fore.LIGHTYELLOW_EX+" ")#color al item
        w = input("item# 2: ")
        print(Fore.LIGHTGREEN_EX+" ")#color a la coordenada
        ww = int(input("coordenada : "))
        print(Fore.LIGHTYELLOW_EX+" ")#color al item
        e = input("item# 3: ")
        print(Fore.LIGHTGREEN_EX+" ")#color a la coordenada
        ee = int(input("coordenada : "))
        print(Fore.LIGHTYELLOW_EX+" ")#color al item
        r = input("item# 4: ")
        print(Fore.LIGHTGREEN_EX+" ")#color a la coordenada
        rr = int(input("coordenada : "))

        a.insert(qq,q)
        a.insert(ww,w)
        a.insert(ee,e)
        a.insert(rr,r)

        print(Fore.LIGHTRED_EX+Style.BRIGHT+"      ")#color al conjunto
        for i in range(len(a)):
            print(i,a[i])
         

    else:
        print("")
