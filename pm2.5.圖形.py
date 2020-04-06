import requests, time, json, sys, os
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
#%matplotlib inline

start = datetime(2020, 3, 18, 0, 0)

axis_x = []
axis_y1 = []
axis_y2 = []
for i in range(24):
    ftime = start.strftime("%Y%m%d%H%M")
    #filename = os.path.join(os.getcwd(), "datas", "pm25", f"pm25_{ftime}.json")
    filename = f"D:\\pm25_{ftime}.json"

    try:
        with open(filename, 'r', encoding="UTF-8") as f:
            datas = json.loads(f.read())
            axis_x.append(start.strftime("%H"))
            axis_y1.append(int(datas[7]['PM25']))
            axis_y2.append(int(datas[8]['PM25']))
            #print(datas[7]['Site'], start.strftime("%H")+", ", datas[7]['PM25'])
    except:
        print(filename, sys.exc_info())
        axis_y1.append(-1)

    start = start + timedelta(hours=1) 

plt.rcParams['font.family']='DFKai-SB' #顯示中文 for Windows10
plt.figure(dpi=120,linewidth = 2)
plt.plot(axis_x,axis_y1,'o-',color = 'g', label=datas[7]['Site'])
plt.plot(axis_x,axis_y2,'X-',color = 'b', label=datas[8]['Site'])
plt.legend()
plt.title(datetime(2020, 3, 18, 0, 0).strftime("%Y%m%d")+" PM2.5 趨勢圖")
plt.show()
