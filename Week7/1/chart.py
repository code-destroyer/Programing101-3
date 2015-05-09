from matplotlib import pyplot
from histogram import Histogram
from req import Links


class Chart:

    def make_chart(labels, values):
        dict_histogram = Links.load_results('servers_by_groups.json')
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
        explode = (0.1, 0.1, 0.1, 0.1)
        labels = []
        sizes = []
        for servers in dict_histogram:
            labels.append(servers)
            sizes.append(dict_histogram[servers])

        pyplot.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90)
        pyplot.axis('equal')
        pyplot.savefig("chart.png")
        pyplot.show()

h = Histogram()
labels = h.dict_histogram.keys()
values = h.dict_histogram.values()
chart = Chart.make_chart(labels, values)
