print("Hoe duur is de iPhone? :")
iphone = int(input("€"))
print("Hoe duur is de Samsung?:")
samsung = int(input("€"))

def prijzen(goedkoopNaam, duurNaam, goedkoop, duur):
    return f"De {duurNaam} is het duurst, de telefoon kost: {duur} Euro\nDe {goedkoopNaam} is het goedkoopst, de telefoon kost: {goedkoop} Euro"


if samsung < iphone <= samsung + 50:
    verschil = iphone - samsung
    print(prijzen("Samsung", "iPhone", samsung, iphone))
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {verschil} euro duurder dan de Samsung")
elif iphone < samsung:
    verschil = samsung - iphone
    print(prijzen("iPhone", "Samsung", iphone, samsung))
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {verschil} euro goedkoper dan de Samsung")
elif iphone > samsung:
    verschil = iphone - samsung
    print(prijzen("Samsung", "iPhone", samsung, iphone))
    print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {verschil} euro goedkoper dan de iPhone")
elif iphone == samsung:
    print(f"Het advies is dus de iPhone te kopen. Beide smartphones zijn namelijk even duur")