import numpy as np
import matplotlib.pyplot as plt


# 模拟数据
# 1--11月份的销售金额
data = [533.8, 606.9, 574.6, 547, 609.8,
        563.4, 572, 616.4, 592.7, 563.9, 615.1]
data_index = np.array(range(1, 12))  # 索引，作图用
data_np = np.array(data, dtype=np.float)  # 转成数组
plt.plot(data_index, data, color='b', linewidth=2, label='原始数据')  # 原始数据展示
plt.show()

'''
移动平均法
是根据时间序列资料逐渐推移，依次计算包含一定项数的时序平均数，
以反映长期趋势的方法。当时间序列的数值由于受周期变动和不规则变动的影响，起伏
较大，不易显示出发展趋势时，可用移动平均法，消除这些因素的影响，分析、预测序列的长期趋势。
移动平均法有简单移动平均法，加权移动平均法，趋势移动平均法等。
'''
# 简单移动平均法
'''
简单移动平均法只适合做近期预测，而且是预测目标的发展趋势变化不大的情况。
如果目标的发展趋势存在其它的变化， 采用简单移动平均法就会产生
较大的预测偏差和滞后。
'''

# 总期数 t
# 移动平均的项数 n （n<t）
# 预测标准误差 s
t = len(data)
n = 4
data_index_out = []
data_out = []
for x in range(0, t - n + 1):
    data_use = data[x:x + n]
    data_index_out.append(x + n + 1)  # 结果索引
    data_out.append(sum(data_use) / n)  # 最后结果


# 测量误差
data_in_np = data_np[n:]  # 原始数据
data_out_np = np.array(data_out)[:-1, ]  # 结果数据
s = sum((data_out_np - data_in_np)**2 / (t - n))**0.5  # 预测标准误差


plt.plot(data_index_out, data_out, color='r',
         linewidth=2, label='结果数据')  # 结果数据展示
plt.plot(data_index, data, color='b', linewidth=2, label='原始数据')  # 原始数据展示

plt.show()


# 加权移动平均
'''
在简单移动平均公式中，每期数据在求平均时的作用是等同的。但是，每期数据
所包含的信息量不一样，近期数据包含着更多关于未来情况的信心。因此，把各期数据
等同看待是不尽合理的，应考虑各期数据的重要性，对近期数据给予较大的权重，这就
是加权移动平均法的基本思想。

在加权移动平均法中， wt 的选择，同样具有一定的经验性。一般的原则是：近期
数据的权数大，远期数据的权数小。至于大到什么程度和小到什么程度，则需要按照预
测者对序列的了解和分析来确定。
'''
# 总期数 t
# 移动平均的项数 n （n<=t）
# 预测标准误差 s
t = len(data)
n = 4
data_index_out = []
data_out = []
Weighting = np.array([1, 2, 3, 4])  # 加权
for x in range(0, t - n + 1):
    data_use = data_np[x:x + n]
    data_index_out.append(x + n + 1)  # 结果索引
    data_out.append(sum(data_use * Weighting) / sum(Weighting))  # 最后结果

# 测量误差
data_in_np = data_np[n:]  # 原始数据
data_out_np = np.array(data_out)[:-1, ]  # 结果数据
s = sum((data_out_np - data_in_np)**2 / (t - n))**0.5  # 预测标准误差

# 预测结果修正
out = sum(data_out_np) / sum(data_in_np) * data_out_np[-1]
# 展示
plt.plot(data_index_out, data_out, color='r',
         linewidth=2, label='结果数据')  # 结果数据展示
plt.plot(data_index, data, color='b', linewidth=2, label='原始数据')  # 原始数据展示

plt.show()

