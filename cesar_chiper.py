import string
alphabet = list(string.ascii_uppercase) # ARMAZENANDO ALFABETO MAIUSCULO NA VARÍAVEL alphabet
print(alphabet)


def encrypt(plaintext,key): # FUNÇÃO P/ RETORNAR TEXTO CIFRADO  
  encrypt_string = ''

  for i in plaintext.upper():
    
    if i==" ":
      encrypt_string=encrypt_string+i
    else:
      index_char_chipertxt = (alphabet.index(i.upper()) + key)%26
      encrypt_string=encrypt_string+alphabet[index_char_chipertxt]

    #print(i,alphabet.index(i.upper()),alphabet[index_char_chipertxt],index_char_chipertxt) -> IMPRIME A CIFRAGEM DE CADA LETRA

  return encrypt_string



def decrypt(chipertext,key): # FUNÇÃO P/ DESCIFRAR TEXTO CIFRADO
  decrypt_string = ''

  for i in chipertext.upper():

    if i==" ":
      decrypt_string=decrypt_string+i
    else:
      index_char_plaintxt = (alphabet.index(i.upper()) - key)%26
      decrypt_string=decrypt_string+alphabet[index_char_plaintxt]

    #print(i,alphabet.index(i.upper()),alphabet[index_char_plaintxt],index_char_plaintxt) -> IMPRIME A DESCIFRAGEM DE CADA LETRA

  return decrypt_string


def break_crypt(chipertext): # FUNÇÃO PARA "QUEBRAR" A CRIPTOGRAFIA DO TEXTO POR FORÇA BRUTA
  for key in range(len(alphabet)):
    decrypt_string = ''
    for i in chipertext.upper():

      if i==" ":
        decrypt_string=decrypt_string+i
      else:
        index_char_plaintxt = (alphabet.index(i.upper()) - key)%26
        decrypt_string=decrypt_string+alphabet[index_char_plaintxt]

    print(decrypt_string,key)



print("TEXO CIFRADO: "+encrypt('THIS IS MY MESSAGE',18)) 
print("TEXTO DESCIFRADO: "+decrypt('LZAK AK EQ EWKKSYW',18))

print("BRUTE FORCE NO TEXTO CIFRADO(TESTANDO TODAS AS POSSIBILIDADES):")
break_crypt("LZAK AK EQ EWKKSYW")
