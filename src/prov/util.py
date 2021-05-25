class MultiBundle:
    def __init__(self):
        self.dict = {}

    def __setitem__(self, key, value):
        try:
            self.dict[key].append(value)
            print('*********',key, value)
        except KeyError:
            self.dict[key] = [value]

    def __getitem__(self, key):
        try:
            return self.dict[key]
        except KeyError:
            return "keyError"
    

    
    def items(self,key):
        return self.__getitem__(key)
    

# Append multiple value to a key in dictionary
def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    #sample_dict[key].extend(list_of_values)
    sample_dict[key].append(list_of_values)
    return sample_dict