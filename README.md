# 英雄联盟S14世界赛选手数据可视化

## 项目简介

> 这是一个基于 PyEcharts 的数据可视化小项目，展示了英雄联盟 S14 世界赛选手的关键数据表现，适合作为数据可视化课程作业或兴趣项目。

**项目特点：**

- 数据源权威，来源于 Kaggle。
- 涉及多种可视化类型，包括柱状图、箱形图、雷达图等。
- 共包含 14 个可视化图表，分布在 3 个 HTML 页面中，方便浏览与展示。

## 数据来源

数据来自 Kaggle 平台的 [2024 LoL Championship Player Stats & Swiss Stage](https://www.kaggle.com/datasets/anmatngu/2024-lol-championship-player-stats-and-swiss-stage)。

- 数据涵盖选手的各项核心指标，如 KDA、场均击杀、场均死亡等。
- 细化到每分钟视野分数、野区控制等高级数据。

## 数据总览：

![战队平均胜率](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126003227281.png)

![选手国家分布](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126003342263.png)



***

## 主要数据

![场均击杀榜](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126003438484.png)

![场均KDA榜](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126003458850.png)

![场均死亡榜](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126003516411.png)

![场均助攻榜](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126003539273.png)

****

**其中每分钟视野分数(VSPM)、每分钟赢得的野区分数(每分钟赢得的野区分数)、每分钟控制野区分数(Avg WCPM)、每分钟视野控制分数(Avg VWPM)各自的权重为1，可自行更改**

![辅助野区视野排行](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126003627091.png)

**各位置场均击杀箱形图：**

![各位置场均击杀](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126004021015.png)

![闪现按键](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126004101790.png)

***

## 我的主队

**共有五个选手的雷达图**

六大维度：

- KDA
- KP% (击杀参与率)
- CSPerMin (每分钟补刀数)
- GoldPerMin (每分钟经济)
- DPM (每分钟伤害)
- VSPM (每分钟视野分数)

![我的主队1](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126004202316.png)

![我的主队2](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126004222226.png)

***

## 整体效果

![整体效果1](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126004434139.png)

![整体效果2](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126004447792.png)

![整体效果3](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126004503807.png)

![整体效果4](C:\Users\HP\AppData\Roaming\Typora\typora-user-images\image-20241126004520842.png)

> 完整效果请访问生成的 HTML 页面

***

## 如何运行

1. 克隆此项目：

   ```git
   git clone <repo-url>
   ```

2. 安装所需依赖：

   ```
   pip install pyecharts
   ```

3. 运行代码生成 HTML 页面：

   ```
   python main.py
   ```

4. 在浏览器中打开生成的 HTML 文件，欣赏可视化效果(推荐使用谷歌)


