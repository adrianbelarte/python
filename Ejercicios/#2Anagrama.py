### 2 ES UN ANAGRAMA? ###

"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def anagrama(s1, s2):
    if s1.lower() == s2.lower():
        return False
    return sorted(s1.lower()) == sorted(s2.lower())

print(anagrama("amor","roma"))