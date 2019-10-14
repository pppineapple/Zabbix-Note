import requests
import json

zabbixurl = "http://{}/zabbix/api_jsonrpc.php".format("10.211.55.4")
user = 'admin'
password = 'zabbix'
jsonrpc = '2.0'
id = 1
headers = {"Contetn-Type": "application/json-rpc"}

# 获取token
token_data = {
            "jsonrpc": jsonrpc,
            "method": "user.login",
            "params": {
                "user": user,
                "password": password
                },
            "id": id,
            "auth": None
            }
token_response = requests.post(zabbixurl, json=token_data, headers=headers)
token_content = json.loads(token_response.content.decode())

# 获取已有的主机信息
host_data = {
    "jsonrpc": jsonrpc,
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip"
        ]
    },
    "id": id,
    "auth": token_content["result"]

}
host_response = requests.post(zabbixurl, json=host_data, headers=headers)
host_content = json.loads(host_response.content.decode())

# 根据主机名查hostid
host_data1 = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "10.211.55.4",
            ]
        }
    },
    "auth": token_content["result"],
    "id": 1
}
host_response1 = requests.post(zabbixurl, json=host_data1, headers=headers)
host_content1 = json.loads(host_response1.content.decode())

hostid = host_content1['result'][0]['hostid']

# 根据hostid查item
item_data = {
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        #"output": "extend",
        "output": [
            "hostid",
            "name",
            "lastvalue"
        ],
        "hostids": hostid,
        "search": {
            "key_": "web_monitor"
        },
        "sortfield": "name"
    },
    "auth": token_content["result"],
    "id": 1
}
item_response = requests.post(zabbixurl, json=item_data, headers=headers)
item_content = json.loads(item_response.content.decode())

# 查看item的最新值
item_content['result'][0]['lastvalue']