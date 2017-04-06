import os
import csv

def getModelName(filename):
    model = filename.split(".")[0].capitalize()
    if "_" in model:
        model = model.split("_")
        model = "".join(map(lambda x: x.capitalize(),model))
    return model

def writeToSeeds(rawfile,targetfile):
    model = getModelName(rawfile)
    with open(rawfile) as csvfile:
        spamreader = csv.reader(csvfile)
        has_header = 0
        for row in spamreader:
            if has_header == 0:
                header = row
                has_header = 1
            else:
                if (row[0] == '' and row[1] == ''):
                    break
                inputcat =model+".create("
                for idx, param in enumerate(row):
                    param = param.strip()
                    if param.isdigit():
                        inparam = param
                    elif (param.lower() in ['true','false']):
                        inparam = '"'+ param.lower() +'"'
                    else: 
                        inparam = '"'+param+'"'
                        
                    inputcat = inputcat+" "+":"+header[idx].lower()+' => '\
                    +inparam + ","
                inputcat = inputcat[:-1]+')'                
                with open(targetfile,'a') as seeds:
                    seeds.write(inputcat+'\n')
                        
programfile = "program.csv"
userfile = "user.csv"
targetfile = 'seeds.rb'
print(programfile)
writeToSeeds(programfile,targetfile)
print(userfile)
writeToSeeds(userfile,targetfile)
shipname =[]
for file in os.listdir(os.getcwd()):
    if file.endswith(".csv"):
        if (file != programfile and file != userfile):
            if (not os.path.splitext(file)[0].endswith("ship")):
                print(file)
                writeToSeeds(file,targetfile)
            else:
                shipname.append(file)
for file in shipname:
    print(file)
    writeToSeeds(file,targetfile)

  