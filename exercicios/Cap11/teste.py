import csv

disciplinas = {}

def lerArquivoCSV(arq):
    with open(arq, encoding="utf-8") as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        #print(cabecalho)
        turmas = {}
        for line in reader:
            cod = line[0]
            nomeDis = line[1]
            nomeProf = line[4].split("(")[0].strip()
            carga = int(line[4].split("(")[1].split("h")[0])
            disciplinas[cod] = {"nome": nomeDis}
            turma = line[2]
            if cod in turmas:
                if turmas[cod].count(turma) == 0:
                    turmas[cod].append(turma)
            else:
                turmas[cod] = [turma]
            #print(cod,nomeDis,nomeProf,carga)
            disciplinas[cod]["turmas"] = turmas[cod]
        print(disciplinas)
        
    

def lerArquivo(arq):
    with open(arq, encoding="utf-8") as file:
        next(file)
        for line in file:
            cod = line.split(",")[0]
            nome = line.split(",")[1]
            print(line.split(","))
            print(cod, nome)

def gravarArquivo(arq):
    with open(arq, mode="w") as file:
        ll = [1,2,3,4,5,6,7]
        file.write("Oi eu sou o Goku!\n")
        file.write("Tudo bem com vc?\n")
        file.write(str(ll))


lerArquivoCSV("teste.csv")
#gravarArquivo("teste2.txt")
        



        
        
        
        
        
        
        
        