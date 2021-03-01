class Solution:
    def strStr(self, haystack, needle):

        if len(needle) == 0:
            return 0

        i = 1
        j = 0

        prefix_array = [0] * len(needle)

        while i < len(needle):
            if needle[j] == needle[i]:
                prefix_array[i] = j + 1
                j += 1
            else:
                while True:
                    j = prefix_array[j - 1]

                    if needle[j] == needle[i]:
                        prefix_array[i] = j + 1
                        j += 1
                        break
                    else:
                        if j == 0:
                            break
            i += 1

        i = 0

        j = 0

        while i < len(haystack):
            if needle[j] == haystack[i]:
                j += 1
            else:
                if j != 0:
                    j = prefix_array[j - 1]
                    i -= 1
            i += 1

            if j == len(needle):
                return i - j

        return -1
