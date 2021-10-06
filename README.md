# frpscan
扫描frp默认配置主机

## fofa:
status_code="502" && port="7000" && title=="502 Bad Gateway"
## 原理：
frp默认配置7000端口 无需鉴权即可使用通道 红队可通过此方法使用代理


python模拟操作 运行frpc和不同的配置文件，通过爬虫查看是否将端口映射出去来验证是否存在
## 优化：
1、增加多线程

2、对爬取内容进行正则匹配

3、对多个端口进行映射测试
## 链接:
https://github.com/xiaojiangxl/frpscan
