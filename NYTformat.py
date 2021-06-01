#produce a formatted version of the cleaned result data from the json
import json

file=open('NYTcleaned.json','r')
mainD=json.load(file)
new=open('NYTformatted.txt','w')
for section in mainD:
    new.write('Section: '+ section+'\n')
    for key in mainD[section]:
        length=len(mainD[section][key])
        if str(key)=='1':
            new.write(str(length)+' words appear once: \n')
            for word in mainD[section][key]:
                new.write(word+ ' ')
            new.write('\n')
        else:
            new.write(str(length)+' words appear '+ str(key)+' times: \n')
            for word in mainD[section][key]:
                new.write(word+ ' ')
            new.write('\n')
    new.write('\n')
new.close()
file.close()