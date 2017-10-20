import yaml

'''
# abc.yaml file
title: Penny Lane
songs:
  -  Abby Road
  -  White Album
  -  Revolver
Band: Beatles

 
 
truck = dict(
    color = 'blue',
    brand = 'ford',
import config
print config.truck['color']
'''

'''
{'total': 4443.52, 
 'tax': 251.42,
 'product': [
                {'description': 'Basketball', 'sku': 'BL394D', 'quantity': 4, 'price': 450.0},
                {'description': 'Super Hoop', 'sku': 'BL4438H', 'quantity': 1, 'price': 2392.0}
            ],
 'date': datetime.date(2001, 1, 23), 
 'invoice': 34843,
 'bill-to': {
            'given': 'Chris',
            'family': 'Dumars',
            'address': {
                        'lines': '458 Walkman Dr.\nSuite #292\n',
                        'city': 'Royal Oak', 
                        'state': 'MI',
                        'postal': 48046
                        }
            },
 'ship-to': 
            {
            'given': 'Chris', 
            'family': 'Dumars',
            'address': {
                        'lines': '458 Walkman Dr.\nSuite #292\n',
                        'city': 'Royal Oak', 
                        'state': 'MI',
                        'postal': 48046
                        }
            },
 'comments': 'Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338"""))'}

'''

#with open('abc.yaml', 'r') as mixed_data:
#with open('yaml1.yaml', 'r') as mixed_data:
with open('invoicex.yaml', 'r') as mixed_data:
    try:
        #for x in yaml.load_all(mixed_data):
        for x in yaml.load_all(mixed_data):
            pass
            print(x)
            #print(type(x))
            #< class 'dict'>
    except yaml.YAMLError as err:
        print(err)
print('------------------------------')
for key,val in x.items():
    #print(key)
    #if key=='date':
    #    print(key,val)
    ########################print(key,' : ',val)
    #print(type(val))
    if isinstance(val, str):
        if key=='comments':
            ship_comments='Ship comments:\n'+val
        #print('String =',key,val)
    elif isinstance(val, dict):
        #print('This is an outer DICT:',key,val)
        for j,k in val.items():
            #print('This is an inner1 DICT:',j,k)
            if isinstance(k, dict):
                #print('This is an inner2 DICT:', j,k)
                for n, m in k.items():
                    if n=='lines':
                        if key=='bill-to':
                            bill_address=m
                        if key=='ship-to':
                            ship_address=m
                    elif n in ['city','state','postal']:
                        if n == 'city':
                            city=m
                        elif n == 'state':
                            state=m
                        else:
                            zip=m

                        #print(m)
            #else:
            #    if j=='given':
            #        print('First Name:',k)
            #    elif j=='family':
            #        print('Last Name:',k)

                #print('This is an inner1 DICT:', j, k)
                #    if isinstance(n, dict):
                #        for a, b in n.items():
                #            print(b)
                #            if isinstance(a, dict):
                #                for a1, b1 in a.items():
                #                    print(b1)


    elif isinstance(val, list):
        #print('This is a list:',key,val)
        print('\nItems Sold:\n')
        for v in val:
            for o,p in v.items():
                print(o,p)
            print('')
    elif isinstance(val, int) and key=='invoice':
        print('Invoice Number:',val)
    elif isinstance(val, float):
        if key=='tax':
            print('Sales Tax:',val)
        elif key=='total':
            print('Total Invoice:',val)
        #elif key == 'price':
        #    print('price = ', key, val)
        else:
            print('float = ', key, val)
    else: print('\nDate:',val)

    #else:
    #    raise ValueError

bill_address1=''
indexi=0
for i in bill_address:
   if i == '\n':
      break
   else:
      indexi +=1
      bill_address1 += i

bill_address2=''
for j in bill_address[int(indexi + 1):]:
    if j == '\n':
        break
    else:
        bill_address2 += j
print('')
print('Billing Address:')
print(bill_address1)
print(bill_address2)
print('{}, {}  {}'.format(city,state,zip))

ship_address1=''
indexi=0
for i in ship_address:
   if i == '\n':
      break
   else:
      indexi +=1
      ship_address1 += i

ship_address2=''
for j in ship_address[int(indexi + 1):]:
    if j == '\n':
        break
    else:
        ship_address2 += j
print('')
print('shiping Address:')
print(ship_address1)
print(bill_address2)
print('{}, {}  {}'.format(city,state,zip))
print('')
print(ship_comments)
