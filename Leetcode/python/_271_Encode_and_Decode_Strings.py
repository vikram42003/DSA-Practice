# Problem number 659 on Lintcode
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # The main idea is, we cannot rely on a delimiter alone since
        # any ASCII character (including the delimiter) may appear inside the string.
        # So instead, we prefix each string with its length followed by a special marker '#'.
        # Format becomes: <length>#<string>
        # This guarantees unambiguous decoding because we know exactly
        # how many characters to read after the '#'.

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # For decoding, we iterate through the encoded string.
        # First, we read digits until we hit '#', which gives us the length.
        # Then we extract exactly 'length' characters after '#'.
        # We repeat this process until we process the entire string.

        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1

            length = int(str[i:j])
            j += 1

            res.append(str[j : j + length])
            i = j + length

        return res



    # Unserious but works solution
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        return "🤪".join(strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        return str.split("🤪")
