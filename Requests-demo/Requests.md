## Requests
### 介绍
> Requests是用python语言基于urllib编写的，采用的是Apache2 Licensed开源协议的HTTP库。与urllib相比，Requests更加方便，可以节约我们大量的工作，建议爬虫使用Requests库。

### 请求方式
- get：请求指定的页面信息，并返回实体主体。（查询）
- post：请求服务器接受所指定的文档作为对所标识的URI的新的从属实体。(添加)
- put：从客户端向服务器传送的数据取代指定的文档的内容。(更新)
- delete：请求服务器删除指定的页面。（删除）
- head：只请求页面的首部。
- options：为了网站安全先发一个options请求 （跨域访问）
- patch: 更新url连接（更新 一般url参数）
- request:

### requests.request
> 发送一个request请求

- method：请求类型（GET、OPTIONS、HEAD、POST、PUT、PATCH、DELETE）
- url：请求url
- params:query参数，url参数 类型 dict、list of tuples or bytes 
- data：body参数  类型：Dict, list of tuples, bytes, or file-like object
- json：json序列化python对象传入body
- headers：http请求头信息 类型dict
- cookies：cookie  类型 dict or CookieJar 对象
- files：请求上传的文件 类型 dict {"文件名"：文件对象}
- auth: http auth认证 类型 Auth tuple to enable Basic/Digest/Custom HTTP Auth
- timeout： 等待超时时间  类型 float or tuple (connect timeout, read timeout) 
- allow_redirects:表示允许跟踪 GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD 方法的重定向 类型 bool  默认 True
- proxies：用于将协议映射为代理的URL 类型 dict
- verify: 是否验证TLS证书  值为 str是 为CA路径
- stream： 是否立即下载响应内容  类型 bool
- cert: 为字符串时应是 SSL 客户端证书文件的路径(.pem格式)，如果是元组，就应该是一个('cert', 'key') 二元值对
- 返回值为 Response 对象




#### json 和 data区别
1. 不管json是str还是dict，如果不指定headers中的content-type，默认为application/json

2. data为dict时，如果不指定content-type，默认为application/x-www-form-urlencoded，相当于普通form表单提交的形式

3. data为str时，如果不指定content-type，默认为application/json

4. 用data参数提交数据时，request.body的内容则为a=1&b=2的这种形式，用json参数提交数据时，request.body的内容则为'{"a": 1, "b": 2}'的这种形式

### response
> 属性：content', 'status_code', 'headers', 'url', 'history', 'encoding', 'reason', 'cookies', 'elapsed', 'request'
- apparent_encoding:chardet库的返回编码
- content：响应的内容，以字节为单位。
- cookies：服务器发送回的Cookie的CookieJar
- elapsed：从发送请求到响应到达之间经过的时间，此属性专门测量发送请求的第一个字节与完成头解析之间所花费的时间。因此，它不会因使用响应内容或stream关键字参数的值而受到影响。
- encoding：访问r.text时进行编码以进行解码。
- headers：不区分大小写的响应header字典
- history:Response请求历史记录中的对象列表。任何重定向响应都将在此处结束。该列表从最早的请求到最新的请求进行排序。
- is_permanent_redirect:如果此响应是重定向的永久版本之一，则为True
- is_redirect：如果此响应是可以自动处理的格式良好的HTTP重定向，则为True
- ok:如果status_code小于400，则返回True 。
- next:如果有重定向请求，则为重定向链中的下一个请求返回PreparedRequest
- text：响应的内容，以unicode表示。
- links：返回响应的已解析头链接
- iter_content()：遍历响应数据
- iter_lines()：按行变量响应数据
- json()：返回响应的json编码内容
- url:响应的最终URL位置。
- request:一个响应的对象
- reason:响应HTTP状态的文本原因，例如“未找到”或“确定”
- status_code:响应的HTTP状态的整数代码，例如404或200。
- raise_for_status():HTTPError如果发生一次，则进行存储
- close():将连接释放回池中，即关闭连接，通常不需要调用
- raw：响应的类似文件的对象表示形式（用于高级用法）。使用的raw要求stream=True是在请求上设置的。

### 响应状态码
##### 信息性状态码
100：（'continue'，），
101：（'switching_protocols'，），
102：（'processing'，），103：（'checkpoint'，），
122：（'uri too_long，'request_uri_too_long'），

#### 成功状态码
200：（ok"，‘okay'，'allok'，‘all_okay'，'all_good'，'\\o/'，'√），
201：（'created'，），202：（accepted'，），
203：（'non authoritative info'，'non authoritative_information'），
204：（'no content'，），
205：（'reset content'，'reset'），
206：（'partial_content'，‘partial'），
207：（'multi status'，‘multiple_status'，'multi_stati'，'multiple_stati'），
208：（'already reported'，），
226：（'im_used'，），

#### 重定向状态码
300：（'multiple_choices'，），
301：（"moved_permanently'，'moved'，'\\o-'），
302：（'found，），
303：（'see_other'，‘other’），
304：（'not_modified"，），
305：（'use_proxy'，），
306：（'switch_proxy'，），
307：（'temporary_redirect'，‘temporary_moved"，'temporary'），
308：（'permanent redirect’
resume_incomplete'，'resume'，），#These 2 to be removed in 3.o

#### 客户端错误状态码
400：（"bad_request"，'bad'），
401：（“unauthorized'，）’
402：（“payment_required'，‘payment"），
403：（'forbidden'，），
404：（'not found'，-o-'），
405：（method not allowed'，'not_allowed’），
406：（'not acceptable'，），
407：（"proxy_authentication_required'，‘proxy_auth'，'proxy_authentication"），
408：（‘request_timeout'，'timeout"），
409：（‘conflict'，），
410：（'gone'，），
411：（iength required'，），
412：（"precondition_failed'，‘precondition'），
413：（request_entity too_large'，），
414：（request_uri_too_large'，），
415：（'unsupported media type'，'unsupported media'，'media type'），
416：（"requested_range not_satisfiable'，‘requested_range'，"range_not_satisfiable'），
417：（expectation_failed，），
418；（im_a teapot"，'teapot'，'i am a teapot'），
421：（'misdirected request'，
422：（"unprocessable_entity'，'unprocessable'），
423：（locked"，），
424：（'failed_dependency'，‘dependency'），
425：（'unordered collection'，'unordered'），
426：（'upgrade required"，'upgrade'），
428：（precondition_required"，'precondition'），
429：（'too_many_requests'，'too_many'），
431：（"header_fields_too_large'，‘fields_too_large'），
444：（'no response'，'none'），449：（'retry with'，'retry'），
450：（'blocked_by windows parentalcontrols'，‘parental_controls'），
451：（'unavailable_for_legal_reasons'，‘1egal_reasons'），
499：（'client_closed request7，），

#### 服务端错误状态码
500：（internal_server_error'，'server error'，‘/o\\"，'x'），
501：（'not implemented"，），
502：（‘bad_gateway'，），
503：（'service_unavailable'，‘unavailable'），
504：（'gateway_timeout'，），
505：（"http_version_not_supported"，"http version"），
506：（"variant also negotiates'，），
507：（"insufficientstorage"，），
509：（"bandwidth 1imit_exceeded'，‘bandwidth'），
510：（'not extended'，），
511：（network_authentication_required"，'network_auth'，‘network authentication'）