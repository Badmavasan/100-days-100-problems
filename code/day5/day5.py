class Day5:

    def get_items_at(self, arr, par):
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return [arr[-1]] if par == 'odd' else []
        return self.get_items_at(arr[:-2], par) + [arr[-1] if par == 'odd' else arr[-2]]

