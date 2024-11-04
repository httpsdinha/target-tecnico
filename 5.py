def inverter_string(texto):
    invertida = ""
    for char in texto:
        invertida = char + invertida
    return invertida


texto = input()
print("String invertida:", inverter_string(texto))
