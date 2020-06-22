import xlrd
data = xlrd.open_workbook(r'C:\Users\kw445\Desktop\新北勞動參與率vs失業率.xlsx')
table = data.sheets()[0]
X=''
x=table.col_values(0)[1:13]
Y1=''
y1=table.col_values(1)[1:13]
Y2=''
y2=table.col_values(1)[15:27]

import matplotlib.pyplot as plt
import numpy as np
n=12
X=x
Y1=y1
Y2=y2


new_ticks = np.linspace(2007, 2018, 12)
plt.xticks(new_ticks)
plt.xlabel('Year')
plt.ylabel('%')


plt.plot(X, Y1, '*--', label='G1') 
plt.plot(X, Y2, 'rd--', label='G2') 


for x, y1 in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x, y1, '%.2f' % y1 ,ha='center', va='bottom')


for x, y2 in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x, y2, '%.2f' % y2 ,ha='center', va='bottom')


plt.show()
