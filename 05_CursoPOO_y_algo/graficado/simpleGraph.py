from bokeh.plotting import figure, output_file, show

if __name__=="__main__":
    output_file("simpleGraph.html")
    fig = figure()
    n = int(input("Size of vals: "))
    x_vals = list(range(n))
    y_vals=[]
    for x in x_vals:
        y_vals.append(int(input(f"Valor de y para {x}: ")))
    fig.line(x_vals,y_vals,line_width=2)
    show(fig)