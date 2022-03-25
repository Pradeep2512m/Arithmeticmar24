import unittest
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def addition(x,y,z):
    return x+y+z
class myapp(unittest.TestCase):
    def test_add(self):
        a=2
        b=3
        c=add(a,b)
        self.assertEqual(a+b,c)
    def test_sub(self):
        a = 3
        b = 2
        c = sub(a,b)
        self.assertEqual(a-b,c)
    def test_mul(self):
        a = 3
        b = 2
        c = mul(a,b)
        self.assertEqual(a*b,c)

    def test_div(self):
        a = 10
        b = 5
        c = div(a, b)
        self.assertEqual(a / b, c)

    def test_addition(self):
        a = 10
        b = 5
        c = 8
        d = addition(a, b , c)
        self.assertEqual(a + b + c, d)
if __name__=="__main__":
    unittest.main()
