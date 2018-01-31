'''
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
再思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
'''
'''
import functools


def log(func_str):
	if isinstance(func_str, (int, str)): #传入了字符串参数
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print("%s %s" % (func_str, func.__name__))
				func(*args, **kw)
				print("%s end %s" % (func_str, func.__name__))
				return
			return wrapper
		return decorator
	else: #否则是直接把函数引用传进来
		@functools.wraps(func_str)
		def wrapper(*args, **kw):
			print("call %s" % func_str.__name__)
			func_str(*args, **kw)
			print("end %s" % func_str.__name__)
			return
		return wrapper

#@log #等价于=>now = log(now)
def now():
	print("2017-07-11")

temp = now #保存原来定义的函数对象
now = log(now) #包装
now()

now = log("excute")(temp) #包装
now()
'''
'''
#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, width):
		self.__width = width

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, height):
		self.__height = height

	#这是只读属性，不能修改的
	@property
	def resolution(self):
		return self.__width * self.__height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

#利用os模块编写一个能实现dir -l输出的程序
from datetime import datetime
import os

#获取当前路径的绝对路径
pwd = os.path.abspath(".")

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

#遍历当前路径下的所有文件
for f in os.listdir(pwd):
	#获取这个文件的大小
	fsize = os.path.getsize(f)
	#对这个文件的时间进行格式化输出
	mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')

	#如果这个文件是一个文件夹（即还有子目录）
	if os.path.isdir(f):
		flag = "/"
	else:
		flag = ""
	#对这个文件进行详细输出，即dir -l的功能
	print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

#在pwd路径下创建一个新的文件夹，名为"new folder"
#join()将当前路径与新建路径拼接起来
#os.mkdir(os.path.join(pwd, "new folder"))


#pwd为上面获取的当前路径的绝对路径
def findFile(newPwd, str):
	#遍历当前路径下的所有文件
	for x in os.listdir(newPwd):
		#如果这个文件名包含我们所要寻找的关键字
		if str in x:
			#使用join()将当前路径与文件名拼接起来，形成这个文件的绝对路径
			print(os.path.join(newPwd, x))
		#如果这个文件是个文件夹（还有子目录），则递归去寻找
		if os.path.isdir(x):
			#绝对路径为这个文件夹的绝对路径
			findFile(os.path.join(newPwd, x), str)

findFile(pwd, ".py")
'''

#Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
#首先导入多进程模块
from multiprocessing import Process, Queue
import os, time, random

#负责写数据的进程执行的函数代码
def write(q):
	print("Process to write: %s " % os.getpid())
	for value in ["A", "B", "C"]:
		print("Put %s to queue..." % value)
		#将数据放入queue中
		q.put(value)
		time.sleep(random.random())

#负责读数据的进程执行的函数代码
def read(q):
	print("Process to read: %s " % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)
'''
#接着就是来创建进程了
if __name__ == "__main__":
	q = Queue()
	#创建子进程，将分别要执行的函数传入，并传入相应的函数参数
	pw = Process(target = write, args = (q,))
	pr = Process(target = read, args = (q,))
	#启动进程
	pw.start()
	pr.start()
	#等待pw进程结束
	pw.join()
	#将pr进程强制终止
	pr.terminate()
'''

#请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#someone@gmail.com
#bill.gates@microsoft.com
'''
import re
test = "zhuangb@qq.com"
#()代表我们要提取出来的group，可以通过group(x)来提出相应的匹配()中的内容
re_pattern = re.compile(r"([a-zA-Z][0-9a-zA-Z\.\_]+)\@([0-9a-zA-Z]+.com$)")
if re_pattern.match(test):
	testName = re_pattern.match(test).group(1)
	testDomain = re_pattern.match(test).group(2)
	print("name is %s" % testName)
	print("domain is %s" % testDomain)
else:
	print("failed")

test1 = "<Tom Paris> tom@voyager.org"
re_pattern1 = re.compile(r"\<([a-zA-Z\s]+)\>\s?([a-zA-Z][0-9a-zA-Z\.\_]+)\@([0-9a-zA-Z]+.org$)")
if re_pattern1.match(test1):
	print("name is %s" % re_pattern1.match(test1).group(1))
	print("domain is %s" % re_pattern1.match(test1).group(3))
else:
	print("failed")
'''

#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，
#请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
	#首先将dt_str转为datetime
	dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
	#然后将tz_str转为timezone，这里要用到正则表达式进行分割，取出所要加或减的时间
	tz_group = re.split(r"[UTC\:]+", tz_str)
	#将datetime转为修正过时区的datetime
	tz_hours = int(tz_group[1])
	tz_minutes = int(tz_group[2])
	dt = dt.replace(tzinfo = timezone(timedelta(hours = tz_hours, minutes = tz_minutes))) 
	return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')