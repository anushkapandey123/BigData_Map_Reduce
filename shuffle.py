import binascii

def get_partition( key, value, numReduceTasks):
    result= hash(key) % numReduceTasks
    return result
    
f0=open("/home/pes1ug20cs072/BD_Project/worker1/inter_file.txt","r")
f1=open("/home/pes1ug20cs072/BD_Project/worker2/inter_file.txt","r")
#f2=open("txt3.txt","r")

line0=f0.readlines()
line1=f1.readlines()
#line2=f2.readlines()
o0=open("/home/pes1ug20cs072/BD_Project/worker1/o1.txt","w")
o1=open("/home/pes1ug20cs072/BD_Project/worker2/o1.txt","w")
#o2=open("o2.txt","a")


for index,line in enumerate (line0):
    k,v=line.strip().split(',')
    
    output=get_partition(k,v,2)
    if(output==0):
        o0.write("{}, {}\n".format(k,v))
    if(output==1):
        o1.write("{}, {}\n".format(k,v))
    '''if(output==2):
        o2.write("{}, {}\n".format(k,v))'''
f0.close()
for index,line in enumerate (line1):
    k,v=line.strip().split(',')
    
    output=get_partition(k,v,2)
    if(output==0):
        o0.write("{}, {}\n".format(k,v))
    if(output==1):
        o1.write("{}, {}\n".format(k,v))
    '''if(output==2):
        o2.write("{}, {}\n".format(k,v))'''
f1.close()
'''for index,line in enumerate (line2):
    k,v=line.strip().split(',')
    
    output=get_partition(k,v,2)
    if(output==0):
        o0.write("{}, {}\n".format(k,v))
    if(output==1):
        o1.write("{}, {}\n".format(k,v))
    if(output==2):
        o2.write("{}, {}\n".format(k,v))'''
#f2.close()


