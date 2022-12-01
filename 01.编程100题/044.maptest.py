from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.options import ToolboxOpts


# 数据要求 [("市",数值)]
data_city = [('广州市', 8), ('东莞市', 2), ('梅州市', 5), ('佛山市', 5), ('汕尾市', 2), ('河源市', 3), ('汕头市', 5), ('潮州市', 3), ('清远市', 3),
             ('湛江市', 3), ('茂名市', 3), ('中山市', 2), ('揭阳市', 2), ('惠州市', 3), ('肇庆市', 3), ('韶关市', 1), ('阳江市', 1)]

province_city = (
    # 构建地图对象
    Map(
        init_opts=opts.InitOpts(bg_color='rgba(253,245,230,0.4)',
                                width='1530px',
                                height='830px',
                                page_title="SHOW"
                                )
        # add三个参数: 名称 数据 地图类型
    ).add("SHOW: ", data_city, "广东")
    # 设置全局配置项 set_global_opts
    .set_global_opts(
        # 设置标题 位置居中 且距离底部 1%
        title_opts=opts.TitleOpts(title="计协招新之广东地区人数统计", pos_left="center", pos_bottom="92%"),
        # 视觉映射
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            # 数据 最大是8 最小是1 -> 设置图例
            pieces=[
                {"min": 1, "max": 2, "lable": "1-3", "color": "#eaffd0"},
                {"min": 3, "max": 4, "lable": "3-4", "color": "#CCEEFF"},
                {"min": 4, "max": 5, "lable": "4-5", "color": "#aa96da"},
                {"min": 5, "max": 6, "lable": "5-6", "color": "#a8d8ea"},
                {"min": 6, "max": 8, "lable": "6-8", "color": "#71c9ce"},

            ]
        ),
        # 展示工具箱
        toolbox_opts=ToolboxOpts(is_show=True)
    )
    # render生成HTML
    .render(path="计协招新之广东地区人数展示.html")
)
