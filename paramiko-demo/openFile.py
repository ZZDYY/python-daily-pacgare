import paramiko
hostname = "192.168.174.3"
port = 22
username = "root"
password = "123456"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password, allow_agent=True)
sftp_client = client.open_sftp()
remote_file = sftp_client.open("/root/restart_influxdb.sh") #文件路径
try:
  for line in remote_file:
    print(line.strip())
finally:
  remote_file.close()