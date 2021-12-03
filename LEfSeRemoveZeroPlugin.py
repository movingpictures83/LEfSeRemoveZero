import sys

class LEfSeRemoveZeroPlugin:
    def input(self, filename):
        self.resfile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
        outresfile = open(filename, 'w')
        for line in self.resfile:
           contents = line.split('\t')
           if (len(contents[2]) > 0):
               outresfile.write(line)
