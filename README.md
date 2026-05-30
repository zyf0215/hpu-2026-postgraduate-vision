# hpu-2026-postgraduate-vision

# 📊 基于 2026 河南理工大学考研数据的成绩回归分析与多维交互可视化系统

## 📖 项目故事 (Our Story)
每年考研拟录取名单公布时，大批学子面对官方网站上成百上千条、密密麻麻的 PDF 列表和粘连表格感到无从下手。我们无法直观看到初试高分的人复试表现如何？更看不清各个专业的出分密度和备考容错率。

为了打破这种“信息黑盒”，本项目利用 Python 编写了智能数据清洗程序，提取出河南理工大学 **572 条真实的拟录取全样本数据**，并利用机器学习（一元线性回归模型）进行统计推断。最终，我们摒弃了传统的静态死板图表，选用高雅的**莫兰迪低饱和度学术色系**，构建了具有全样本平铺抖动算法（Jitter）的 HTML5 动态交互可视化系统。

---

## 🌐 线上动态交互演练 (Live Demo)
> **💡 核心亮点：** 本项目已成功部署至云端，评审专家与读者无需配置 Python 环境，点击下方链接即可在浏览器中直接体验多维标签悬停、专业动态筛选等高阶交互：

* 🔗 **[https://你的GitHub用户名.github.io/hpu-2026-postgraduate-vision/postgraduate_analysis.html] 线上交互散点回归矩阵 (图 1.1)** *(注：进入网页后，请将鼠标悬停在点簇或黑色趋势线上查看动态统计公式)*
* 🔗 **[https://你的GitHub用户名.github.io/hpu-2026-postgraduate-vision/postgraduate_boxplot.html] 线上交互全样本沙盘箱线图 (图 1.2)**

---

## 🛠️ 本地工程运行指南 (Getting Started)
1. 将本仓库克隆或下载到本地。
2. 确保本地安装了运行环境：`pip install pandas numpy plotly scikit-learn openpyxl`
3. 运行核心控制程序：`hpu_postgraduate.py`

---
*✨ 本项目为 张一凡 的期末大作业作品，数据源自官方公示，并已对隐私信息进行脱敏处理。*
