import pandas as pd
from pyecharts.charts import Bar, Radar
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.charts import Boxplot

# 读取数据
df = pd.read_csv('data\\data.csv')

# 计算各队伍平均胜率，并将其转换为百分数形式（乘以100并保留两位小数）
team_win_rates = df.groupby('TeamName')['Win rate'].mean().reset_index()
team_win_rates['Win rate'] = team_win_rates['Win rate'].apply(lambda x: round(x * 100, 2))
print(team_win_rates)
bar = Bar(
    init_opts=opts.InitOpts(width="1100px", height="500px")
)
bar.add_xaxis(team_win_rates['TeamName'].tolist())
bar.add_yaxis("平均胜率", team_win_rates['Win rate'].tolist(), category_gap="60%")
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="各队伍平均胜率", subtitle=""),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=45)
    ),
    yaxis_opts=opts.AxisOpts(name="胜率", min_=0, max_=100),
    visualmap_opts=opts.VisualMapOpts(is_show=False, max_=100, min_=0)
)
bar.render("static/charts/team_win_rates.html")

# 准备箱线图数据
data = [df[df['Position'] == pos]['Avg kills'].tolist() for pos in df['Position'].unique()]

print(data)
boxplot = Boxplot(
    init_opts=opts.InitOpts(width="600px", height="400px")
)
boxplot.add_xaxis(df['Position'].unique().tolist())
boxplot.add_yaxis("平均击杀数", boxplot.prepare_data(data), itemstyle_opts=opts.ItemStyleOpts(color="black"))
boxplot.set_global_opts(
    title_opts=opts.TitleOpts(title="不同位置选手平均击杀数分布"),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=45)  # 此处也是修改为axislabel_opts
    ),
    yaxis_opts=opts.AxisOpts(name="平均击杀数")
)
boxplot.render("static/charts/avg_kills_distribution.html")

# 国家分布
# 按照国家进行分组，计算每个国家的选手数量
grouped_data = df.groupby('Country').size()

# 将结果转换为 DataFrame，并命名为 'Count'
country_data = grouped_data.reset_index(name='Count')
print(country_data)
country_pie = (
    Pie(
        init_opts=opts.InitOpts(theme="macarons")
    )
    .add("", [list(z) for z in zip(country_data['Country'], country_data['Count'])])
    .set_global_opts(title_opts=opts.TitleOpts(title=""))
)
country_pie.render("static/charts/country_distribution_chart.html")

# 场均击杀
# 按 Avg kills 排序，ascending=False 表示降序
sorted_df = df.sort_values(by='Avg kills', ascending=False)
avg_kills = sorted_df[['PlayerName', 'Avg kills']]
avg_kills_top10 = avg_kills[0:10]
print(avg_kills_top10)

# 创建Bar实例，用于构建柱状图
bar = Bar(
    init_opts=opts.InitOpts(width="600px", height="300px")
)

# 添加x轴数据，即选手姓名
bar.add_xaxis(avg_kills_top10['PlayerName'].tolist())

# 添加y轴数据，即场均击杀数，并设置系列名称为"场均击杀数"
bar.add_yaxis("场均击杀数", avg_kills_top10['Avg kills'].tolist())

# 设置全局配置项
bar.set_global_opts(

    title_opts=opts.TitleOpts(title="场均击杀榜前十"),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=45),  # 让x轴标签旋转45度，避免文字重叠
    ),
    yaxis_opts=opts.AxisOpts(name="场均击杀数"),  # 设置y轴名称
    visualmap_opts=opts.VisualMapOpts(is_show=False, max_=6, min_=4)
)

bar.render("static/charts/avg_kills_top10.html")

# KDA
kda_top10 = df.sort_values(by='KDA', ascending=False)[['PlayerName', 'KDA']][0:10]
print(kda_top10)

bar = Bar(
    init_opts=opts.InitOpts(width="600px", height="300px")
)
bar.add_xaxis(kda_top10['PlayerName'].tolist())

bar.add_yaxis('场均KDA', kda_top10['KDA'].tolist())

# 设置全局配置项
bar.set_global_opts(

    title_opts=opts.TitleOpts(title="场均KDA前十"),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=45),  # 让x轴标签旋转45度，避免文字重叠
    ),
    yaxis_opts=opts.AxisOpts(name="场均KDA"),  # 设置y轴名称
    visualmap_opts=opts.VisualMapOpts(is_show=False, max_=10, min_=6)
)
bar.render("static/charts/kda_top10.html")

# 辅助野区视野排行
df['custom_sort'] = df['VSPM'] * 25 + df['Avg WPM'] * 25 + df['Avg WCPM'] * 25 + df['Avg VWPM'] * 25
support_top_10 = df.sort_values(by='custom_sort', ascending=False)[
                     ['PlayerName', 'VSPM', 'Avg WPM', 'Avg WCPM', 'Avg VWPM', 'custom_sort']][0:10]
print(support_top_10)

# 创建堆叠柱状图
bar_stacked = Bar(
    init_opts=opts.InitOpts(width="1000px", height="400px", theme='macarons')
)

# 添加 X 轴数据（选手名字）
bar_stacked.add_xaxis(support_top_10['PlayerName'].tolist())

# 添加堆叠柱状图的每一项数据
bar_stacked.add_yaxis("每分钟视野分数", support_top_10['VSPM'].tolist(), stack="stack1")
bar_stacked.add_yaxis("每分钟赢得的野区分数", support_top_10['Avg WPM'].tolist(), stack="stack1")
bar_stacked.add_yaxis("每分钟控制野区分数", support_top_10['Avg WCPM'].tolist(), stack="stack1")
bar_stacked.add_yaxis("每分钟视野控制分数", support_top_10['Avg VWPM'].tolist(), stack="stack1")

# 设置全局配置
bar_stacked.set_global_opts(
    title_opts=opts.TitleOpts(title="辅助野区视野排行"),
    yaxis_opts=opts.AxisOpts(name=""),
    xaxis_opts=opts.AxisOpts(name="选手"),
    legend_opts=opts.LegendOpts(pos_left="right", orient="vertical"),  # 设置图例在左侧
)

# 渲染图表到 HTML 文件
bar_stacked.render("static/charts/support_top_10.html")


# 获取选手 'crisp' 的数据
def get_player_render_data(player_name, file_name):
    player_data = df[df['PlayerName'] == player_name][['KDA', 'KP%', 'CSPerMin', 'GoldPerMin', 'DPM', 'VSPM']].iloc[0]

    # 雷达图的维度
    attributes = ['KDA', 'KP%', 'CSPerMin', 'GoldPerMin', 'DPM', 'VSPM']
    values = player_data.tolist()

    # 配置雷达图
    radar = Radar(
        init_opts=opts.InitOpts(width="350px", height="350px")
    )

    # 定义雷达图的每个维度
    radar.add_schema(
        schema=[
            opts.RadarIndicatorItem(name='KDA', max_=10),
            opts.RadarIndicatorItem(name='击杀参与率', max_=1),
            opts.RadarIndicatorItem(name='每分钟补兵', max_=10),
            opts.RadarIndicatorItem(name='分钟收入金币', max_=500),
            opts.RadarIndicatorItem(name='分钟伤害', max_=800),
            opts.RadarIndicatorItem(name='分钟视野分', max_=5)
        ]
    )

    # 添加数据系列，并设置图例
    radar.add(
        player_name,
        [values],
        color="blue"
    )

    # 设置全局选项
    radar.set_global_opts(
        title_opts=opts.TitleOpts(title=player_name),
        legend_opts=opts.LegendOpts(is_show=True, orient="vertical", pos_left="right")
    )

    radar.render(file_name)


# 我的主队
get_player_render_data('crisp', 'static/charts/crisp_render_data.html')
get_player_render_data('light', 'static/charts/light_render_data.html')
get_player_render_data('xiaohu', 'static/charts/xiaohu_render_data.html')
get_player_render_data('tarzan', 'static/charts/tarzan_render_data.html')
get_player_render_data('breathe', 'static/charts/breathe_render_data.html')

flash = df.groupby('FlashKeybind').size()
flash_data = flash.reset_index(name='flash_group')
print(flash_data)

# 创建饼图
pie = Pie(
    init_opts=opts.InitOpts(width="400px", height="400px")
)

# 添加数据，设置标签格式
pie.add(
    "闪现按键使用情况",
    [list(z) for z in zip(flash_data['FlashKeybind'].tolist(), flash_data['flash_group'].tolist())],
    radius=["30%", "60%"],
    label_opts=opts.LabelOpts(formatter="{b}")
)

# 设置标题
pie.set_global_opts(title_opts=opts.TitleOpts(title="闪现按键"))

# 渲染到本地文件
pie.render("static/charts/flash.html")


# 场均助攻
assists_top10 = df.sort_values(by='Avg assists', ascending=False)[['PlayerName', 'Avg assists']][0:10]
print(assists_top10)

bar = Bar(
    init_opts=opts.InitOpts(width="600px", height="300px", theme="macarons")
)
bar.add_xaxis(assists_top10['PlayerName'].tolist())

bar.add_yaxis('场均助攻', assists_top10['Avg assists'].tolist())

# 设置全局配置项
bar.set_global_opts(

    title_opts=opts.TitleOpts(title="场均助攻前十"),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=45),  # 让x轴标签旋转45度，避免文字重叠
    ),
    yaxis_opts=opts.AxisOpts(name="场均助攻"),  # 设置y轴名称
    visualmap_opts=opts.VisualMapOpts(is_show=False, max_=13, min_=10)
)
bar.render("static/charts/assists_top10.html")


# 场均死亡
deaths_top10 = df.sort_values(by='Avg deaths', ascending=False)[['PlayerName', 'Avg deaths']][0:10]
print(deaths_top10)

bar = Bar(
    init_opts=opts.InitOpts(width="600px", height="300px", theme="macarons")

)
bar.add_xaxis(deaths_top10['PlayerName'].tolist())

bar.add_yaxis('场均死亡', deaths_top10['Avg deaths'].tolist())

# 设置全局配置项
bar.set_global_opts(

    title_opts=opts.TitleOpts(title="场均死亡前十"),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=45),  # 让x轴标签旋转45度，避免文字重叠
    ),
    yaxis_opts=opts.AxisOpts(name="场均死亡"),  # 设置y轴名称
    visualmap_opts=opts.VisualMapOpts(is_show=False, max_=6, min_=4)
)
bar.render("static/charts/deaths_top10.html")
