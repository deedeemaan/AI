#Să se determine produsul scalar a doi vectori rari care conțin numere reale.
#Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
#De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.

#raspunsul meu:
def produs_scalar(v1, v2):
    """
        Calculează produsul scalar al doi vectori.
        Args:
        v1 (list): Primul vector.
        v2 (list): Al doilea vector.
        Returns:
        int: Produsul scalar al celor doi vectori.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie să aibă aceeași lungime.")

    suma_produselor = 0

    for i in range(len(v1)):
        suma_produselor += v1[i] * v2[i]

    return suma_produselor

v1 = [1, 0, 2, 0, 3]
v2 = [1, 2, 0, 3, 1]
rezultat = produs_scalar(v1, v2)
print("Produsul scalar al vectorilor este: ", rezultat)

#raspunsul chat-ului:
def produs_scalar(vector1, vector2):
    # Asigurăm că vectorii au aceeași lungime
    if len(vector1) != len(vector2):
        raise ValueError("Vectorii trebuie să aibă aceeași lungime.")

    # Calculăm produsul scalar folosind compresie de listă și funcția zip
    suma_produselor = sum(x * y for x, y in zip(vector1, vector2))

    return suma_produselor

# Exemplu de utilizare:
vector1 = [1, 0, 2, 0, 3]
vector2 = [1, 2, 0, 3, 1]
rezultat = produs_scalar(vector1, vector2)
print("Produsul scalar al vectorilor {} și {} este: {}".format(vector1, vector2, rezultat))
