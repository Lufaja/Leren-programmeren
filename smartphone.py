print("Hoe duur is de iPhone? :")
iphone = int(input("€"))
print("Hoe duur is de Samsung?:")
samsung = int(input("€"))
print("Hoe duur is de Zenfone?:")
zenfone = int(input("€"))


budget = 900
def sorteer():
    if samsung > zenfone > iphone:
        print(prijzen("iPhone", "Samsung", "Zenfone", iphone, samsung, zenfone))
    elif zenfone > samsung > iphone:
        print(prijzen("iPhone", "Zenfone", "Samsung", iphone, zenfone, samsung))
    elif samsung > iphone > zenfone:
        print(prijzen("Zenfone", "Samsung", "iPhone", zenfone, samsung, iphone))
    elif zenfone > iphone > samsung:
        print(prijzen("Samsung", "Zenfone", "iPhone", samsung, zenfone, iphone))
    elif iphone > zenfone > samsung:
        print(prijzen("Samsung", "iPhone", "Zenfone", samsung, iphone, zenfone))
    elif iphone > samsung > zenfone:
        print(prijzen("Zenfone", "iPhone", "Samsung", zenfone, iphone, samsung))

def prijzen(goedkoopNaam, duurNaam, tussenNaam, goedkoop, duur, tussen):
    return f"De {duurNaam} is het duurst, de telefoon kost: {duur} Euro\nDe {goedkoopNaam} is het goedkoopst, de telefoon kost: {goedkoop} Euro\nDe {tussenNaam} zit er tussenin met: {tussen} Euro"

if iphone > budget and samsung > budget and zenfone > budget:
    if zenfone == iphone or zenfone == samsung or samsung == iphone:
        pass
    else:
        sorteer()
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur")
elif zenfone <= iphone - 100 and zenfone <= samsung - 100 and zenfone <= budget or samsung>budget<iphone and zenfone<=budget:
    verschil = samsung - zenfone
    verschil1 = iphone - zenfone
    sorteer()
    print(f"Het advies is dus de Zenfone te kopen. Deze is namelijk {verschil} euro goedkoper dan de Samsung en {verschil1} euro goedkoper dan de iPhone")
elif samsung < iphone <= samsung + 50 and iphone <= budget:
    verschil = iphone - samsung
    sorteer()
    if zenfone > iphone:
        verschil1 = zenfone - iphone
        print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {verschil} euro duurder dan de Samsung en {verschil} euro goedkoper dan de Zenfone")
    else:
        verschil1 = iphone - zenfone
        print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {verschil} euro duurder dan de Samsung en {verschil} euro duurder dan de Zenfone")
elif iphone < samsung:
    verschil = samsung - iphone
    sorteer()
    if zenfone > iphone:
        verschil1 = zenfone - iphone
        print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {verschil} euro goedkoper dan de Samsung en {verschil} euro goedkoper dan de Zenfone")
    else:
        verschil1 = iphone - zenfone
        print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {verschil} euro goedkoper dan de Samsung en {verschil} euro duurder dan de Zenfone")
elif iphone > samsung:
    verschil = iphone - samsung
    sorteer()
    if zenfone > samsung:
        verschil1 = zenfone - samsung
        print(f"Het advies is dus de samsung te kopen. Deze is namelijk {verschil} euro goedkoper dan de iPhone en {verschil} euro goedkoper dan de Zenfone")
    else:
        verschil1 = samsung - zenfone
        print(f"Het advies is dus de samsung te kopen. Deze is namelijk {verschil} euro goedkoper dan de iPhone en {verschil} euro duurder dan de Zenfone")
elif iphone == samsung:
    print(f"Het advies is dus de iPhone te kopen.")