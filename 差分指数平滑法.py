# 差分指数平滑法
'''
在前面我们已分析过，指数平滑值实际上是一种加权平均数。因此把序列中逐期增
量的加权平均数（指数平滑值）加上当前值的实际数进行预测，比一次指数平滑法只用
变量以往取值的加权平均数作为下一期的预测更合理。 从而使预测值始终围绕实际值上
下波动，从根本上解决了在有直线增长趋势的情况下，用一次指数平滑法所得出的结果
始终落后于实际值的问题。

差分指数平滑就是对增长幅度进行指数平滑预测
'''

import numpy as np
import matplotlib.pyplot as plt


# 模拟数据
data = [24, 26, 27, 30, 32, 33, 36, 40, 41, 44]
data_index = np.array(range(1, len(data) + 1))  # 索引，作图用
data_np = np.array(data, dtype=np.float)  # 转成数组
plt.plot(data_index, data_np, color='b', linewidth=2, label='原始数据')  # 原始数据展示
plt.show()

# 一阶差分可以做直线趋势预测
# 求差分
chafen = data_np[1:] - data_np[:-1]


# 指数平滑函数
def moav_index(data_np, y1, a)->(np.array, float):
    '''
    输入目标数组，初始值，平滑指数
    返回，一次平滑值，和标准误差
    '''
    out = [y1]  # 结果赋值初始化数据
    for x in range(0, len(data_np)):  # 最后一个数据为预测数据
        predict = a * data_np[x] + (1 - a) * out[-1]
        out.append(predict)
    out_np = np.array(out)  # 输出数据转np
    s = sum((out_np[:-1] - data_np)**2 / len(data_np))**0.5  # 预测标准误差
    return(out_np, s)


alf = 0.4
a, b = moav_index(chafen, chafen[0], alf)
# 预测值
out = a[1:] + data_np[1:]

# 二阶差分
'''
当时间序列呈现二次曲线增长时，可用二阶差分指数平滑模型来预测
'''
data = [676, 825, 774, 716, 940, 1159, 1384, 1524, 1668, 1688, 1958,
        2031, 2234, 2566, 2820, 3006, 3093, 3277, 3514, 3770, 4107]
data_index = np.array(range(1, len(data) + 1))  # 索引，作图用
data_np = np.array(data, dtype=np.float)  # 转成数组
plt.plot(data_index, data_np, color='b', linewidth=2, label='原始数据')  # 原始数据展示
plt.show()

# 求一阶差分
chafen1 = data_np[1:] - data_np[:-1]
# 二阶差分
chafen2 = chafen1[1:] - chafen1[:-1]
# 二阶差分的指数平滑
alf = 0.1
a, b = moav_index(chafen2, chafen2[0], alf)
# 预测
out = a[1:] + chafen1[1:] + data_np[2:]
data_out_index = np.array(range(3, len(out) + 3))  # 索引，作图用
plt.plot(data_index, data_np, color='b', linewidth=2, label='原始数据')  # 原始数据展示
plt.plot(data_out_index, out, color='r', linewidth=2, label='数据')  # 原始数据展示
plt.show()
