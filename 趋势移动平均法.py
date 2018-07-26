import numpy as np
import matplotlib.pyplot as plt

'''
简单移动平均法和加权移动平均法，在时间序列没有明显的趋势变动时，能够准确
反映实际情况。但当时间序列出现直线增加或减少的变动趋势时，用简单移动平均法和
加权移动平均法来预测就会出现滞后偏差。因此，需要进行修正，修正的方法是作二次
移动平均，利用移动平均滞后偏差的规律来建立直线趋势的预测模型。这就是趋势移动
平均法。

下面讨论如何利用移动平均的滞后偏差建立直线趋势预测模型。
设时间序列{yt} 从某时期开始具有直线趋势，且认为未来时期也按此直线趋势变
化，则可做直线趋势预测模型 yˆt+T = at + btT ， T = 1,2....
'''
# 模拟数据
data = [676, 825, 774, 716, 940, 1159, 1384, 1524, 1668, 1688, 1958,
        2031, 2234, 2566, 2820, 3006, 3093, 3277, 3514, 3770, 4107]
data_index = np.array(range(1, 22))  # 索引，作图用
data_np = np.array(data, dtype=np.float)  # 转成数组
plt.plot(data_index, data_np, color='b', linewidth=2, label='原始数据')  # 原始数据展示
plt.show()


def moav(data_index, data_np, n) ->(np.array, np.array, int, float):
    '''
    求数据的移动平均，及索引（移动平均索引应该在对应值加一为对应原始数据索引）
    输入参数 索引，数组，移动平均n值，以及是否第一次移动平均，是1，不是0
    返回 索引，移动平均值，n,以及误差值
    '''
    t = len(data_np)
    data_out = []  # 结果列表
    for x in range(0, t - n + 1):
        data_use = data_np[x:x + n]
        data_out.append(sum(data_use) / n)  # 最后结果
        data_index_out = data_index[n - 1:]  # 索引
    data_out_np = np.array(data_out)
    # 测量误差计算
    data_in_np = data_np[n:]  # 原始数据
    data_out_np_two = data_out_np[:-1, ]  # 结果数据,最后一个为预测数据舍弃
    s = sum((data_out_np_two - data_in_np)**2 / (t - n))**0.5  # 预测标准误差
    return(data_index_out, data_out_np, n, s)


# 一次移动平均， N＝ 6
n = 6
a, b, x, z = moav(data_index, data_np, n)
# 二次移动平均 N＝ 6
n = 6
c, d, k, y = moav(a, b, n)

# M21(1)为一次移动平均， M21(2)二次移动平均
m211 = b[-1]
m212 = d[-1]
# 平滑指数计算
at = 2 * m211 - m212
bt = 2 / (n - 1) * (m211 - m212)

# 得到方程y = at + bt * t
y22 = at + bt * (22 - 21)
y23 = at + bt * (23 - 21)

# 预测数据展示
plt.scatter(data_index, data_np, color='b',
            linewidth=2, label='原始数据')  # 原始数据展示
plt.scatter([22, 23], [y22, y23], color='r',
            linewidth=2, label='原始数据')  # 原始数据展示
plt.show()
