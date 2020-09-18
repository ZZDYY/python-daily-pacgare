## Paramiko介绍
> paramiko是一个基于python编写的、使用ssh协议的模块，跟xshell和xftp功能类似，支持加密与认证，可以上传下载和访问服务器的文件。
可以利用paramiko模块写服务器脚本，在本地执行，比如持续更新代码，查看日志，批量配置集群等。
paramiko 主要包含SSHClient和SFTPClient两个组件：

### SSHClient

ssh服务会话的表示，通常用来执行命令，主要有connect、exec_command、load_system_host_keys和set_missing_host_key_policy方法。

- connect：建立SSH远程连接并校验。
- exec_command：执行指令并返回结果。
- load_system_host_keys：加载本地公钥校验文件。
- save_host_keys: 将主机密钥保存回文件。只有主机密钥通过load_host_keys加载主机密钥才能被保存--而不是load_system_host_keys加载的秘钥
- get_host_keys： 获取主机秘钥
- set_log_channel :设置log管道
- set_missing_host_key_policy：远程主机没有本地主机密钥或HostKeys时的策略。
- invoke_shell:交互式会话
- open_sftp:文件传输
- get_transport：获取底层的 transport 对象, 用于执行低级的任务


#### 异常: 
- BadHostKeyException        无法验证服务器的主机密钥
- AuthenticationException    认证失败
- SSHException               连接或建立 SSH 会话时出现任何其他错误   
- socket.error               连接时发生套接字错误
#### connect
- hostname(str类型)，连接的目标主机地址；
- port(int类型)，连接目标主机的端口，默认为22；
- username(str类型)，校验的用户名(默认为当前的本地用户名)；
- password(str类型)，密码用于身份校验或解锁私钥；
- pkey(Pkey类型)，私钥方式用于身份验证；
- key_filename(str or list(str)类型)，一个文件名或文件名列表，用于私钥的身份验证；
- timeout(float类型)，一个可选的超时时间(以秒为单位)的TCP连接；
- allow_agent(bool类型)，设置为False时用于禁用连接到SSH代理；
- look_for_keys(bool类型)，设置为False时用于来禁用在～/.ssh中搜索私钥文件；
- compress(bool类型)，设置为True时打开压缩。
- sock(类型 socket),一个打开的socket或类似socket的对象 如 Channel，用来和主机通信
- gss_auth(类型bool),是否用GSS-API认证
- gss_kex(bool)，用GSS-API key交换做用户认证
- gss_deleg_creds(bool),是否委托GSS-API客户端凭据
- gss_host(str),kerberos数据库中的目标名称。默认值：主机名
- gss_trust_dns(bool),指示是否信任DNS以安全规范化所连接主机的名称（默认 True）。
- banner_timeout(float),等待SSH标语显示的可选超时（以秒为单位）。
- auth_timeout(float),等待验证响应的可选超时（以秒为单位）
- disabled_algorithms(dict),个直接传递给Transport其的可选dict 及其名称相同的关键字参数。
### SFTPClient

SFTP客户端对象，实现远程文件操作，主要有from_transport、put、get、Mkdir、remove、rename、stat、listdir等方法。

- from_transport：从已通过验证的传输对象简历连接。
- put：上传本地文件到服务器上。
- get：从服务器下载文件到本地。
- get_channel：返回Channel此SFTP会话的基础对象
- getfo：下载文件, 本地打开一个文件句柄用于写入远程服务的数据
- putfo：上传文件, 参数类似于 getfo
- getcwd ：获取当前 sftp 会话所在目录
- listdir_attr：以类似于 ls -l 的格式列出指定路径下的所有文件目录列表(包括以隐藏文件), 默认 sftp 会话所在目录
- listdir_iter：生成器版本的listdir_attr
- open：在远程服务器上打开文件, 参数和 python 的 open() 函数相同
- readlink：返回符号链接的原始路径
- symlink：创建符号链接
- file： 在远程服务器上打开一个文件
- normalize：返回给定路径的标准化路径
- posix_rename、rename：重命名文件或文件夹
- Mkdir、remove、rename、stat、listdir、chmod、chown：创建目录、删除目录、重命名文件或目录、获取文件信息、获取指定目录中的列表、更改文件的权限、更改文件的所有者（uid）和组（gid）



[项目demo](https://github.com/paramiko/paramiko/tree/master/demos)