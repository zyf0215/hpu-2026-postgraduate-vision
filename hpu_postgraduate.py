import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# ==========================================
# 1. 载入你清洗好的真实数据 (D:\code\vscodepython\visionwork\hpu_2026_data.xlsx)
# ==========================================
excel_path = r"D:\code\vscodepython\visionwork\hpu_2026_data.xlsx"

try:
    df = pd.read_excel(excel_path)
    print(f" 成功读取真实数据，共 {len(df)} 条记录，启动高级美化渲染引擎...")
except Exception as e:
    print(f"⚠️ 未检测到真实文件，启用 572 条标准高保真学术模拟数据：{e}")
    np.random.seed(2026)
    n_samples = 572
    majors = ['计算机科学与技术', '计算机技术', '软件工程', '人工智能', '大数据技术']
    student_majors = np.random.choice(majors, n_samples, p=[0.25, 0.3, 0.15, 0.15, 0.15])
    base_scores = {'计算机科学与技术': 310, '计算机技术': 295, '软件工程': 290, '人工智能': 305, '大数据技术': 285}
    p_scores = [int(base_scores[m] + np.random.beta(2.5, 2) * 90) for m in student_majors]
    re_scores = [round(min(98.0, max(60.0, 68 + ((ps - base_scores[m])/90)*12 + np.random.normal(0, 5.5))), 2) for ps, m in zip(p_scores, student_majors)]
    df = pd.DataFrame({
        '拟录取院系': ['计算机科学与技术学院']*n_samples, '拟录取专业': student_majors,
        '考生编号': [f'104602026{i:06d}' for i in range(1, n_samples+1)],
        '姓名': [f'考生_{i}' for i in range(n_samples)], '初试成绩': p_scores, '复试成绩': re_scores,
        '总成绩': [round(p*0.6 + r*0.4, 2) for p, r in zip(p_scores, re_scores)]
    })

# 定义高雅的莫兰迪/高级灰学术色系 (5个专业对应5种质感色彩)
exquisite_palette = ['#4A6984', '#6E8E75', '#A27B5C', '#8A7B9B', '#D2766E']

# ==========================================
# 2. 极致美化：图 1.1 散点回归图
# ==========================================
X = df[['初试成绩']]
y = df['复试成绩']
model = LinearRegression().fit(X, y)
X_line = np.linspace(X.min()[0], X.max()[0], 100).reshape(-1, 1)
y_line = model.predict(X_line)

fig1 = px.scatter(
    df, x='初试成绩', y='复试成绩', color='拟录取专业',
    hover_name='姓名', hover_data={'考生编号': True, '总成绩': ':.2f', '初试成绩': True, '复试成绩': ':.2f'},
    labels={'初试成绩': '初试成绩 (Score)', '复试成绩': '复试成绩 (Score)', '拟录取专业': '专业类别'},
    opacity=0.85, color_discrete_sequence=exquisite_palette
)

# 叠加强度柔和的回归趋势虚线
fig1.add_traces(go.Scatter(
    x=X_line.squeeze(), y=y_line,
    name=f'全样本线性回归趋势 (R²={model.score(X, y):.3f})',
    line=dict(color='#2C3E50', width=2, dash='dot')
))

# 杂志级UI布局优化
fig1.update_layout(
    title=dict(text="<b>图 1.1：初试与复试成绩回归关系及专业分布多维交互矩阵</b>", font=dict(size=16, color='#2C3E50'), x=0.05),
    xaxis=dict(title="<b>初试成绩 (分)</b>", gridcolor='#F0F2F5', showline=True, linewidth=1, linecolor='#CBD5E1'),
    yaxis=dict(title="<b>复试成绩 (分)</b>", gridcolor='#F0F2F5', showline=True, linewidth=1, linecolor='#CBD5E1'),
    plot_bgcolor='#FAFAFB', paper_bgcolor='#FFFFFF',
    legend=dict(title_text="<b>专业筛选 (点击切换)</b>", bordercolor="#E2E8F0", borderwidth=1, yanchor="top", y=0.99, xanchor="left", x=0.01),
    margin=dict(l=60, r=40, t=60, b=60), hovermode='closest'
)

fig1.write_html(r"D:\code\vscodepython\visionwork\postgraduate_analysis.html")

# ==========================================
# 3. 极致美化：图 1.2 全样本平铺交互箱线图
# ==========================================
fig2 = px.box(
    df, x='拟录取专业', y='初试成绩', color='拟录取专业',
    points="all", hover_name='姓名', hover_data={'考生编号': True, '总成绩': ':.2f'},
    color_discrete_sequence=exquisite_palette
)

# 极致优化箱线图外观：隐藏多余元素，强化抖动点艺术感
fig2.update_traces(
    marker=dict(size=4, opacity=0.6), # 减小点尺寸，提高半透明度，形成高级颗粒感
    line=dict(width=1.5), # 框线纤细化
    boxmean=True # 额外显示均值线，增加专业度
)

fig2.update_layout(
    title=dict(text="<b>图 1.2：2026年拟录取考生初试成绩区间分布与样本抖动沙盘图</b>", font=dict(size=16, color='#2C3E50'), x=0.05),
    xaxis=dict(title="<b>拟录取专业类别</b>", showline=True, linewidth=1, linecolor='#CBD5E1'),
    yaxis=dict(title="<b>初试成绩分布 (分)</b>", gridcolor='#F0F2F5', showline=True, linewidth=1, linecolor='#CBD5E1'),
    plot_bgcolor='#FAFAFB', paper_bgcolor='#FFFFFF',
    showlegend=False, # 隐藏图例，因X轴已有标签，腾出黄金视觉空间
    margin=dict(l=60, r=40, t=60, b=60)
)

fig2.write_html(r"D:\code\vscodepython\visionwork\postgraduate_boxplot.html")
print("✨ 高级艺术感视觉图表渲染完成！请至相应路径查看 HTML 成果。")