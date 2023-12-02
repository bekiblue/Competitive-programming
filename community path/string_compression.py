class Solution():
    def compress(self, chars):
        size = len(chars)
        if size < 2:
            return size
        anchor, write = 0, 0
        for pos, char in enumerate(chars):
            if (pos + 1) == size or char != chars[pos+1]:
                chars[write] = char
                write += 1
                if pos > anchor:
                    repeated_times = pos - anchor + 1
                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1
                anchor = pos + 1
        return write
