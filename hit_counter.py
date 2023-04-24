class HitCounter:
    hits = []

    def record(self, timestamp):
        """
        records a hit that happened at timestamp
        """
        self.hits.append(timestamp)

    def total(self):
        """
        returns the total number of hits recorded
        """
        return len(self.hits)

    def range(self, lower, upper):
        """
        returns the number of hits that occurred between timestamps lower and upper (inclusive)
        """
        return len([hit for hit in self.hits if hit >= lower and hit <= upper])

hc = HitCounter()
hc.record(2)
hc.record(7)
hc.record(5)

print(hc.range(0, 6))
