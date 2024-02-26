import re 
import csv
f=open("row.txt","r",encoding="utf8")
text=f.read()

pattern=r"\n(?P<order>[0-9]+)\.\n(?P<name>.+)\n(?P<count>.+)x(?P<price>.+)\n(?P<cost>.+)\n"
results=re.finditer(pattern,text)

with open('date.csv','w',newline='',encoding="utf8") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['order','name','count','price','cost'])
    for x in results:
        writer.writerow([
            x.group('order'), 
            x.group('name'), 
            float(x.group('count').strip().replace(',','.')), 
            float(x.group('price').strip().replace(',','.').replace(' ','')),
            x.group('cost')
        ])