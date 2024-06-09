#Să se determine cuvintele unui text care apar exact o singură dată în acel text.
# De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.

#raspunsul meu
def aparitie_unica(text):
    """
        Identifică cuvintele dintr-un text care apar exact o singură dată.
        Args:
        text (str): Textul în care se caută cuvintele cu o singură apariție.
        Returns:
        list: O listă conținând cuvintele care apar o singură dată în text.
    """
    cuvinte = text.split()

    frecventa_cuvinte = {}
    for cuvant in cuvinte:
        frecventa_cuvinte[cuvant] = frecventa_cuvinte.get(cuvant, 0) + 1

    cuvinte_unice = [cuvant for cuvant, frecventa in frecventa_cuvinte.items() if frecventa == 1]

    return cuvinte_unice

text = "ana are ana are mere rosii ana"
print("Cuvintele care apar o singură dată sunt: ", aparitie_unica(text))


#raspunsul chat ului
from collections import Counter
import re

def cuvinte_unice(text):
    # Descompunem textul în cuvinte folosind expresii regulate
    cuvinte = re.findall(r'\b\w+\b', text.lower())

    # Numărăm de câte ori apare fiecare cuvânt
    frecventa_cuvinte = Counter(cuvinte)

    # Selectăm cuvintele care apar o singură dată
    cuvinte_unice = [cuvant for cuvant, frecventa in frecventa_cuvinte.items() if frecventa == 1]

    return cuvinte_unice

# Exemplu de utilizare:
text = "ana are ana are mere rosii ana"
cuvinte = cuvinte_unice(text)
print("Cuvintele care apar o singură dată în textul '{}' sunt: {}".format(text, cuvinte))

