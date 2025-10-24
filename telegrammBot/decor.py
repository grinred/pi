def string_strip(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


str1 = string_strip("!")
print(str1("! some "))
