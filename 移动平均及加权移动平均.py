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


'''
附加说明

时间序列是按时间顺序排列的、随时间变化且相互关联的数据序列。分析时间序
列的方法构成数据分析的一个重要领域，即时间序列分析。
时间序列根据所研究的依据不同，可有不同的分类。
1．按所研究的对象的多少分，有一元时间序列和多元时间序列。
2．按时间的连续性可将时间序列分为离散时间序列和连续时间序列两种。
3．按序列的统计特性分，有平稳时间序列和非平稳时间序列。如果一个时间序列
的概率分布与时间t 无关，则称该序列为严格的（狭义的）平稳时间序列。如果序列的
一、二阶矩存在，而且对任意时刻t 满足：
（ 1）均值为常数
（ 2）协方差为时间间隔τ 的函数。
则称该序列为宽平稳时间序列，也叫广义平稳时间序列。我们以后所研究的时间序列主
要是宽平稳时间序列。
4．按时间序列的分布规律来分，有高斯型时间序列和非高斯型时间序列。
1 确定性时间序列分析方法概述
时间序列预测技术就是通过对预测目标自身时间序列的处理，来研究其变化趋势
的。一个时间序列往往是以下几类变化形式的叠加或耦合。
（ 1）长期趋势变动。它是指时间序列朝着一定的方向持续上升或下降，或停留在
某一水平上的倾向，它反映了客观事物的主要变化趋势。
（ 2）季节变动。
（ 3）循环变动。通常是指周期为一年以上，由非季节因素引起的涨落起伏波形相
似的波动。
（ 4）不规则变动。通常它分为突然变动和随机变动。
通常用
Tt
表示长期趋势项， St 表示季节变动趋势项， Ct 表示循环变动趋势项， Rt
表示随机干扰项。常见的确定性时间序列模型有以下几种类型：
（ 1）加法模型
yt = Tt + St + Ct + Rt
（ 2）乘法模型
yt = Tt ⋅ St ⋅ Ct ⋅ Rt
（ 3）混合模型
yt = Tt ⋅ St + Rt
yt = St + Tt ⋅Ct ⋅ Rt
其中 yt 是观测目标的观测记录， E(Rt ) = 0 ， E(Rt2 ) = σ 2 。
如果在预测时间范围以内，无突然变动且随机变动的方差σ 2 较小，并且有理由认
为过去和现在的演变趋势将继续发展到未来时，可用一些经验方法进行预测
'''
