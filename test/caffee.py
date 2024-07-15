# how 2 cook coffee
# 3 stages: boil water, put water to cup, put coffee
# check stages, if skipped = bomzhih, if ok = next stage
# print coffe ready

def funkcija(arg1: str, arg2: str, arg3: str):
    """
    arg1 = Кипяченость воды

    arg2 = Налитость воды

    arg3 = Кофе

    :return: How to make coffe
    """
    bwater = arg1
    if bwater.lower() == "true":
        bwater = True
    else:
        bwater = False
    awater = arg2
    if awater.lower() == "true":
        awater = True
    else:
        awater = False
    acaffee = arg3
    if acaffee.lower() == "true":
        acaffee = True
    else:
        acaffee = False
    if bwater:
        if awater:
            if acaffee:
                print("kafa je spremna!")
            else:
                print("dodaj kafu!")
        else:
            if acaffee:
                print("BOMZHIH!")
            else:
                print("dodaj vadu!")
    else:
        if not awater and not acaffee:
            print("vruci vadu!")
        else:
            print("BOMZHIH!")


funkcija(input(), input(), input())

