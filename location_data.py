# coding: utf-8

import openpyxl, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

df = pd.read_excel("data.xlsx")

sh=[]; bj=[]; gd=[]; js=[]; zj=[]; hb=[]; qt=[]

for k in df['企业地点']:
	if k == '上海':
		sh.append(k)

	elif k == '北京':
		bj.append(k)

	elif k == '广东':
		gd.append(k)

	elif k == '江苏':
		js.append(k)

	elif k == '浙江':
		zj.append(k)

	elif k == '湖北':
		hb.append(k)

	else:
		qt.append(k)


len_local = pd.Series([len(sh), len(bj), len(gd), len(js), len(zj), len(hb),  len(qt)], index = ['ShangHai', 'Beijing', 'GuangDong', 'JiangSu', 'ZheJiang', 'HuBei', 'Other'])

#创建绘图 / 饼图 pie(数据，数据对应的标签，百分比小数点后两位)
fig = plt.figure()
plt.pie(len_local.values, labels=len_local.index, autopct='%1.2f%%')
plt.title('Company distribution')
plt.savefig('img/location_pie.png')

#创建绘图 / 柱状图 pie(x轴，y轴，颜色)
fig_2 = plt.figure()
plt.bar(len_local.index, len_local.values, color='green')
plt.title('Company distribution')
plt.savefig('img/location_bar.png')

plt.show()
