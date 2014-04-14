# Written by Alexander Starr

from mrjob.job import MRJob
from mrjob.step import MRStep

QUERY = "AACCCTAACCCT"

class mrBLAST(MRJob):
    def mapper_get_lines(self, _, line):
        if QUERY in line:
            yield (QUERY, line)

    def reducer_show_occurrences(self, key, values):
        yield (key, str(list(values)))

    def steps(self):
        return [MRStep(mapper=self.mapper_get_lines,
                reducer=self.reducer_show_occurrences)]

if __name__ == '__main__':
    mrBLAST.run()