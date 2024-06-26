#import typing
# - Must recieve 3 parameters: (operatinon, number , number)
# - validate the parameters and make sure they all are valid, in the case of not valid raise a exception 
# - Must return the result of the operation when the parameters are valide

def calculator(operation: str,number_1 : int|float,number_2 : int|float):
    
    validade_calculator(operation=operation,number_1=number_1,number_2=number_2)

    if operation == 'add':
        return number_1 + number_2
    elif operation == 'sub':
        return number_1 - number_2
    elif operation == 'div':
        try:
            return number_1/number_2
        except ZeroDivisionError:
            raise ZeroDivisionError('You can\'t divide by zero.')
    elif operation == 'multiply':
        return number_1 * number_2
    
def validade_calculator(operation:str, number_1: int|float, number_2: int|float) -> None:
    #validating the operation througt testing
    if operation is None:
        raise Exception("Operation can't be None.")
    if number_1 is None or number_2 is None:
        raise Exception('Need to inform 2 valid numbers.')
    if operation not in ['add','sub','div','multiply']:
        raise Exception('The operations can be add,sub,div or multiply.')
