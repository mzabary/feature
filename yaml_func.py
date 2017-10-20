import yaml
# ytub    Learn Python and Make Games

def yaml_load(filepath):
    with open(filepath, 'r') as fd:
        try:
            data = yaml.load(fd)
            print(data)
            print(yaml.dump(data,default_flow_style=False))
            return(data)
        except yaml.YAMLERROR as exc:
            print(exc)
def yaml_dump(filepath, data):
    with open(filepath, 'w') as fd:
        yaml.dump(data,fd)

if __name__ == '__main__':

    filepath='yaml2.yaml'
    data = yaml_load(filepath)
    print(data)
'''
    filepath2= 'yaml3.yaml'
    data2= {"items": {
        "sward":100,
        "axe":80,
        "boots":40
    }}
    yaml_dump(filepath2, data2)
#,default_flow_style=False

'''
