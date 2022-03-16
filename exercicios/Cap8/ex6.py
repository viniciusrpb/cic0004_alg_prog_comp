frase_completa = input()
ss = ""
for frase in frase_completa.split("."):
    if frase != "":
        ss += frase.strip().capitalize() + ". "
print(ss)