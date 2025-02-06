
# class Evaluation:
#     def __init__(self):
#         """
#         Gets metadata for a particular function. 
#         """
#         self.metadata = {}

#     def eval(func):
#         def wrap(*args, **kwargs):
#             self._populate_metadata(func, (args, kwargs))
#             return self._process_function()
#         return wrap
        
#     def _populate_metadata(self, func, params):
#         args, kwargs = params

#         self.metadata['name'] = func.__name__
#         self.metadata['doctstring'] = func.__doc__
#         self.metadata['args'] = args
#         self.metadata['kwargs'] = kwargs

#         return self.metadata

#     def _process_function():
#         string_builder = ''    
#         star = '*' * 75

#         string_builder += star

#         # add name of function
#         string_builder += f'\nEvaulation for {self.metadata}'
        

#         return string_builder
    
class Helper:
    def __init__(self):
        pass

    def _is_prime(x:int) -> int:
        """
        Helper function to determine if a number is prime
        """
        for i in range(2, (x//2) + 1):
            if x % i != 0:
                return x
            
    def _is_prime_bool(x:int) -> bool:
        """
        Helper function to determine if a number is prime
        """
        for i in range(2, (x//2) + 1):
            if x % i != 0:
                return True
        return False