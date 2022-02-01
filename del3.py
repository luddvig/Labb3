from bintreeFile import Bintree
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet

print()

engelska = Bintree()
with open("engelska.txt", "r") as engelskfil:
    for rad in engelskfil:
        for uttryck in rad.split():
            ordet = uttryck.strip(' ",.!')
            if ordet in engelska:
                pass
            else:
                engelska.put(ordet)
                if ordet in svenska:
                    print(ordet, end=" ")
# .isalnum