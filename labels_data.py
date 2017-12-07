# coding:utf-8

import openpyxl, matplotlib
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

df = pd.read_excel('data.xlsx')

# 创建18个空list对应18种公司类型
for i in range(1,19):
	locals()['label_' + str(i)] = []

for labels in df['企业类型']:
	if labels == '教育':
		label_1.append(labels)
	if labels == '金融':
		label_2.append(labels)
	if labels == '汽车交通':
		label_3.append(labels)
	if labels == '房产服务':
		label_4.append(labels)
	if labels == '医疗健康':
		label_5.append(labels)
	if labels == '旅游':
		label_6.append(labels)
	if labels == '本地生活':
		label_7.append(labels)
	if labels == '游戏':
		label_8.append(labels)
	if labels == '广告营销':
		label_9.append(labels)
	if labels == '硬件':
		label_10.append(labels)
	if labels == '文化娱乐':
		label_11.append(labels)
	if labels == '企业服务':
		label_12.append(labels)
	if labels == '社交网络':
		label_13.append(labels)
	if labels == '电子商务':
		label_14.append(labels)
	if labels == '工具软件':
		label_15.append(labels)
	if labels == '体育运动':
		label_16.append(labels)
	if labels == '物流':
		label_17.append(labels)
	if labels == '农业':
		label_18.append(labels)				

len_labels = []
for i in range(1,19):
	k = len(locals()['label_' + str(i)])
	len_labels.append(k)

quantity = pd.Series(len_labels, index=['教育','金融','汽车交通','房产服务','医疗健康','旅游','本地生活','游戏','广告营销','硬件','文化娱乐','企业服务','社交网络','电子商务','工具软件','体育运动','物流','农业'])

fig = plt.figure()
plt.pie(quantity.values, labels=quantity.index, autopct='%1.2f%%')
plt.title('Business type')
plt.savefig('img/labels_pie.png')

fig_2 = plt.figure()
plt.barh(quantity.index, quantity.values)
plt.grid(True)
plt.title('Business type')
plt.savefig('img/labels_bar.png')

plt.show()