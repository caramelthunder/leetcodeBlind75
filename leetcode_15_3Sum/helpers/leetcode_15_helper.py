class Helper:
    def compare_lists(self, lst1: list[list[int]], lst2: list[list[int]]) -> bool:
        if len(lst1) != len(lst2):
            return False
        
        set1 = sorted([sorted(triplet) for triplet in lst1])
        set2 = sorted([sorted(triplet) for triplet in lst2])

        return set1 == set2