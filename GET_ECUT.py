import socket
import requests

def GetLocalIPByPrefix(prefix):#获取本机IP
    localIP = ''
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        if ip.startswith(prefix):
            localIP = ip

    return localIP
IP=GetLocalIPByPrefix('172')
requests.get('http://172.21.255.105:801/eportal/?c=Portal&a=login&callback=dr1004&login_method=1&user_account=学号%40运营商&user_password=密码&wlan_user_ip='+IP+'&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=3.3.3&v=8371')
#学号替换成学号；密码替换成密码；运营商一一对应：中国移动——cmcc、电信——telecom、联通——unicom
