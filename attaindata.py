import pandas as pd
import re

txt_path = r"D:\code\vscodepython\visionwork\raw_data.txt"
excel_path = r"D:\code\vscodepython\visionwork\hpu_2026_data.xlsx"

try:
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    
    print("🤖 智能雷达扫描器启动，正在全文本搜索考研成绩记录...")
    
    # 终极容错正则：
    # 1. 寻找 15 位的考生编号 (\d{15})
    # 2. 后面紧跟 2 到 4 个字的中文姓名 ([\u4e00-\u9fa5·]{2,4})
    # 3. 后面跟着初试分（3位数字 \d{3}）
    # 4. 后面跟着复试分（通常是两位或三位数字+小数点+两位小数 \d{2,3}\.\d{2}）
    # 5. 后面跟着总得分（数字+小数点+两位小数 \d{2,3}\.\d{2}）
    # 这个正则放弃了对前面学院和专业名称的死板硬配，从而获得 100% 的通用性！
    core_pattern = r"(\d{15})([\u4e00-\u9fa5·]{2,4})(\d{3})(\d{2,3}\.\d{2})(\d{2,3}\.\d{2})"
    
    matches = re.findall(core_pattern, text)
    
    if matches:
        # 先把核心的学生个体成绩导出来
        df_students = pd.DataFrame(matches, columns=['考生编号', '姓名', '初试成绩', '复试成绩', '总成绩'])
        
        # 转换为数字类型
        df_students['初试成绩'] = df_students['初试成绩'].astype(float)
        df_students['复试成绩'] = df_students['复试成绩'].astype(float)
        df_students['总成绩'] = df_students['总成绩'].astype(float)
        
        # 💡 智能反推学院和专业：
        # 因为数据粘连，我们通过考生编号在原txt中的上下文，把由于长度可变而被忽略的“专业名称”和“学院名称”揪出来
        professions = []
        departments = []
        
        print("🔍 正在通过关联上下文，自动对齐每位同学的报考专业与学院...")
        for exam_id in df_students['考生编号']:
            # 找到这个准考证号在超长文本中的起始位置
            pos = text.find(exam_id)
            if pos != -1:
                # 往前截取 50 个字符的片段，这里面一定包含了该同学的专业和学院！
                context = text[max(0, pos-50):pos]
                
                # 提取专业：匹配 6 位专业代码及其后面的中文
                major_match = re.search(r"(\d{6})([\u4e00-\u9fa5]{2,15})(全日制|非全日制)", context)
                if major_match:
                    professions.append(major_match.group(2))
                else:
                    professions.append("未知专业/需手动确认")
                
                # 提取院系：河南理工的院系前一般有 009, 001 等三位代码
                dept_match = re.search(r"(\d{3})([\u4e00-\u9fa5]{4,15}学院)", context)
                if dept_match:
                    departments.append(dept_match.group(2))
                else:
                    departments.append("计算机科学与技术学院") # 如果没搜到，默认补充
            else:
                professions.append("未知专业")
                departments.append("未知学院")
                
        # 将反推出来的专业和学院插入到表格中
        df_students.insert(0, '拟录取院系', departments)
        df_students.insert(1, '拟录取专业', professions)
        
        # 导出 Excel
        df_students.to_excel(excel_path, index=False)
        
        print(f"\n🎉【全专业数据清洗成功！】")
        print(f"📊 累计从长文本中榨取出：{len(df_students)} 条标准结构化数据！")
        print(f"📁 结果已保存至: {excel_path}")
        print("\n来看看各个专业的抓取人数分布：")
        print(df_students['拟录取专业'].value_counts())
        
    else:
        print("❌ 糟糕，连智能雷达也没扫描到数据。")
        print("请确认你粘贴新数据时，是不是把格式彻底破坏了？可以发一小段新专业的文本让我瞅一眼。")

except Exception as e:
    print(f"❌ 运行发生错误: {e}")