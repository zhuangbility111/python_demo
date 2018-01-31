import math	#意思是导入math这个包
from functools import reduce #使用reduce()函数要导这个包


a = 80.5 / (1.75 * 1.75)
if a >= 18.5:
	print("过轻")
elif a > 18.5 and a <= 25:
	print("正常")
elif 28 >= a > 25:
	print("过重")
elif 32 >= a > 28:
	print("肥胖")

#求二元一次方程的解
def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
	x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
	return x1, x2	
print(quadratic(2,3,1))



#求杨辉三角
def triangles():
	row = [1]
	newrow = row
	a = 1
	while(a <= 10):
		yield newrow #此处将newrow添加到generator中
		newrow = [1] + [row[i] + row[i+1] for i in range(0, len(row)-1)] + [1]
		row = newrow
		a = a+1
	return
for t in triangles(): #遍历generator
	print(t)


#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def normalize(name):
	return name[0].upper() + name[1:].lower()

names = ['adam', 'LISA', 'barT']
print(list(map(normalize, names)))

#请编写一个prod()函数，可以接受一个list并利用reduce()求积
def multiply(x1, x2):
	return x1 * x2
def prod(L):
	return reduce(multiply, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s] #前面是一个dict，根据s选中的键来返回相应的值

def addAll(x1, x2):
	return x1*10 + x2

def str2float(s):
	str = s.replace(".", "")
	if "." in s:
		index = len(s) - s.index(".") - 1
	else:
		index = 0
	return reduce(addAll, list(map(char2num, str)))/10**index
print('str2float(\'123.45987908\') =', str2float('123.45987908'))


#利用filter()函数来将从1-999中不是回数的去掉

def is_palindrome(n):
	s = str(n)
	i, j = 0, len(s)-1
	while(i < j):
		if(s[i] != s[j]):
			break
		i = i + 1
		j = j - 1
	if(i < j):
		return False
	else:
		return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))


#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
def by_name(t):
	return t[0]

def by_score(t):
	return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_name) #sorted()会使用key指向的函数处理每一个元素，然后组成一个新的list，再对新list进行排序，并返回排序结果
L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L3 = sorted(L1, key = by_score, reverse = True) #reverse参数是说明是否要反转排序
print(L3)
