import smartpy as sp
@sp.module
def main():
    class MyClass(sp.Contract):
        def __init__(self, startingValue):
            sp.cast(startingValue, sp.set[sp.nat])
            self.data.validNumbers = startingValue

        @sp.entrypoint
        def addId(self, newId):
            sp.cast(newId, sp.nat)
            self.data.validNumbers.add(newId)

        @sp.onchain_view
        def checkId(self, testId):
            sp.cast(testId,sp.nat)
            isReal = self.data.validNumbers.contains(testId)
            if isReal:
                return True
            else:
                return False

@sp.add_test()
def test():
    scenario = sp.test_scenario("Authenticity Test", main)
    scenario.h1("Authenticity Test")
    c = main.MyClass(sp.set([sp.nat(1),(2),(3)]))
    scenario += c

    c.addId(sp.nat(4))










