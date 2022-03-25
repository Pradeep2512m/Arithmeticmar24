import unittest
def checkevenoroddno(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
def check_divisible_by7(x):
    if x%7==0:
        return True
    else:
        return False
def PrimeorNot(x):
    if x>1:
        for i in range(2,int(x/2)+1):
            if(x%i)==0:
                break
            else:
                return True
        else:
            return False

class Mycheck(unittest.TestCase):
    def test_even_or_odd(self):
        result = checkevenoroddno(2)
        self.assertEqual("even",result)
    def test_even_or_odd1(self):
        result=checkevenoroddno(9)
        self.assertEqual("odd",result)
    def test_divisibleby7(self):
        result=check_divisible_by7(3)
        self.assertFalse(result)
    def test_divisibleby7_2(self):
        result=check_divisible_by7(28)
        self.assertTrue(result)
    def test_primeornot(self):
        result=PrimeorNot(2)
        self.assertTrue(result)
    def test_primeornot2(self):
        result=PrimeorNot(1)
        self.assertFalse(result)
if __name__=="__main__":
    unittest.main()