from OOPSdemo import Calculator
#if you have a constructor defined in the parent
# class and the child class is inheriting that class, then child constructor needs
# to call the parent class constructor


class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2, 10)

    def getCom(self):
        return self.num
