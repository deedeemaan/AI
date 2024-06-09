import math
#Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
#De ex. distanța între (1,5) și (4,1) este 5.0

#Respunsul meu:
def distantaEuclidiana(p1,p2, q1,q2):
    """
        Calculează distanța euclidiană între două puncte bidimensionale.
        Args:
        p1 (float): Coordonata x a primului punct.
        p2 (float): Coordonata y a primului punct.
        q1 (float): Coordonata x a celui de-al doilea punct.
        q2 (float): Coordonata y a celui de-al doilea punct.
        Returns:
        float: Distanța euclidiană dintre cele două puncte.
    """
    return math.sqrt((q1-p1)**2+(q2-p2)**2)

p1, p2 = 1, 5
q1, q2 = 4, 1
print("Distanta euclidiana este: ", distantaEuclidiana(p1, p2, q1, q2))


#raspunsul chat-ului:
def distanta_euclidiana(locatie1, locatie2):
    x1, y1 = locatie1
    x2, y2 = locatie2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Exemplu de utilizare:
locatie1 = (1, 5)
locatie2 = (4, 1)
distanța = distanta_euclidiana(locatie1, locatie2)
print("Distanța euclidiană între {} și {} este: {:.2f}".format(locatie1, locatie2, distanța))
