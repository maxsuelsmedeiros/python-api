#import typing
# - Must recieve 3 parameters: (operatinon, number , number)
# - validate the parameters and make sure they all are valid, in the case of not valid raise a exception 
# - Must return the result of the operation when the parameters are valide

def calculator(operation: str,number_1 : int|float,number_2 : int|float):
    if operation is None:
        raise Exception("Operation can't be None.")