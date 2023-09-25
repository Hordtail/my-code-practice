diccionario = {
    "A": "4",
    "B": "13",
    "C": "[",
    "D": ")",
    "E": "3",
    "F": "|=",
    "G": "&",
    "H": "#",
    "I": "1",
    "J": ",_|",
    "K": ">|",
    "L": "1",
    "M": "JVI",
    "N": "^/",
    "O": "0",
    "P": "|*",
    "Q": "(_,)",
    "R": "I2",
    "S": "5",
    "T": "7",
    "U": "(_)",
    "V": "|/",
    "W": "\/\/",
    "X": "><",
    "Y": "j",
    "Z": "2",
    "1": "L",
    "2": "R",
    "3": "E",
    "4": "A",
    "5": "S",
    "6": "b",
    "7": "T",
    "8": "B",
    "9": "g",
    "0": "o",

}


def conversor(text):
    traducido = ""

    for i in text.upper():
        if i.isdigit() and i in diccionario:
            traducido += diccionario[i]
        elif i.isalpha() and i in diccionario:
            traducido += diccionario[i]
        else:
            traducido += i
    return traducido


print("Conversor a Hacker:")
text = input("Introduce el texto a convertir:")
traducido = conversor(text)
print(traducido)
