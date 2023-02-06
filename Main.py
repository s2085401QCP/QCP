from Register import Register
from Qubit import Qubit
import Operators as op
import Tests



r1 = Tests.threeSevenTest()
Tests.normalizedTest(r1)
r1.updateS()

#op.printMat(r1.coefs)
print("REGISTER STATE: VECTOR AS VERTICAL MATRIX")
op.printMat(r1.stateS)

r2 = Tests.hadamardTest()
Tests.normalizedTest(r2)

Tests.hadAdvanced()

r2.updateE()
