class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for path in paths:
            values = path.split(" ")
            for i in range(1, len(values)):
                name_cont = values[i].split("(", maxsplit=1)  # stops when '(' char is first encountered.
                name_cont[1] = name_cont[1].replace(")", "")
                ## For key= content Add folder structure as values
                map[name_cont[1]].append(values[0] + "/" + name_cont[0])

        res = []

        for k, v in map.items():
            if len(v) > 1:
                res.append(v)

        return res