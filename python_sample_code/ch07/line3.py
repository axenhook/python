from bokeh.plotting import figure, show

p = figure(width=800, height=400, title="零花钱统计")
p.title_text_color = "green"
p.title_text_font_size = "18pt"
p.xaxis.axis_label = "年龄"
p.xaxis.axis_label_text_color = "violet"
p.yaxis.axis_label = "零花钱"
p.yaxis.axis_label_text_color = "violet"
dashs = [12, 4]
listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
p.line(listx1, listy1, line_width=4, line_color="red", line_alpha=0.3, line_dash=dashs, legend="男性")
listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
p.line(listx2, listy2, line_width=4, legend="女性")
show(p)
