#!/usr/bin/env python
##lets rock the python programming on cloud
'''
Simple program to perform following operations
Addition of 2 values
Substraction of 2 values
Multiplication of 2 values
'''

import argparse
import logging
import sys
import warnings

warnings.simplefilter("ignore")


class myFirstClass:
    def __init__(self):
        self.msg = 'hello my Class!!'
        print(self.msg)
        logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.warning('This will get logged to a file')

    def addTwoValues(self, a, b):
        logging.info("Sum of two values {} and {} is".format(str(a), str(b)))
        return a + b

    def subTwoValues(self, a, b):
        logging.info("Sub of two values {} and {} is".format(str(a), str(b)))
        return a - b

    def mulTwoValues(self, a, b):
        logging.info("Mul of two values {} and {} is".format(str(a), str(b)))
        return a / b


if __name__ == "__main__":
    myclass = myFirstClass()

    logging.info("Reading provided arguments into!!!")
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--method", type=str, help="Provide any method from following Add/Sub/Multi",
                        required=True)
    parser.add_argument("-v1", "--value1", type=int, help="Provide any method from following Add/Sub/Multi",
                        required=True)
    parser.add_argument("-v2", "--value2", type=int, help="Provide any method from following Add/Sub/Multi",
                        required=True)

    args = parser.parse_args()
    method = args.method
    val1 = args.value1
    val2 = args.value2

    logging.info("Method ={}".format(method))
    logging.info("Val1 ={}".format(val1))
    logging.info("Val2 ={}".format(val2))

    if isinstance(method, str) == False:
        logging.warning("Provided method value should be string!!")
        sys.exit(0)

    if method == 'Add':
        add = myclass.addTwoValues(val1, val2)
        logging.info("Sum of two value {} and {} is {}".format(str(val1), str(val2), str(add)))
    elif method == 'Sub':
        sub = myclass.subTwoValues(val1, val2)
        logging.info("Sub of two value {} and {} is {}".format(str(val1), str(val2), str(sub)))
    elif method == 'Multi':
        mult = myclass.mulTwoValues(val1, val2)
        logging.info("Multi of two value {} and {} is {}".format(str(val1), str(val2), str(mult)))
    else:
        logging.warning("Unknown state!!!")