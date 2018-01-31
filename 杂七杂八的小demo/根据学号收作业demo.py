import os
import re
import xlrd
import xlwt
from xlutils.copy import copy

def listdir(path):
	return os.listdir(path)

#将已交作业的所有文件中分割出所有交了作业的同学的学号
def splitStudentId(filePath):
	tempList = listdir(filePath)
	pattern = re.compile(r'[0-9]{10}')
	resultList = pattern.findall(''.join(tempList))
	resultList.sort()
	return resultList

resultList = splitStudentId(r'E:\庄晨文件\学习文件\Linux\Linux课设报告')
resultDict = {}
for result in resultList:
	resultDict[result] = 1

#打开工作表
readBook = xlrd.open_workbook(r'E:\庄晨文件\学习文件\商务与经济统计\数据挖掘缺勤名单.xls')
writeBook = copy(readBook)
#然后打开工作表中的分页
w_sheet1 = writeBook.get_sheet(0)
r_sheet1 = readBook.sheet_by_index(0)

i = 0
#循环遍历名单中的每一行，将每一行的学号与已交作业的同学学号进行比对，若匹配，则将这一行（这个同学）设置为已交
while i < r_sheet1.nrows:
	row = r_sheet1.row_values(i)
	if row[0] in resultDict and row[5] == 0:
		col = 5
		print(row[0])
		#对相应位置的单元格进行赋值，设置为1，表示已交
		w_sheet1.write(i, col, 1)
	i=i+1

#保存修改，如果路径与原文件相同则进行覆盖，未修改的数据保持不变
writeBook.save(r'E:\庄晨文件\学习文件\商务与经济统计\数据挖掘缺勤名单.xls')

