from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

c = (
    Map(init_opts=opts.InitOpts(bg_color='rgba(0,0,0,0.2)',
                                width='1500px',
                                height='820px',
                                page_title='广东地区人数分析',
                                ))
    .add("商家A", [list(z) for z in zip(Faker.guangdong_city, Faker.values())], "广东")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-广东地图"), visualmap_opts=opts.VisualMapOpts()
    )
    .render("map_guangdong.html")
)


"""
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.options.global_options import ThemeType

x_data = ['分类1', '分类2', '分类3', '分类4', '分类5', '分类6', '分类7', '分类8', '分类9', '分类10', '分类11', '分类12', '分类13', '分类14', '分类15',
          '分类16', '分类17']
y_data = [0.72, 0.61, 0.98, 0.92, 0.67, 0.87, 0.6, 0.75, 0.96, 0.68, 0.71, 0.49, 0.35, 0.76, 0.81, 0.45, 0.51]
instance_bar = (
    Bar(init_opts=opts.InitOpts(bg_color='rgba(255,250,205,0.2)',
                                width='1000px',
                                height='600px',
                                page_title='page',
                                theme=ThemeType.MACARONS
                                )
        )
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(yaxis_data=y_data, series_name='aaa')
)
instance_bar.render('11.html')
"""