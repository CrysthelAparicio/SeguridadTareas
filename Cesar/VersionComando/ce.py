import sys

TAM_MAX_CLAVE = 26

def menuPrincipal():
 while True:
  print("========= CIFRADO CESAR ========== ")
  #print("== a) Cifrar                    == ")
  #print("== b) Decifrar                  == ")
  print("== c) Decifrar por fuerza bruta == ")
  print("== x) Salir                     == ")
  opcion = input().lower();
  if opcion in "a,b,c,x".split(','):
   return opcion

def obtenerMensaje():
 print('Ingresa tu mensaje:')
 return input()

def obtenerClave():
    clave = 0
    while True:
     print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
     clave = int(input())
     if(clave >= 1 and clave <= TAM_MAX_CLAVE):
      return clave


def traducirMensaje(opcion, mensaje, clave):
 if opcion == 'b':
  clave = -clave
 traduccion = ''

 for simbolo in mensaje:
  if simbolo.isalpha():
   num = ord(simbolo)
   num += clave

   if simbolo.isupper():
    if num > ord('Z'):
     num -= 26
    elif num < ord('A'):
     num += 26
   elif simbolo.islower():
    if num > ord('z'):
     num -= 26
    elif num < ord('a'):
     num += 26
   traduccion += chr(num)
  else:
   traduccion += simbolo
 return traduccion


def main():
    if(sys.argv[1] == "help"):
        print("\tBienvenido al encriptador de Cesar\n\nPara correr un comando solo necesita poner la clave antes qu el texto entre comillas dobles, ejemplo:")
        print(">python3 ce.py 3 \"meet me after the toga party\"")
        print("\nEl resultado de encriptacion es: phhw ph diwhu wkh wrjd sduwb")
    else:
        print(traducirMensaje('c', sys.argv[2], int(sys.argv[1])));


if __name__ == "__main__":
 main()