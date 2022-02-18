# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

pat = "test"
text = "test bruh test Test"
m = len(pat)
n = len(text)

strongBord = []


def sliding_window(count=0):
    i = 0
    while i <= n - m:
        j = 0
        while (j < m) and (pat[j] == text[i + j]):
            j += 1
            if j == m:
                count += 1
                break

        i += 1
    print("sliding window Matches: ", count)
    return


def kmp_table():
    strongBord.append(-1)
    t = -1
    for j in range(1, m):
        while (t >= 0) and (pat[t] != pat[j - 1]):
            t = strongBord[t]
        t += 1

        if (j == m) or (pat[t] != pat[j]):
            strongBord.append(t)
        else:
            strongBord.append(strongBord[t])


def kmp_search(count=0):
    i = 0
    j = 0
    while i <= (n - m):
        while (j < m) and (pat[j] == text[i + j]):
            j += 1
        if j == m:
            count += 1
            print("index; ", i)
        i = i + strongBord[j - 1]
        j = max(0, j - strongBord[j - 1])
    print("kmp Matches: ", count)


def bm_shift():
    bmShift = [-1] * 256
    for i in range(0, 256):
        bmShift[i] = m
    for i in range(0, m - 1):
        bmShift[ord(pat[i])] = m - i - 1
    return bmShift


def boyer_moore(count=0):
    bmShift = bm_shift()
    for c in set(pat):
        print(c, ord(c), bmShift[ord(c)])
    i = 0
    while i <= n - m:
        j = m
        while j > 0 and pat[j - 1] == text[i + j - 1]:
            j = j - 1
        print("j:", j, "i:", i)
        if j == 0:
            count += 1
            print("index; ", i)
            i += m
        else:
            i += bmShift[ord(text[i + m - 1])]
    print("bm Matches: ", count)


class Node:
    def __init__(this, final=False, index=-1):
        this.final = final
        this.index = index
        this.childern = {}

    def __str__(self):
        self.__toString__()
        return ""

    def __toString__(self, depth=0):
        print("({0} {1}:".format(self.final, self.index))
        for k, v in self.childern.items():
            for i in range(depth):
                print("\t", end="")
            print("'{0}' -> ".format(k), end="")
            v.__toString__(depth + 1)


class Autoamton:
    def __init__(this):
        this.root = Node(True, -1)

    def add_Suffix_Root(this, string):
        this.add_Suffix(this.root, string)

    def add_Suffix(this, node, string, index):
        if len(string) == 0:
            node.final = True
            node.index = index
            return
        if string[0] not in node.childern.keys():
            node.childern[string[0]] = Node()

        this.add_Suffix(node.childern[string[0]], string[1:], index)

    def print(this):
        print(this.root)


def suffix_trie():
    M = Autoamton()
    i = 0
    for i in range(i, n):
        fork, k = find_trie(M.root, i)
        p = fork
        j = k
        for j in range(j, n):
            M.add_Suffix(p, text[i:], i)
    return M


def find_trie(p, k):
    while k < n and target(p, k):
        p, k = target(p, k), k + 1
    return p, k


def target(p, k):
    return p.childern == text[k]


def search_suffix_trie(M, pat):
    indices = []
    current_node = M.root
    for c in pat:
        if current_node.childern[c]:
            current_node = current_node.childern[c]
        else:
            return []
    count_matches(current_node, indices)
    indices.sort()
    return indices


def count_matches(current_node: Node, indices):
    if current_node.final:
        indices.append(current_node.index)
    for child in current_node.childern.values():
        count_matches(child, indices)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sliding_window()
    boyer_moore()
    M = suffix_trie()
    #M.print()
    print("trie matches:", search_suffix_trie(M, pat))


"""
    A = Autoamton()
    A.add_Suffix_Root("test")
    A.add_Suffix_Root("est")
    A.add_Suffix_Root("st")
    A.add_Suffix_Root("t")

    A.print()
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""
def bm_same(str1, str2, length):
    i = length - 1
    while str1[i] == str2[i]:
        if i == 0:
            return True
        i -= 1
    return False


def bm_search():
    bmShift = bm_shift()
    skip = 0
    while n - skip >= m:
        if bm_same(text[skip:], pat, m):
            return skip
        skip += bmShift[text[skip + m - 1]]
    print("no match")
"""
