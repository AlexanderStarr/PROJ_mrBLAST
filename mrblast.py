# Written by Alexander Starr

from mrjob.job import MRJob
from mrjob.step import MRStep

class mrBLAST(MRJob):

    def mapper_init(self):
        # Provide the query, located in a file, to the mapper.
        qfile = open('query.txt', 'r')
        self.query = ''.join(qfile.read().split())
        qfile.close()

    def mapper_get_lines(self, _, line):
        if self.query in line:
            yield (self.query, line)

    def reducer_show_occurrences(self, key, values):
        yield (key, str(list(values)))

    def steps(self):
        return [MRStep(mapper_init=self.mapper_init,
                       mapper=self.mapper_get_lines,
                       reducer=self.reducer_show_occurrences)]

if __name__ == '__main__':
    mrBLAST.run()