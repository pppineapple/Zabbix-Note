#-*- coding: UTF-8 -*import os
from zabbix_api import ZabbixApi

api_url = "http://{}/zabbix/api_jsonrpc.php".format("10.211.55.4")
zabbix_api = ZabbixApi("Admin","zabbix","2.0",1, api_url)

zabbix_api.get_login_token()
print(zabbix_api.token)

zabbix_api.get_host_info()
zabbix_api.get_item("10107",["agent.version"])
