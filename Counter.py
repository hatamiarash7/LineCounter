class Counter(object):
    def __init__(self, file_list):
        self.file_list = file_list
        self.c = 0

    def count(self):
        for file in self.file_list:
            self.c += sum(1 for line in open(file))
        return self.c