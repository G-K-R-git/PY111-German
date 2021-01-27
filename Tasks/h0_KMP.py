from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    if len(prefix_str) == 0:
        return None
    else:
        prefix_table = [0]
        i = 1
        while i <= len(prefix_str) - 1:
            i += 1
            max_match = 0
            prefix_table.append(max_match)
            for j in range(0, i - 1):
                flag = True
                k = 0
                while flag:
                    if prefix_str[k] == prefix_str[i-j-1+k]:
                        k += 1
                    else:
                        flag = False
                    if k >= j+1:
                        flag = False
                if not flag and prefix_table[-1] < k:
                    prefix_table[-1] = k
        return prefix_table


    # VARIANT WITH SLICING
    # if len(prefix_str) == 0:
    #     return None
    # else:
    #     prefix_table = [0]
    #     i = 1
    #     while i <= len(prefix_str)-1:
    #         i += 1
    #         max_match = 0
    #         for j in range(0, i-1):
    #             print(i, j, prefix_str[0:j+1], prefix_str[i-1-j:i])
    #             if prefix_str[0:j+1] == prefix_str[i-1-j:i]:
    #                 max_match = j+1
    #         prefix_table.append(max_match)
    #     print(prefix_table)
    #     return prefix_table


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    i = 0
    j = 0
    search_index = []
    prefix = _prefix_fun(substr)
    while i < len(inp_string):
        if inp_string[i] == substr[j]:
            if j == len(substr)-1:
                search_index.append(i-j)
                j = prefix[j - 1]
            i += 1
            j += 1
        elif j <= 0:
            i += 1
        elif j > 0:
            j = prefix[j-1]
    if not search_index:
        return None
    return search_index[0]


if __name__ == '__main__':
    _prefix_fun("abcabca")
    # searched = kmp_algo("abcabca", "abca")
    # print(searched)