import os
import csv
def getModelName(filename):
    model = filename.split(".")[0].capitalize()
    if "_" in model:
        model = model.split("_")
        model = "".join(map(lambda x: x.capitalize(),model))
    return model

def writeMdTable(rawfile,targetfile):
    model = getModelName(rawfile)
    with open(targetfile,'a') as seeds:
        seeds.write("\n\n#### "+ model +'\n\n\n')

    with open(rawfile) as csvfile:
        spamreader = csv.reader(csvfile)
        has_header = 0
        for row in spamreader:
            if has_header == 0:
                header = list(map(lambda x: x.lower(),row))
                has_header = 1
                nocol = len(header)
                headerline = "|"
                secondline = "|"
                for param in row:
                    headerline = headerline+param+" |"
                    secondline = secondline+":---|"
                with open(targetfile,'a') as seeds:
                    seeds.write(headerline+'\n'+secondline+'\n')
            else:
                dataline = "|"
                for param in row:
                    dataline = dataline+param+" |"
                with open(targetfile,'a') as seeds:
                    seeds.write(dataline+'\n')
                    
programfile = "program.csv"
targetfile = 'ModelMdTable.md'
print(programfile)
writeMdTable(programfile,targetfile)
shipname =[]
for file in os.listdir(os.getcwd()):
    if file.endswith(".csv"):
        if (file != programfile):
            if (not os.path.splitext(file)[0].endswith("ship")):
                print(file)
                writeMdTable(file,targetfile)
            else:
                shipname.append(file)
for file in shipname:
    print(file)
    writeMdTable(file,targetfile)