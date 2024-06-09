#Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text
#care conține mai multe cuvinte separate prin ” ” (spațiu).
#De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este cuvântul "si".

#raspunsul meu

def ultimul_cuv(text):
    """
        Returnează ultimul cuvânt dintr-un text dat în ordine alfabetică.
        Args:
        text (str): Textul din care se va extrage ultimul cuvânt.
        Returns:
        str: Ultimul cuvânt din text, ordonat alfabetic.
        Complexitate: O(nlogn)
    """
    cuvinte = text.split()
    cuvinte.sort()
    ultimul = cuvinte[-1]
    return ultimul

# text="Maria si Ana merg la magazin"
# assert(ultimul_cuv(text) == "si")

text = "Ana are mere rosii si galbene"
print("Ultimul cuvânt din punct de vedere alfabetic este:", ultimul_cuv(text))

#raspunsul chat ului
def ultimul_cuvant(text):
    """
     Complexitate O(n)
    """

    # Split textul într-o listă de cuvinte
    cuvinte = text.split()

    # Folosim functia max() pentru a găsi ultimul cuvânt în ordine alfabetică
    ultim = max(cuvinte, key=str.lower)

    return ultim

# assert()

# Exemplu de utilizare:
text = "Ana are mere rosii si galbene"
ultim = ultimul_cuvant(text)
print("Ultimul cuvânt din punct de vedere alfabetic în textul '{}' este: '{}'".format(text, ultim))
