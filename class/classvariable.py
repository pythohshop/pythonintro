class DemoClassVariable:
    class_variable = 0

    def __init__(self):
        DemoClassVariable.class_variable += 1

    def get_class_variable(self):
        return self.class_variable

dcv1 = DemoClassVariable()
print(dcv1.class_variable)

dcv2 = DemoClassVariable()

print(dcv2.class_variable)
