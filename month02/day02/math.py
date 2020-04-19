class math:
    def plus(self, a, b):
        print("%d + %d = %d" % (a, b, a + b))

    def sub(self, a, b):
        print("%d-%d=%d" % (a, b, a - b))

    def mul(self, a, b):
        print("%d*%d=%d" % (a, b, a * b))

    def divide(self, a, b):
        print("%d/%d=%d" % (a, b, a / b))


if __name__ == "__main__":
    m = math()
    m.plus(1, 2)
    m.mul(1, 2)
    m.sub(2,3)
