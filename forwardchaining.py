class Rule:
    def __init__(self, premises, conclusion):
        self.premises = premises
        self.conclusion = conclusion

    def evaluate(self, facts):
        for premise in self.premises:
            if premise not in facts:
                return False
        return True

    def fire(self, facts):
        facts.add(self.conclusion)


class ForwardChaining:
    def __init__(self, rules):
        self.rules = rules
        self.facts = set()

    def run(self):
        while True:
            fired = False
            for rule in self.rules:
                if rule.evaluate(self.facts) and rule.conclusion not in self.facts:
                    rule.fire(self.facts)
                    fired = True
            if not fired:
                break


def main():
    rules = [
        Rule(["mammal(A)"], "vertebrate(A)"),
        Rule(["vertebrate(A)"], "animal(A)"),
        Rule(["vertebrate(A)", "flying(A)"], "bird(A)")
    ]

    fc = ForwardChaining(rules)
    fc.facts.add("mammal(duck)")
    fc.run()
    print(fc.facts)


if __name__ == "__main__":
    main()
