import tests.circuit_test
import tests.input_test

def main():
    tests.circuit_test.twoBitEntanglement()
    tests.circuit_test.testHadamardApplications()
    tests.circuit_test.testPauliXApplication()
    tests.input_test.registerTest()
    tests.input_test.dJTest()
    tests.input_test.groversTest()

if __name__ == "__main__":
    main()  