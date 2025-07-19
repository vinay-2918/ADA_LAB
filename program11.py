def compute_lps(pat):
    lps = [0] * len(pat)
    length = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(txt, pat):
    lps = compute_lps(pat)
    i = j = 0
    while i < len(txt):
        if txt[i] == pat[j]:
            i += 1
            j += 1
        if j == len(pat):
            print("Pattern found at index", i - j)
            j = lps[j - 1]
        elif i < len(txt) and txt[i] != pat[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

text = input("Enter text: ")
pattern = input("Enter pattern: ")
kmp_search(text, pattern)
# This code implements the Knuth-Morris-Pratt (KMP) algorithm for substring search.
# The function kmp_search uses a precomputed longest prefix-suffix (LPS) array to efficiently find occurrences of a pattern in a given text.