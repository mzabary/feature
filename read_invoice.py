import yaml
#explicit_start=True  use with dump
with open('invoice.yaml', 'r') as mixed_data:
    try:
        for mydict in yaml.load_all(mixed_data):
            pass
            print(mydict)
            #print(type(mydict))
            #< class 'dict'>
    except yaml.YAMLError as err:
        print(err)

for i in mydict:
    print(i,' : ', mydict[i])
    if isinstance(mydict[i], dict):
        for j,h in mydict[i].items():
            print('j=',j,'h=',h)
            if isinstance(mydict[i][j], dict):
                print('-----dict')
                for l,m in mydict[i][j].items():
                    print('l=',l,'m=',m)
    elif isinstance(mydict[i], list):
        for v in mydict[i]:
            for o,p in v.items():
                print(o,p)

