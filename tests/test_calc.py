from src.calc import add,mul

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum =a + b
# sum=add(a,b)
# multi=mul(a,b)
def test_add():
    assert add(1000, 2) == 1006
def test_mul():
    assert mul(1000, 2) == 2004



# print("The sum is:", sum)
# print("The mul is:", multi)

