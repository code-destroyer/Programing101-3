class Histogram:

    def __init__(self):
        self.dict_histogram = {}

    def __str__(self):
        for key, count in self.dict_histogram.items():
            print("{}: {}".format(key, count))

    def add(self, string):
        if string not in self.dict_histogram:
            self.dict_histogram[string] = 1
        else:
            self.dict_histogram[string] += 1

    def count(self, string):
        if string in self.dict_histogram:
            return self.dict_histogram[string]
        else:
            return None

    def get_dict(self):
        return self.dict_histogram


h = Histogram()

h.add("Apache")
h.add("Apache")
h.add("nginx")
h.add("IIS")
h.add("nginx")

print(h.count("Apache"))
print(h.count("nginx"))
print(h.count("IIS"))
print(h.count("IBM Web Server"))

print(h.get_dict())
