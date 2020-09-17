import paramiko
#服务器信息，主机名（IP地址）、端口号、用户名及密码
hostname = "192.168.174.3"
port = 22
username = "root"
password = "123456"
#创建SSH对象 
client = paramiko.SSHClient()
#自动添加策略，保存服务器的主机名和密钥信息
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
client.connect(hostname, port, username, password, allow_agent=True)
# 执行linux命令
stdin, stdout, stderr = client.exec_command('ls /')
for line in stdout:
  print('... ' + line.strip('\n')) 
#or
print(stdout.readlines())