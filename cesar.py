import string

#avec printable on a pas les caractères avec les accents, on peut le rajouter manuellement (une des façons de rajouter les autres caractères)
alphabet = string.printable + "àéèêôùü"

def cesar_cipher(message, key):
    crypted_message = ""
    #processus qui va chiffrer la variable message et stocker cela dans crypted message
    for char in message:
        """
        on va chiffrer le caractère
            1- trouver la position du carac dans l'alphabet
            2- y rajouter la clé à la postion du carac dans l'alphabet
            3- récupérer le caractère chiffré
        on va stocker le caractère chiffré
        """
        index_carac_in_printable = alphabet.index(char)
        index_crypted_char = (index_carac_in_printable + key) % len(alphabet)
        crypted_char = alphabet[index_crypted_char]

        crypted_message += crypted_char

    return crypted_message

def cesar_uncipher(crypted_message, key):
    return cesar_cipher(crypted_message, -key)

# print(cesar_cipher("coucou", 3))

# crypted_message = cesar_cipher("Salut les bgs aujourd'hui on va corriger l'exercice", 11)
# print(crypted_message)


def brute_force_cesar_cipher(crypted_message):
    for possible_key in range(0, len(alphabet)):
        print(cesar_uncipher(crypted_message, possible_key))
        print ("_"*15)

# brute_force_cesar_cipher(crypted_message)

"""VERSION 1 (longue)"""
def convert_password_to_list_of_keys(password):
    #password correspond à une liste de clés de chiffrement
    list_of_keys = [] #ici on utilise une liste car on fait des ajouts itératifs
    for char in password:
        current_key = alphabet.index(char)
        list_of_keys.append(current_key)
    return list_of_keys

def vigenere_cipher(message, password, reverse=False):
    #on peut aussi juste mettre "reverse" sans préciser "False", ici on met le paramètre par défaut à False.
    list_of_keys = convert_password_to_list_of_keys(password)
    crypted_message = ""
    for index, char in enumerate(message):
        current_key = list_of_keys[index % len(list_of_keys)]
        crypted_message += cesar_uncipher(char, current_key) if reverse else cesar_cipher(char, current_key) #si reverse=False alors on va déchiffrer, sinon on va chiffrer.
    return crypted_message

"""FIN VERSION 1"""


"""VERSION 2 (fonction convert_password mise en 1 ligne directement dans la fonction vigenere_cipher >> on fait ça car la fonction convert_password n'est pas bcp utilisée)"""
def vigenere_cipher(message, password, reverse=False):
    list_of_keys = [] #chercher le code sur drive
    crypted_message = ""
    for index, char in enumerate(message):
        current_key = list_of_keys[index % len(list_of_keys)]
        crypted_message += cesar_uncipher(char, current_key) if reverse else cesar_cipher(char, current_key)
    return crypted_message
    
"""FIN VERSION 2"""

crypted_message = vigenere_cipher("Salut les bgs aujourd'hui on va corriger l'exercice", "helloworld")
print(crypted_message)
original_message = vigenere_cipher(crypted_message, "helloworld", reverse=True)
print(original_message)

#si on indique pas que reverse=True >> ça va considérer que reverse=False

