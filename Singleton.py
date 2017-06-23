__author__ = 'Xiang-Yi'

#key-value pair example with **kwargs

def greet_me(**kwargs):
    if kwargs is not None:
        for key in kwargs:
            print ("%s == %s" %(key, kwargs[key]))

greet_me(name="yasoob", age="18",year="2017")

#iterations --> which item to call first is uncertain, defined by the language








class DatabaseConfiguration():
    _sharedData = {}
    def __init__(self, **kwargs):
        self._sharedData.update(kwargs)             # update _sharedData dictionary with key-value pair(s) provided
    def __str__(self):
        return str(self._sharedData)                # return the _sharedData dictionary when object is printed

# Let's add a configuration detail in the form of a key-value pair to the sharedData dictionary
configDetailsOne = DatabaseConfiguration(database = "10.10.10.10")
# Printing the sharedData dictionary
print(configDetailsOne)                             # OUTPUT: {'database': '10.10.10.10'}

# Let's add a few more other configuration details to the sharedData dictionary
configDetailsTwo = DatabaseConfiguration(user = "userOne")
configDetailsThree = DatabaseConfiguration(password="userOne")
configDetailsFour = DatabaseConfiguration(serviceName="serviceOne")

# Let's take a look at what the sharedData dictionary now looks like.
print(configDetailsFour)                            # OUTPUT: {'password': 'userOne', 'database': '10.10.10.10', 'user': 'userOne', 'serviceName': 'serviceOne'}

#note that it's printing config4, but all are printed, which shows that they all call the same dictionary (global dictionary, hence global key-value entries)
