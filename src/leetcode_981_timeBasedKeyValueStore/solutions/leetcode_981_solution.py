class TimeMap:
    def __init__(self):
        self.kvstore = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvstore:
            self.kvstore[key] = []
        self.kvstore[key].append((timestamp, value))
            
    def get(self, key:str, timestamp: int) -> str:
        if key not in self.kvstore:
            return ""

        values = self.kvstore[key]

        # When target timestamp is outside of the range.
        if values[0][0] > timestamp: return ""
        if values[-1][0] <= timestamp: return values[-1][1]

        idx = self._idx_search(values, timestamp)
        return values[idx][1]

    # Binary search, return index that matches the target timestamp
    # or the version right before target timestamp.
    def _idx_search(self, values, target):
        idx, left, right = 0, 0, len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2
        
            if values[mid][0] < target:
                left = mid + 1
                idx = mid
            elif values[mid][0] > target:
                right = mid - 1
            else:
                return mid

        return idx