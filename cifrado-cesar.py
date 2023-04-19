# Se sabe que el cifrado cesar es un cifrado de sustitución
# monoalfabetica que desplaza 3 caracteres adelante en el alfabeto, el 3
# funciona como una clave, sin embargo no estamos obligados a usar el 3, lo
# único que debemos tener presente, es que tanto emisor como receptor sepan
# cual es la clave (cantidad de desplazamientos).

# Se utilizará un metodo de fuerza bruta en donde iremos iterando k (la clave) hasta hallar un mensaje coherente
# Formula: M = C - [K MOD |A|] -> donde:
#     M = mensaje descifrado
#     C = Posición de la letra, del mensaje cifrado, correspondiente con el abecedario
#     K = Clave que iremos iterando
#     A = Cantidad de letras del abecedario

encode_message = "QCZW AWSMTUMTMUBM LMNMULMZ I TP UIKPWU KWU MS XWLMZ LM SI KZPXBWÑZINPI"
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
m = ""
a = 27

# Siendo K la posible clave
for k in range(0,21):
    for j in encode_message:
        if(j == " "):
            m += " "
        else:
            c = alphabet.index(j)
            m += alphabet[c - k % a]
    print(m + " - clave: " + " " + str(k))
    m = ""

# Una vez se han hecho las iteraciones con un intervalo que permita generar un mensaje coherente podemos concluir que el mensaje descifrado sería:
# JURO SOLEMNEMENTE DEFENDER A MI NACION CON EL PODER DE LA CRIPTOGRAFIA 
# Y su clave es: 8 posiciones