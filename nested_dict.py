mydict={'One':{'First':'Mike','Last':'Zabary'}
      ,'Two':{'Address1':'1112 Mountain Springs Drive','Address2':'Stroudsburg, PA 18360'}}
#### PRINT THE DICT
print(mydict)
#{'Two': {'Address1': '1112 Mountain Springs Drive', 'Address2': 'Stroudsburg, PA 18360'},
                                                   #  'One': {'Last': 'Zabary', 'First': 'Mike'}}
# PRINT THE OUTER KEYS
for i in (mydict):
    pass
    #print(i)
#One
#Two
    # PRINT THE 2 Seperate DICT
    #print(mydict[i])

#{'Last': 'Zabary', 'First': 'Mike'}
#{'Address1': '1112 Mountain Springs Drive', 'Address2': 'Stroudsburg, PA 18360'}

####  PRINT INNER AND OUTER KEYS
for i in mydict:
   #pass
   for j in mydict[i]:
        pass
        #print(j)
#First
#Last
#Address2
#Address1

for i in mydict:
   pass
   #print(i, ' : ',mydict[i])  # print 2 seperate dict
#Two: {'Address1': '1112 Mountain Springs Drive', 'Address2': 'Stroudsburg, PA 18360'}
#One: {'First': 'Mike', 'Last': 'Zabary'}
for i in mydict:
   pass
   #print(i,mydict[i])  # print 2 seperate dict
#One {'First': 'Mike', 'Last': 'Zabary'}
#Two {'Address1': '1112 Mountain Springs Drive', 'Address2': 'Stroudsburg, PA 18360'}

### PRINT KEYS AND VALUES of ALL inner and outer
for i in mydict:
   for j in mydict[i]:
        pass
        #print(j,'is:',mydict[i][j])
#First is: Mike
#Last is: Zabary
#Address1 is: 1112 Mountain Springs Drive
#Address2 is: Stroudsburg, PA 18360

mydict2={'One': {'First': 'Mike', 'Last': 'Zabary'},
         'Two': {'Address1': '1112 Mountain Springs Drive','Address2': ['Stroudsburg', 'PA', '18360']}}
print(mydict2)
#{'Two': {'Address2': ['Stroudsburg', 'PA', '18360'], 'Address1': '1112 Mountain Springs Drive'},
#                                     'One': {'Last': 'Zabary', 'First': 'Mike'}}

# PRINT KEYS
for i in mydict2:
    pass
    #print(i)
#Two
#One
for i in mydict2:
    pass
    for j in mydict2[i]:
        pass
        #print(j)
#Address1
#Address2
#First
#Last

### PRINT ALL KEY & VALUES
for i in mydict2:
    pass
    #for j in mydict2[i]:
    #    print(j,mydict2[i][j])
#Address1 1112 Mountain Springs Drive
#Address2 ['Stroudsburg', 'PA', '18360']
#First Mike
#Last Zabary

for i in mydict2:
    for j in mydict2[i]:
        line=(j,mydict2[i][j])
        #print(line[0])
        if line[0]=='First':
            print('First Name:', mydict2[i][j])
        elif line[0]=='Last':
            print('Last Name:', mydict2[i][j])
        elif line[0]=='Address1':
            print('Address:', mydict2[i][j])
        elif line[0]=='Address2':
            print('State, City, Zip:', mydict2[i][j])
#Last Name: Zabary
#First Name: Mike
#Address: 1112 Mountain Springs Drive
#State, City, Zip: ['Stroudsburg', 'PA', '18360']

for i in mydict2:
    for j in mydict2[i]:
        line=(j,mydict2[i][j])
        if line[0]=='First':
            fname=mydict2[i][j]
        elif line[0]=='Last':
            lname=mydict2[i][j]
        elif line[0]=='Address1':
            addr=mydict2[i][j]
        elif line[0]=='Address2':
            addr2=list(mydict2[i][j])
print(fname,lname)
print(addr)
print(addr2[0],addr2[1],addr2[2])

#Mike Zabary
#1112 Mountain Springs Drive
#Stroudsburg PA 18360