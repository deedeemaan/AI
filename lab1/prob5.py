def valoare(nums):
    """
    Identifică valoarea care apare de două ori într-un șir dat.
    Args:
    nums (list): Un șir de numere întregi care conține valori din mulțimea {1, 2, ..., n - 1}, unde n este lungimea șirului.
    Returns:
    int or None: Valoarea care apare de două ori în șir, sau None dacă nu există o valoare repetată.
    Complexitate O(n)
    """
    numere_vazute = set()

    for num in nums:
        if num in numere_vazute:
            return num
        else:
            numere_vazute.add(num)
    return None

nums = [1, 2, 3, 4, 2]
val = valoare(nums)
if val is not None:
    print("Valoarea care se repetă este: ", val)
else:
    print("Nu s-a găsit nicio valoare repetată în sir")


#raspunsul chat ului
def valoare_repetata(nums):
    n = len(nums)

    # Calculăm suma totală a elementelor și suma elementelor distincte
    suma_totala = sum(nums)
    suma_distincta = sum(set(nums))

    # Diferența dintre suma totală și suma elementelor distincte va fi valoarea care se repetă
    valoare_repetata = suma_totala - suma_distincta

    return valoare_repetata


# Exemplu de utilizare:
nums = [1, 2, 3, 4, 2]
valoare = valoare_repetata(nums)
print("Valoarea care se repetă în șirul {} este: {}".format(nums, valoare))

