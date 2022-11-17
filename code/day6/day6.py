class Day6:
    #
    def bomb(self, lst):
        for a in range(51):
            for b in range(51):
                matches = 0
                for x, y, t in lst:
                    matches += (a - x) ** 2 + (b - y) ** 2 == round((t * 0.343) ** 2)
                if matches == 3:
                    return a, b
