#-*- coding: UTF-8 -*
import json
import requests


class ZabbixApi(object):
    def __init__(self, user, password, jsonrpc, id, api_url):
        self.user = user
        self.password = password
        self.jsonrpc = jsonrpc
        self.id = id
        self.api_url = api_url
        self.headers = {"Content-Type": "application/json-rpc"}
        self.token = None

    def get_login_token(self):
        """
        Get zabbix token and assign it to self.token.
        """
        original_data = {
            "jsonrpc": self.jsonrpc,
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.password
            },
            "id": self.id,
            "auth": None
        }
        try:
            response = requests.post(self.api_url, json=original_data, headers=self.headers)
            self.token = json.loads(response.content.decode())["result"]
        except Exception as e:
            print e

    def get_host_info(self, hostname=None):
        """
        get hostid by hostname
        :param hostname: host name List[str,] , default None means we get info of all hosts.
        :return: List[Dict{}] example:[{"hostid": "10107, "host": "10.211.55.4"},]
        """
        original_data = {
            "jsonrpc": self.jsonrpc,
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
            "id": self.id,
            "auth": self.token
        }
        if not hostname:
            original_data["params"]["filter"] = {"host":hostname}
        try:
            response = requests.post(self.api_url, json=original_data, headers=self.headers)
            return json.loads(response.content.decode())['result']

        except Exception as e:
            print e

    def get_item(self, hostid, key):
        """

        :param hostid: List[str,] . A list of hosts you want to get some key_ info.
        :param key_name: str . A Key you want to get.
        :return: List[Dict{},] . A list of host's key info dict.
        """
        original_data = {
            "jsonrpc": self.jsonrpc,
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "search": {
                    "key_": key
                },
                "sortfield": "name"
            },
            "auth": self.token,
            "id": self.id
        }
        try:
            response = requests.post(self.api_url, json=original_data, headers=self.headers)
            return json.loads(response.content.decode())["result"]
        except Exception as e:
            print e


