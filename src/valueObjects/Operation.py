from dataclasses import dataclass
from .BasicObject import BasicValueObject
from .BusinessRules import BusinessRulesValidationException
from ..utils.constants import Constants
from math import prod 

#@dataclass(frozen=True)
class Operation(BasicValueObject):
    """Operation value objecto for make valid math operations"""
    
    operator:str
    numbers:list[int]
    result:int
    
    def __init__(self, operator:str, *numbers) -> None:
        """Here we initialize and check if a value object has a valid state."""
        self.operator = self.check_valid_operator(operator)
        self.numbers = [self.convert_string_number_to_integer(number)for number in numbers]
    
    def __post_init__(self) -> None:
        """Here we check if a value object has a valid state for divisions."""
        self.check_division_to_zero()
        
    def check_valid_operator(self, operator:str) -> str:
        """Here we can check if the string is a valid math operator

        Args:
            operator (str): the string operator that we check if a valid math operator

        Raises:
            BusinessRulesValidationException: raise If the string that we pass is not a valid math operator

        Returns:
            str: The operator 
        """
        
        if operator not in Constants.OPERATORS:
            raise BusinessRulesValidationException(Constants.OPERATOR_ERROR_MESSAGE)
        return operator
    
    """Comentarios 
    1. Obviamente si hago el casting de str a int ya me salta un error.
    Como deberia manejar ese error?
    2. Deberia hacer una helper function que valid si es un valid number?
    """
    def convert_string_number_to_integer(self, number:str) -> int:
        """Converts a string number into a integer number (casting)

        Args:
            number (str): the string number that I want to convert into a number

        Raises:
            BusinessRulesValidationException: If its not a invalid string number

        Returns:
            int: the number value in the string arg
        """
        if not(number.isdecimal()):
            raise BusinessRulesValidationException(Constants.NUMBER_ERROR_MESSAGE)
        return int(number)
    
    def check_division_to_zero(self):
        """Here we check if we have a division to zero

        Raises:
            BusinessRulesValidationException: Raise when we have a zero from the second index
        """
        if self.operator == '/' and 0 in self.numbers[1::]:
            raise BusinessRulesValidationException(Constants.ZERO_DIVSION_ERROR_MESSAGE)
        
    def resolve(self) -> int:
        """Here we execute the math operation in the array 

        Returns:
            int: the result of the operation
        """
        
        if self.operator == '+':
            
            self.result = sum(self.numbers)
        elif self.operator == '-':
            
            self.result = self.numbers[0] - sum(self.numbers[1::])
        elif self.operator == '*':
            
            self.result = prod(self.numbers) 
        else:
            
            self.result = self.numbers[0] / prod(self.numbers[1::])
        return self.result
    
    # Usar metodos estaticos?
    @staticmethod
    def create(operator, *numbers):
        """Here we can create the math operation value object

        Args:
            operator (str): operation that we want to perform

        Returns:
            Operation: The operation element that we use to execute the operation
        """
        return Operation(operator, *numbers)
    
    
    
    