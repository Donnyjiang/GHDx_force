import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
# uniform_data = np.random.rand(10, 12)  # 自定义数据
# ax = sns.heatmap(uniform_data)
# values = np.random.rand(3, 3)
values = np.loadtxt(open("/home/jiangdingyi/jdy/force/heat_map/result.csv", "rb"), delimiter=",", skiprows=0)
# x_ticks = ['x-1', 'x-2', 'x-3']
# y_ticks = ['y-1', 'y-2', 'y-3']  # 自定义横纵轴
ax = sns.heatmap(values) #xticklabels=x_ticks, yticklabels=y_ticks)
ax.set_title('Heatmap for test')  # 图标题
ax.set_xlabel('x label')  # x轴标题
ax.set_ylabel('y label')
plt.show()
figure = ax.get_figure()
figure.savefig('/home/jiangdingyi/jdy/force/heat_map/result.jpg')  # 保存图片