import sys
import yaml
import pprint

filename = 'tree.yaml'
#filename = 'invoice.yaml'

y = yaml.safe_load(open(filename, 'r'))

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(y)
print(str(y))
for key0, val0 in y.items():
    print(key0)
    print('\n',val0)
    #if key0 == 'product':
    #    print('yep')

def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                for d in dict_generator(value, [key] + pre):
                    yield d
            elif isinstance(value, list) or isinstance(value, tuple):
                for v in value:
                    for d in dict_generator(v, [key] + pre):
                        yield d
            else:
                yield pre + [key, value]
    else:
        yield indict

x=list(dict_generator(y, pre=None))
print(x)


    #print(val)
#for key, val in y.items():
#    print(key)

"""

bill-to
tax
invoice
comments
total
date
ship-to
product

bill-to
tax
invoice
comments
total
date
ship-to
product

"""