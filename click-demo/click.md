## Click

### 介绍
> Click 是 Flask 的团队 pallets 开发的优秀开源项目，它为命令行工具的开发封装了大量方法，使开发者只需要专注于功能实现  
>下面是一个简单demo:
```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()
```
运行结果
```shell
python hello.py --count=3
Your name: John
Hello John!
Hello John!
Hello John!
```

### 装饰器
### command
> 创建一个新的Command并将修饰的函数用作回调。这还将自动将所有修饰的option()和argument()作为参数附加到命令
#### group
> 创建一个新Group的函数作为回调
#### argument
> 将参数附加到命令。所有位置参数都作为参数声明传递给Argument; 所有关键字参数均按原样转发（除外cls）。这等效于Argument手动创建实例并将其附加到Command.params列表。
#### option
> 将选项附加到命令。所有位置参数都作为参数声明传递给Option; 所有关键字参数均按原样转发（除外cls）。这等效于Option手动创建实例并将其附加到Command.params列表。
#### password_option
> 密码提示的快捷方式。  
> 等效于

```python
@click.command()
@click.option('--password', prompt=True, confirmation_prompt=True,
              hide_input=True)
def changeadmin(password):
    pass
```
#### confirmation_option
> 确认提示的快捷方式，可以通过--yes作为参数传递来忽略

> 等效于

```python
def callback(ctx, param, value):
    if not value:
        ctx.abort()

@click.command()
@click.option('--yes', is_flag=True, callback=callback,
              expose_value=False, prompt='Do you want to continue?')
def dropdb():
    pass
```
#### version_option
> 添加一个--version选项，该选项可立即结束程序并打印出版本号。这是作为一个渴望的选项实现的，该选项可打印版本并在回调中退出程序。
#### help_option
> 添加一个--help选项，该选项立即结束程序打印出帮助页面。通常无需添加，因为默认情况下已将其添加到所有命令，除非被禁止。
#### pass_context
> 将回调标记为希望接收当前上下文对象作为第一个参数。
#### pass_obj
> 与相似pass_context()，但仅在向前的上下文（Context.obj）中传递对象。如果该对象表示嵌套系统的状态，这将很有用。
#### make_pass_decorator
> 给定一个对象类型，这将创建一个装饰器，该装饰器的工作方式类似于pass_obj()但不传递当前上下文的对象，而是查找type的最内部上下文 object_type()。


### 实用工具
#### echo
> 将消息和换行符打印到给定的文件或标准输出中。乍一看，它看起来像打印功能，但是它改进了对处理Unicode和二进制数据的支持，无论系统配置多么糟糕，它们都不会失败。

**参数**
- message:要打印的消息
- file:要写入的文件（默认为stdout）
- err:如果设置为true，则文件默认为stderr而不是 stdout，这比调用get_text_stderr()更快更容易 。
- nl:如果设置为True（默认值），则会在后面打印换行符。
- color:控制终端是否支持ANSI颜色。默认为自动检测。

#### echo_via_pager
> 此函数获取文本，并通过stdout上特定于环境的pager显示它。

**参数**
- text_or_generator ：文本到页面，或者生成器，将文本发送到页面
- color ：控制pager是否支持ANSI颜色。默认为自动检测
#### prompt
> 提示用户输入。这是一项便利功能，可用于提示用户稍后输入

**参数**
- text：要显示的提示文字
- default ：如果没有输入发生时使用的默认值。如果未提供，它将提示直到中止
- hide_input :如果将其设置为true，则输入值将被隐藏。
- Confirmation_prompt :要求确认该值
- type :用于检查值的类型
- value_proc :如果提供此参数，则将调用该函数而不是类型转换来转换值
- prompt_suffix:添加到提示的后缀
- show_default :在提示中显示或隐藏默认值
- err :如果设置为true，则文件默认为stderr而不是 stdout，与echo相同。
- show_choices : 如果传递的类型是Choice，则显示或隐藏选择
#### confirm
>提示确认
- text :要询问的问题
- default ：默认提示内容
- abort ：如果将其设置为True，错误答案会引发一次并中止程序
- prompt_suffix ：添加到提示的后缀
- show_default ：在提示中显示或隐藏默认值
- err ：如果设置为true，则文件默认为stderr而不是 stdout，与echo相同。

#### progressbar
> 此功能创建一个可迭代的上下文管理器，可用于在显示进度条时迭代某些内容

示例：
```python
with progressbar(items) as bar:
    for item in bar:
        do_something_with(item)
```
> 如果未指定可迭代的对象，则可以通过update（）方法手动更新进度条，而不是直接迭代进度条

```python
with progressbar(length=chunks.total_bytes) as bar:
    for chunk in chunks:
        process_chunk(chunk)
        bar.update(chunks.bytes)
```
**参数**
- iterable：可迭代对象。如果未提供，则要求length 
- length ：要迭代的数目，默认情况下，进度条将尝试向迭代器询问其长度，该长度可能有效也可能无效，如果还提供了迭代器，则此参数可用于覆盖长度。如果未提供iterable，则进度条将在该长度范围内进行迭代。
- label ：显示在进度条旁边的标签
- show_eta ：启用或禁用估计时间显示。如果无法确定长度，则会自动禁用。
- show_percent ：启用或禁用百分比显示。如果可迭代对象的长度为默认值，则默认为True；否则为 False。
- show_pos ：启用或禁用绝对位置显示。默认值为False
- item_show_func ：当前项目调用的函数，该函数可以返回字符串以在进度条旁边显示当前项目。请注意，当前项目可以为None！
- fill_char ：用于显示进度条的填充部分的字符
- empty_char ：用于显示进度条中未填充部分的字符
- bar_template ：用作条形模板的格式字符串。其中的参数label用于标签， bar进度条和info信息部分
- info_sep ：多个信息项（eta等）之间的分隔符
- width ：进度条的宽度，以字符为单位，0表示完整的终端宽度
- file ：要写入的文件。如果这不是终端，则仅打印标签
- color ：控制终端是否支持ANSI颜色。默认为自动检测
#### clear
> 清除终端屏幕。这将具有清除终端的整个可见空间并将光标移到左上方的效果。如果未连接到终端，则不会执行任何操作
#### style
> 使用ANSI样式设置文本样式并返回新字符串。默认情况下，样式是自包含的，这意味着在字符串的末尾会发出一个重置代码。这可以通过来防止reset=False。

支持的颜色名称
- black （可能是灰色）
- red
- green
- yellow （可能是橙色）
- blue
- magenta
- cyan
- white （可能是浅灰色）
- bright_black
- bright_red
- bright_green
- bright_yellow
- bright_blue
- bright_magenta
- bright_cyan
- bright_white
- reset （仅重置颜色代码）

**参数**
text :ANSI码样式化的字符串
fg:如果提供，它将成为前景色
bg:如果提供，它将成为背景色
bold：如果提供，将启用或禁用粗体模式
dim：如果提供，将启用或禁用暗淡模式。对此的支持很差
underline：如果提供，则将启用或禁用下划线
blink：如果提供，将启用或禁用闪烁
reverse：如果提供，则将启用或禁用反向渲染（前景变为背景，反之亦然）
reset：默认情况下，在字符串的末尾添加一个全部重置代码，这意味着样式不会保留。可以禁用此功能来构成样式。

#### unstyle
> 从字符串中删除ANSI样式信息。通常不需要使用此功能，因为Click的echo功能会在必要时自动删除样式
#### secho
> 此功能将echo()与style()到一个调用中。因此，以下两个调用是相同的：
#### edit
> 在定义的编辑器中编辑给定的文本

**参数**
- text：要编辑的文字
- editor ：要使用的编辑器，默认自动检测
- env ：将环境变量转发给编辑器。
- require_save： –如果为true，则不保存在编辑器中将使返回值变为None。
- extension :告诉编辑者的扩展名。默认为.txt，但更改此设置可能会更改语法突出显示
- filename :如果提供，它将编辑此文件，而不是提供的文本内容。在这种情况下，它将不会使用临时文件作为间接文件。
  
#### launch
> 此函数在默认查看器应用程序中针对该文件类型启动给定的URL（或文件名）。如果这是一个可执行文件，则可能会在新会话中启动该可执行文件。返回值是已启动应用程序的退出代码。通常，0表示成功。

**参数**
- url:要启动的事物的URL或文件名
- wait :等待程序停止
- locate ：如果将其设置为True，则与其启动与URL相关联的应用程序，不如尝试启动具有所定位文件的文件管理器。如果URL不指向文件系统，这可能会产生奇怪的影响
#### getchar
> 从终端获取单个字符并返回它,这将始终返回一个unicode字符，在极少数情况下，它可能会返回多个字符。返回多个字符的情况是，无论出于何种原因，多个字符最终出现在终端缓冲区中，或者标准输入实际上不是终端。
#### pause
> 此命令停止执行，并等待用户按任意键继续。这类似于Windows批处理“暂停”命令。如果程序未通过终端运行，则此命令将不执行任何操作

**参数**
- info ：暂停前要打印的信息字符串。
- err ：如果设置为message stderr而不是 stdout，则与echo相同
#### get_terminal_size
>以列和行的形式以元组形式返回终端的当前大小
#### get_binary_stream
> 返回用于字节处理的系统流。这从本质上从sys模块返回具有给定名称的流，但是它解决了不同Python版本之间的一些兼容性问题。首先，此功能对于在Python 3上获取二进制流是必需的。
#### get_text_stream
>返回用于文本处理的系统流。通常，这会返回从其返回的二进制流周围的包装流， get_binary_stream()但是对于已正确配置的流，它也可以在Python 3上采用快捷方式
#### open_file
> 这类似于File工作原理，但需要手动使用。默认情况下，文件以非惰性打开。如果'-'通过，这可以打开常规文件以及stdin / stdout

**参数**
- filename：要打开的文件名（或'-'用于stdin / stdout）
- mode ：打开文件的模式
- encoding ：使用的编码。
- errors ：此文件的错误处理
- lazy ：设置为true 延迟打开文件
- atomic ：在原子模式下，写入将进入一个临时文件，并在关闭时移动。
#### get_app_dir
> 返回应用程序的配置文件夹。默认行为是返回最适合操作系统的内容。

**参数**
- app_name:应用程序名称。应正确将其大写，并可以包含空格
- roaming :控制文件夹是否应在Windows上漫游。否则没有影响
- force_posix :如果将其设置为True，则在任何POSIX系统上，该文件夹将以带引号的形式存储在主文件夹中，而不是XDG config home或darwin的应用程序支持文件夹。
#### format_filename
> 格式化文件名以供用户显示。此功能的主要目的是确保可以完全显示文件名。如有必要，它将以不失败的方式将文件名解码为unicode。（可选）它可以缩短文件名，使其不包含文件名的完整路径。


[项目demo](https://github.com/pallets/click/tree/master/examples)