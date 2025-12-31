from src.calc import add,mul,sub

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# sum =a + b
# sum=add(a,b)
# multi=mul(a,b)
def test_add():
    assert add(1000, 2) == 1002
def test_mul():
    assert mul(1000, 2) == 2000
def test_sub():
    assert sub(1000, 200) == 800



# print("The sum is:", sum)
# print("The mul is:", multi)

