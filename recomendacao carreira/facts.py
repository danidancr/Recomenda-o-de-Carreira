class Facts:
    def __init__(self):
        self.facts = set()

    def add_fact(self, fact):
        self.facts.add(fact)

    def has_fact(self, fact):
        return fact in self.facts
