# *********
# Cesar es un cifrado de sustitución, su algoritmo es el siguiente:
# - Tomar mensaje alfabético (de la A a la Z)
# - Tome una clave (1 a 26) (1 es A y 26 es Z)
# - Para cifrar, mensaje de desplazamiento hacia la izquierda o hacia la derecha letra por 
# letra por el valor de la clave
# Por ejemplo
# si el mensaje es "ABC" y la clave es 1 y estamos realizando un desplazamiento a la derecha, 
# el texto cifrado será A + 1 = B, B + 1 = C, C + 1 = D. ABC = BCD, BCD siendo texto cifrado.
# - Para descifrar, desplazar hacia la izquierda o hacia la derecha el mensaje letra por letra opuesto 
# al desplazamiento realizado 

# cifrado por el valor de la clave
# Por ejemplo
# si el texto cifrado es "BCD" y la clave es 1 y estamos realizando un desplazamiento hacia la izquierda,
#  el texto cifrado será B-1 = A,

# C-1 = B, D-1 = C. BCD = ABC, ABC siendo texto descifrado.
# *********


def encryption():
    print("Cifrada")

    print("El mensaje solo puede ser alfabeto en mayúsculas o minúsculas")
    msg = input("Ingresa el mensaje: ")
    key = int(input("Introducir Clave(0-25): "))  # basado en 26 letras del alfabeto

    encrypted_text = ""

    for i in range(len(msg)):
        if ord(msg[i]) == 32:  # ord() nos dará el ASCII de space char, que es 32
            encrypted_text += chr(ord(msg[i]))  # chr() convertirá ASCII de nuevo a carácter

        elif ord(msg[i]) + key > 122:
            # después de 'z', vuelva a 'a', 'a' = 97, 'z' = 122
            temp = (ord(msg[i]) + key) - 122  # restando 122 para obtener un int más bajo y sumándolo en 96
            encrypted_text += chr(96+temp)

        elif (ord(msg[i]) + key > 90) and (ord(msg[i]) <= 96):
            # volviendo a 'A' después de 'Z'
            temp = (ord(msg[i]) + key) - 90
            encrypted_text += chr(64+temp)

        else:
            # en caso de letras entre a-z y A-Z
            encrypted_text += chr(ord(msg[i]) + key)

    print("Encriptado: " + encrypted_text)


def decryption():
    print("Descifrada")

    print("El mensaje solo puede ser alfabeto en mayúsculas o minúsculas")
    encrp_msg = input("Ingrese texto cifrado: ")
    decrp_key = int(input("Introducir Clave(0-25): "))

    decrypted_text = ""

    for i in range(len(encrp_msg)):
        if ord(encrp_msg[i]) == 32: # ord() nos dará el ASCII de space char, que es 32
            decrypted_text += chr(ord(encrp_msg[i])) # chr() convertirá ASCII de nuevo a carácter

        elif ((ord(encrp_msg[i]) - decrp_key) < 97) and ((ord(encrp_msg[i]) - decrp_key) > 90):
            # resto la clave de la letra ASCII y agregue 26 al número actual
            temp = (ord(encrp_msg[i]) - decrp_key) + 26
            decrypted_text += chr(temp)

        elif (ord(encrp_msg[i]) - decrp_key) < 65:
            temp = (ord(encrp_msg[i]) - decrp_key) + 26
            decrypted_text += chr(temp)

        else:
            decrypted_text += chr(ord(encrp_msg[i]) - decrp_key)

    print("Texto Desencriptado: " + decrypted_text)


def main():
    choice = int(input("1. Cifrada\n2. Descifrada\nEscoja(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("No me entendio? es 1 o 2")


if __name__ == "__main__":
    main()