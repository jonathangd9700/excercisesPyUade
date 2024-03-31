import random;

def randomNum():
    numero = random.randint(0,3999)
    numerosStr = str(numero)
    return numerosStr

def convertirRomano(numero):
    for i in range(len(numerosStr)):
        if i == 0:
            match numerosStr[i]:
                case "1":
                    print("M",end="")
                case "2":
                    print("MM",end="")
                case "3":
                    print("MMM",end="")
        if i == 1:
            match numerosStr[i]:
                case "1":
                    print("C",end="")
                case "2":
                    print("CC",end="")
                case "3":
                    print("CCC",end="")
                case "4":
                    print("CD",end="")
                case "5":
                    print("D",end="")
                case "6":
                    print("DC",end="")
                case "7":
                    print("DCC",end="")
                case "8":
                    print("DCCC",end="")
                case "9":
                    print("CM",end="")
        if i == 2:
            match numerosStr[i]:
                case "1":
                    print("X",end="")
                case "2":
                    print("XX",end="")
                case "3":
                    print("XXX",end="")
                case "4":
                    print("XL",end="")
                case "5":
                    print("L",end="")
                case "6":
                    print("LX",end="")
                case "7":
                    print("LXX",end="")
                case "8":
                    print("LXXX",end="")
                case "9":
                    print("XC",end="")
        if i == 3:
            match numerosStr[i]:
                case "1":
                    print("I",end="")
                case "2":
                    print("II",end="")
                case "3":
                    print("III",end="")
                case "4":
                    print("IV",end="")
                case "5":
                   print("V",end="")
                case "6":
                    print("VI",end="")
                case "7":
                    print("VII",end="")
                case "8":
                    print("VIII",end="")
                case "9":
                    print("IX",end="")
def main():
    numero = randomNum()
    convertirRomano(numero)