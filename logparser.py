import re
from enum import Enum

class LogIngester:
    lines: list()
    SortSet = Enum('SortSet', ['file_name', 'request_count', 'total_bytes'])

    def __init__(self, filename):
        line_hashes = dict()

        with open(filename, 'r') as f:
            for line in f.readlines():
                re_string = "^\[(.*)] \"GET (.*) HTTP.*\" (2\d{2}) (\d+)"
                re_compile = re.compile(re_string)
                re_matches = re.match(re_compile, line)
                if re_matches is None:
                    continue

            raw_line = re_matches[0]
            datetime = re_matches[1]
            request = re_matches[2]
            status = int(re_matches[3])
            size = int(re_matches[4])

            existing_file = line_hashes.get(request, dict())

            if existing_file.get('total_count', None) is not None:
                line_hashes.update({request: dict(
                    total_count=existing_file['total_count'] +1,
                    total_bytes=existing_file['total_bytes'] + size
                )})
            else:
                line_hashes.update({request: dict(total_count=1, total_bytes=size)})
            
        for filename, v in line_hashes.items():
            self.lines.append(tuple([filename, v.get('total_count'), v.get('total_bytes')]))

    def sort_lines(self, pivot1, pivot2=(None, 1), pivot3=(None, 1)):
        ordered_tuples = []

        for line in self.lines:
            ordering_middleware = []

            match pivot1[0]:
                case self.SortSet.file_name:
                    ordering_middleware.append(line[0])
                case self.SortSet.request_count:
                    ordering_middleware.append(line[1])
                case self.SortSet.total_bytes:
                    ordering_middleware.append(line[2])
                
            match pivot2[0]:
                case self.SortSet.file_name:
                    ordering_middleware.append(line[0])
                case self.SortSet.request_count:
                    ordering_middleware.append(line[1])
                case self.SortSet.total_bytes:
                    ordering_middleware.append(line[2])
                case other:
                    ordering_middleware.append(None)    

            match pivot3[0]:
                case self.SortSet.file_name:
                    ordering_middleware.append(line[0])
                case self.SortSet.request_count:
                    ordering_middleware.append(line[1])
                case self.SortSet.total_bytes:
                    ordering_middleware.append(line[2])
                case other:
                    ordering_middleware.append(None)    
            
            ordered_tuples.append(tuple(ordering_middleware))

        ordered_tuples.sort(key=lambda x: (x[0] * pivot1[1], x[1] * pivot2[1], x[2] * pivot3[1]))
        self.lines = ordered_tuples
    
    def render(self, fmtstr="{col[0]} {col[1]} {col[2]}", limit=None):
        if limit is not None:
            res = self.lines[:limit]
        for tup in res:
            print(fmtstr.format(col=tup))
    
ing = LogIngester('server.log')

ing.sort_lines(
    pivot1=(ing.SortSet.request_count, -1),
    pivot2=(ing.SortSet.file_name, 1),
    pivot3=(ing.SortSet.total_bytes, -1),
)

ing.render(fmtstr="{col[1]} {col[2]}", limit=10)
