#Pentru un șir cu n numere întregi care conține și duplicate,
#să se determine elementul majoritar (care apare de mai mult de n / 2 ori).
#De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].

#raspunsul meu
def element_majoritar(nums):
    """
       Identifică elementul majoritar dintr-un șir de numere întregi.
       Args:
       nums (list): Lista de numere întregi.
       Returns:
       int or None: Elementul majoritar din șir, sau None dacă nu există un element majoritar.
    """
    n = len(nums)
    aparitii = {}

    for num in nums:
        aparitii[num] = aparitii.get(num, 0) + 1

    for num, count in aparitii.items():
        if count > n / 2:
            return num
    return None


nums = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]
element_major = element_majoritar(nums)
if element_major is not None:
    print("Elementul majoritar este: ",element_major)
else:
    print("Nu există un element majoritar")


#raspunsul chat ului
def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    count = nums.count(candidate)
    if count > len(nums) // 2:
        return candidate
    else:
        return None

nums = [7, 7, 7, 7, 5, 5, 5, 5, 5]
print("Elementul majoritar este:", majority_element(nums))
