import random
l = ['Hi %s','Hello %s', 'Hyy %s', 'bye %s']

#If we have to create names file with our own input, similarly can be done for msg also
# namese = ['neha','bhavesh','yash','kunal']
# with open('names.txt', 'w') as f:
#         f.write("")
# for i in namese:
#     name = i
#     with open('names.txt', 'a') as f:
#         f.write(name)
#         f.write("\n")

with open('names.txt') as f:
    names = f.readlines()
for i in range(len(names)-1):
    names[i]= names[i].strip('\n') #can use rstrip if something xtra on L.H.S.

with open('op.txt', 'w') as f:
        f.write("")
for i in names:
    name = i
    mess = random.choice(l)
    name = name.strip('\n')
    print(mess %name)
    with open('op.txt', 'a') as f:
        f.write(mess %name)
        f.write("\n")
