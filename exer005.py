def inverter_string(string):
    string_invertida = ""

    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida

entrada = input("Informe uma string: ")

resultado = inverter_string(entrada)

print(f"String invertida: {resultado}")
