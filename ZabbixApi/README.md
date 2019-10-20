## Zabbix Python API
这周看了一下Zabbix的[API接口文档](https://www.zabbix.com/documentation/3.4/zh/manual/api)，发现python可以直接调用Zabbix的接口进行一些查询，创建，修改，删除的操作(比如：获取监控主机信息、创建监控项、设置自动发现规则等等)。

ZabbixAPi的获取主要是通过HTTP远程请求来调用API的。
> ####执行请求
设置前端后，你就可以使用远程HTTP请求来调用API。为此，需要向 api_jsonrpc.php 位于前端目录中的文件发送HTTP POST请求。例如，如果你的Zabbix前端安装在 http://company.com/zabbix， 那么用HTTP请求来调用 apiinfo.version 方法就如下面这样：
>
> ```
> POST http://company.com/zabbix/api_jsonrpc.php HTTP/1.1
Content-Type: application/json-rpc
> 
>{"jsonrpc":"2.0","method":"apiinfo.version","id":1,"auth":null,"params":{}}
> ```
> 
> 请求的 Content-Type 头部必须设置为以下值之一： application/json-rpc, application/json 或 application/jsonrequest。

那我们在使用python来编写程序调用Zabbix API时主要使用到**requests**和**json**包模拟一个http请求，然后获得对应的json格式的数据。

## 我的想法
我想在学习Zabbix的过程中，自己尝试编写一个python模块专门来调用Zabbix API。先从一些小的功能开始，然后一步一步熟悉zabbix的功能，再利用python调用zabbix api实现那些功能。

## 更新状态
* 2019-10-20
	* 创建了ZabbixApi类。
	* 编写了根据用户名和密码获取zabbix token的方法
	* 编写获取zabbix host id的方法
	* 编写获取指定host id的监控项item的信息的方法


