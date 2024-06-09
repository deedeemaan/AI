#complexitate de timp O(n log n)
#complexitate de spatiu teta(1)
def elemK(v, k):
    v.sort(reverse = True)
    return v[k-1]


v = [7, 4, 6, 3, 9, 1]
print(elemK(v, 2))


def kth_largest(nums, k):
    # Sortăm șirul în ordine descrescătoare
    nums.sort(reverse=True)

    # Returnăm al k-lea cel mai mare element
    return nums[k - 1]


# Exemplu de utilizare
nums = [7, 4, 6, 3, 9, 1]
k = 2
print(f"Al {k}-lea cel mai mare element este:", kth_largest(nums, k))