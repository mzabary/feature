class Dotable(dict):

    __getattr__= dict.__getitem__

    def __init__(self, d):
        self.update(**dict((k, self.parse(v))
                           for k, v in d.items()))

    @classmethod
    def parse(cls, v):
        if isinstance(v, dict):
            return cls(v)
        elif isinstance(v, list):
            return [cls.parse(i) for i in v]
        else:
            return v

import sys
import yaml
import pprint

filename = 'tree.yaml'
#filename = 'invoice.yaml'

y = yaml.safe_load(open(filename, 'r'))
#mydict=Dotable(y)

d1=Dotable.parse({'a': [{'b': 3, 'c': 5}]})
print(d1.a)

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2)
print("Value : %s" %  dict)
d2=Dotable.parse({'Name': [{'Age': 7, 'Sex': 'female'}]})
print(d2.Name)
'''
Example use:

In [1]: d1 = Dotable.parse({'a': [{'b': 3, 'c': 5}]})

In [2]: d1.a
Out[2]: [{'b': 3, 'c': 5}]

In [3]: d1.a[0].b
Out[3]: 3

In [4]: d2 = Dotable.parse([42, {'a': 'shrubbery'}])

In [5]: d3 = Dotable.parse(7)


You can use format:

In [11]: '{d1.a[0].b}'.format(**locals())
Out[11]: '3'
I lied about not using regular expressions, you need a little one to remove the #s:

In [12]: s = '#{d1.a[0].b} #{d2[0].a}'

In [13]: import re

In [14]: re.sub('#({[^}]*})', r'\1', s)
Out[14]: '{d1.a[0].b} {d2[0].a}'

In [15]: re.sub('#({[^}]*})', r'\1', s).format(**locals())
Out[15]: '3 shrubbery'

d = {'get': 'me'}
d['get'] == d.get # ??
'''