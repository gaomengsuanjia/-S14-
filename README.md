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

***
## 数据示例：
| TeamName | PlayerName | Position | Games | ...  | Penta Kills | Solo Kills | Country | FlashKeybind |
| -------- | ---------- | -------- | ----- | ---- | ----------- | ---------- | ------- | ------------ |
|Top Esports|369|Top|8|...|0|2|China|D|
|Dplus KIA|aiming|Adc| 9     |...|0|2|South Korea|F|
|MAD Lions KOI|alvaro|Support|5|...|0|0|Spain|D|
|...|...|...|...|...|...|...|...|...|
|LNG Esports|zika|Top|8|...|0|2|China|D|
***
## 数据总览：

![战队平均胜率](https://github.com/user-attachments/assets/6a78d114-5b25-4b94-8705-5a95f13a1f4a)


![选手国家分布](https://github.com/user-attachments/assets/24f6e1ad-8761-40be-b61d-5e48979eb047)


***

## 主要数据

![场均击杀榜](https://github.com/user-attachments/assets/1a22dbfa-e730-476b-aa9c-2d49a23c545c)

![场均KDA榜](https://github.com/user-attachments/assets/438d32c2-9de6-4eff-bfc5-6c9dbae5e97a)

![场均死亡榜](https://github.com/user-attachments/assets/3fbcd5c1-697d-4c59-9af6-0f47f31821cb)

![场均助攻榜](https://github.com/user-attachments/assets/40a7ef25-2689-4892-9116-9531c254def1)

****

**其中每分钟视野分数(VSPM)、每分钟赢得的野区分数(每分钟赢得的野区分数)、每分钟控制野区分数(Avg WCPM)、每分钟视野控制分数(Avg VWPM)各自的权重为1，可自行更改**

![辅助野区视野排行](https://github.com/user-attachments/assets/620ce513-d15e-40e3-9339-a4ac9b1b2a6a)

**各位置场均击杀箱形图：**

![各位置场均击杀](https://github.com/user-attachments/assets/4e7ced62-49ce-4769-aeef-f38bd820e839)

![闪现按键](https://github.com/user-attachments/assets/bdd2ea3f-94a2-4e3f-a168-e246d5526b47)

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

![我的主队1](https://github.com/user-attachments/assets/ab48dd7f-af6c-4d04-9017-be9a4fde6786)

![我的主队2](https://github.com/user-attachments/assets/988e6c1a-bc22-4863-8538-320517a0c6a5)


***

## 整体效果

![整体效果1](https://github.com/user-attachments/assets/ff870245-1f67-4949-a63c-f9683356d952)

![整体效果2](https://github.com/user-attachments/assets/f320fcfa-703f-49de-ac89-d8e92b63d433)

![整体效果3](https://github.com/user-attachments/assets/1fa46789-2af2-487b-bf87-6385de34b154)

![整体效果4](https://github.com/user-attachments/assets/657c30b2-0e28-4542-ac1f-08145f60663d)

> 完整效果请访问生成的 HTML 页面

***

## 如何运行

1. 克隆此项目：

   ```git
   git clone https://github.com/gaomengsuanjia/-S14-.git
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


