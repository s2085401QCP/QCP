from Register import Register
from Qubit import Qubit
import Operators as op
import Tests

# this main runs through a few of the materials covered in the notes
# the three seven tests is covered in the slides
print("REGISTER STATE: VECTOR AS VERTICAL MATRIX")
r1 = Tests.threeSevenTest()
Tests.normalizedTest(r1)
r1.updateS()

# these tests are to ensure the hadamard is taking form that is appropriate 
# it seems to be working as intended

# the register must always be normalised, 
# a register involving multiple states of fractions is in a superposition
r2 = Tests.hadamardTest()
Tests.normalizedTest(r2)
Tests.stateTest()
Tests.hadAdvanced()


r2.updateE()

Tests.CNOTtest()
