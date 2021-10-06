import time
import requests
import os
def frp(host):
    with open("./tmp.ini","w") as f:
        f.write("[common]\nserver_addr = "+host+"\nserver_port = 7000\n\n[http]\ntype = tcp \nlocal_ip = 127.0.0.1\nlocal_port = 80\nremote_port = 7090")
    cmd="frpc.exe -c tmp.ini"
    os.system(cmd)
    time.sleep(10)
    url="http://"+host+":7090"
    page=requests.get(url)
    if(page.status_code==200):
        with open("./success.txt",'a') as ff:
            ff.write(str(host))
            print(str(host))
    else:
        with open("./failure.txt","a") as fff:
            fff.write(str(host))
if __name__ == "__main__":
    while True:
        try:
            with open("./host.txt","r") as f:
                for line in f.readlines():
                    frp(line)
        except:
            pass