#! usr/bin/env python3
bignum=int(input("Give me a big num"))
smallnum=int(input("Give me a small num"))
stepper=int(input("Give me a num to step by"))
print(smallnum)
while smallnum < bignum:
    print(smallnum + stepper)
    smallnum+=stepper
