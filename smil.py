
print((lambda str: "\n".join((f"{i}" for i, x in enumerate(str) if x in (":", ";") and (str[i+1:i+2] == ")" or str[i+1:i+3] == "-)"))))(input()))
