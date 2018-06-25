f=open('fread1.py','r')
data1=f.read()
f.close()

lst=data1.split('\n')
mocount=0;
wdcount=0;

for i in range(len(lst)):
    mocount+=len(lst[i])
    wdcount+=len(lst[i].split(' '))

print(len(lst), mocount, wdcount)
