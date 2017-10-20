import yaml
'''
# xyz.yaml file
username: admin
password: admin
ip_address: 192.168.1.1
command: pass
'''
with open("xyz.yaml", 'r') as dict_data:
    try:
        yaml_data = yaml.load(dict_data)
        print(yaml_data)
        #{'username': 'admin', 'command': 'pass', 'password': 'admin', 'ip_address': '192.168.1.1'}
        print(type(yaml_data))
        #< class 'dict'>
    except yaml.YAMLERROR as exc:
        print(exc)

with open("xyz.yaml", 'r') as login_data:
    try:
        yaml_data = yaml.load(login_data)
        print(yaml_data)
        #{'password': 'admin', 'ip_address': '192.168.1.1', 'username': 'admin', 'command': 'pass'}
        ipaddress = yaml_data['ip_address']
        #print(ipaddress)
        #192.168.1.1
        user_name = yaml_data['username']
        passwrd = yaml_data['password']
        commnd = yaml_data['command']
    except yaml.YAMLERROR as e:
        print(e)

