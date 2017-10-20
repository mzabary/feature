import yaml

def yaml_load(filepath):
    with open(filepath, 'r') as fd:
        try:
            data = yaml.load(fd)
            #print(data)
            return(data)
        except yaml.YAMLERROR as exc:
            print(exc)
def parse(dic):
    for k, v in dic.items():
        if isinstance(v, dict):
            for p in parse(v):
                yield [k] + p
        else:
            yield [k, v]


def collect_names(node):
    names = []
    while True:
        names.append(node[u'Name'])
        try:
            # deeper node
            node = node[u'Ancestors'][u'BrowseNode']
        except KeyError:
            # we are done, no ancestors
            return names[::-1]

filepath='invoice.yaml'
data=yaml_load(filepath)
lst = list(parse(data))
print(data)
#print(lst)

#print(collect_names(data[u'BrowseNode']))


