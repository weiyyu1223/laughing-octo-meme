import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']      # Windows
# plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB']  # Mac 用这行
plt.rcParams['axes.unicode_minus'] = False

# ==================== 数据 ====================
days = np.arange(7)    #代表一周7天（数字索引）
week_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

# 更新后的气温数据
high = [31, 33, 35, 30, 31, 33, 31]   # 最高温
low  = [22, 22, 20, 20, 21, 25, 22]   # 最低温
diff = np.array(high) - np.array(low)  # 温差

# ==================== 创建画布 ====================
fig, axes = plt.subplots(2, 1, figsize=(10, 9), dpi=100)   #创建 2 行 1 列 的子图网格  画布尺寸：宽度10英寸，高度9英寸

# ==================== 第1个图：折线图 高温  低温====================
axes[0].plot(days, high, color='red', marker='o', linewidth=2, label='最高温')
axes[0].plot(days, low, color='blue', marker='s', linewidth=2, label='最低温')

axes[0].set_xticks(days)
axes[0].set_xticklabels(week_labels)
axes[0].set_title('北京一周温度变化（最高/最低温）', fontsize=14)
axes[0].set_xlabel('日期')
axes[0].set_ylabel('温度（℃）')
axes[0].legend(loc='best')
axes[0].grid(True, linestyle='--', alpha=0.6)
axes[0].set_ylim(15, 40)  # Y轴范围为15~40

# ==================== 第2个图：柱状图（温差） ====================
axes[1].bar(days, diff, color='green', alpha=0.7, edgecolor='black', label='温差')

# 柱顶标注数值
for i, v in enumerate(diff):
    axes[1].text(i, v + 0.3, str(v), ha='center', fontsize=10)

axes[1].set_xticks(days)
axes[1].set_xticklabels(week_labels)
axes[1].set_title('北京一周温差变化（最高温 - 最低温）', fontsize=14)
axes[1].set_xlabel('日期')
axes[1].set_ylabel('温差（℃）')
axes[1].legend(loc='best')
axes[1].grid(True, linestyle='--', alpha=0.5, axis='y')

# ==================== 顶端 ====================
fig.suptitle('北京未来一周天气趋势分析', fontsize=18, y=0.995)
fig.tight_layout(pad=2.0)

# 保存
plt.savefig('weather.png', dpi=100, bbox_inches='tight')
plt.show()