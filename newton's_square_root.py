# Suppose that you want to know the square root of n. If you start with almost any approximation, you can compute
# a better approximation (closer to the actual answer) with the following formula:
#  better = (approx + n/approx)/2


# This is an example of an indefinite iteration problem: we cannot predict in advance how many times we’ll want to
# improve our guess — we just want to keep getting closer and closer. Our stopping condition for the loop will be
# when our old guess and our improved guess are “close enough” to each other.


def newton_sqrt(n, accuracy):
    approx = n/2.0

    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < accuracy:
            return better
        approx = better


n = int(input("Enter the no to calculate its square root: "))
accuracy = float(input("Enter the accuracy you want (e.g. 0.001): "))
print(newton_sqrt(n, accuracy))
