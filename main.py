# https://gitub.com/malam-x

import subprocess, socket, socks
import _winreg as winreg

internet_settings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_ALL_ACCESS)

proxy,proxy1 = winreg.QueryValueEx(internet_settings, "ProxyServer")
enable,enable1 = winreg.QueryValueEx(internet_settings, "ProxyEnable")

print(proxy)
print(proxy1)
proxy_divided = proxy.split(':')
print(proxy_divided[0])
print(proxy_divided[1])

s = socks.socksocket()
proxyIP= p roxy_divided[0]
port_proxy = proxy_divided[1]
shellproxy = True

try:
    if shellproxy == True:
        s = socks.socksocket()
        s.setproxy(socks.PROXY_TYPE_HTTP,proxy,port_proxy)
        # if you need username and password authentication, use:
        # s.setproxy(socks.PROXY_TYPE_HTTP, proxyaddrs, proxyportn, True, username, password)
        s.connect(("www.google.com", 80))
        shellinfo = "GET / HTTP/1.1\r\n\r\n"
        print(shellinfo)
        s.sendall(shellinfo)
        banner = s.recv(1024)
        print(banner)
    else:
        s.connect(("www.google.com", 80))
        shellinfo = "GET / HTTP/1.1\r\n\r\n"
        print(shellinfo)
        s.sendall(shellinfo)
        banner = s.recv(1024)
        print(banner)
except socket.error:
    s.close()
    time.sleep(30)
