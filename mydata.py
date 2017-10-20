import yaml

data={'First' : 'Michael',
      'Last' :  'Zabary',
      'Age' : 64,
      'Emails' : {'gmail':'mzabary@gmail.com',
                 'aol':'mzabary@aol.com',
                  'yahoo':'mzabary@yahoo.com'},
      'languages' : { 'markup': ['html','xml'],
                     'programing': ['C','Python','Java']}
      }
print(data)

print(yaml.dump(data,default_flow_style=False))

data2= '''
First: Michael
Last: Zabary
Age: 64
Emails:
  aol: mzabary@aol.com
  gmail: mzabary@gmail.com
  yahoo: mzabary@yahoo.com
languages:
  markup:
  - html
  - xml
  programing:
  - C
  - Python
  - Java
'''
from pprint import pprint
pprint(yaml.load(data2))
for i,j in data.items():
    print(i,j)

#{'First': 'Michael', 'Last': 'Zabary', 'Age': 64,
# 'Emails': {'aol': 'mzabary@aol.com', 'gmail': 'mzabary@gmail.com', 'yahoo': 'mzabary@yahoo.com'},
# 'languages': {'markup': ['html', 'xml'], 'programing': ['C', 'Python', 'Java']}}

class1 = { 'xEthan':'9','Ian':'3','Helen':'8','Holly':'6' }
print(sorted(class1.items()))
import collections
class1 = collections.OrderedDict()
for k, v in class1.items():
    print(k, v)