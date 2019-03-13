#!/usr/local/bin/python3

from matplotlib import pyplot
from openpyxl import load_workbook

wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']

def getvalue(x): return x.value

year=list(map(getvalue, sheet['A'][1:]))
temp=list(map(getvalue, sheet['C'][1:]))
activity=list(map(getvalue, sheet['D'][1:]))

pyplot.plot(year, temp, label="Относительная температура")
pyplot.plot(year, activity, label="Активность ")

pyplot.show()
