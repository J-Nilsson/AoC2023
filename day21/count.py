
def positions(k):
    res = 0
    res += 7806 * k ** 2
    res += 7744 * (k - 1) ** 2
    res += 5849
    res += 5852
    res += 5842
    res += 5839
    res += 6799 * (k - 1)
    res += 999 * k
    res += 984 * k
    res += 1000 * k
    res += 982 * k
    res += 6796 * (k - 1)
    res += 6787 * (k - 1)
    res += 6797 * (k - 1)

    return res

print(positions(202300))