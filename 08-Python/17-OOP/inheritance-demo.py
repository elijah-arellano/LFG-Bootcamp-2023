
class Employee:
    
    # attribute shared by all the instances of the class
    instance_count = 0
    
    # a static method - accessible using the the 'class' reference itself
    # any logic related to the Employee type but NOT specific to any instance of Employee
    @staticmethod
    def get_type():
        return type(Employee)
    
    """ 
        from_dict() method usage
        emp_dict = { "id" : 100, "firstName" : "Magesh", "lastName" : "Kuppan" }
        e = Employee.from_dict(emp_dict)
    """
    @staticmethod
    def from_dict(data_dict):
        return Employee(data_dict["id"], data_dict["firstName"], data_dict["lastName"])
    
    # constructor method that gets invoked whenever a new instance of Employee is created
    
    #first_name & last_name are hardcoded
    """ 
    def __init__(self): # self => reference of the newly created object
        print("A new employee instance is being created")
        self.first_name = "Magesh"
        self.last_name = "Kuppan" 
    """
    
    #first_name & last_name can be passed by the user, but required.
    """ 
    def __init__(self, fName, lName): # self => reference of the newly created object
        print("A new employee instance is being created")
        self.first_name = fName
        self.last_name = lName 
    """ 
    
    #first_name & last_name can be passed by the user, and optional.
    # __init__ is invoked whenever a new instance of this class is created
    def __init__(self, id, fName="", lName=""): # self => reference of the newly created object
        
        #track the number of instances created
        Employee.instance_count += 1
        
        # prefixing the attribute with "_" is a CONVENTION to denote that it is a private attribute
        self._id = id 
        self.firstName = fName
        self._last_name = lName 
        self.days_worked = 0
    
    # __str__ is invoked when the object is converted to a string 
    # use str() function
    def __str__(self):
        return f"id={self.id}, firstName={self.firstName}, lastName={self.lastName}"

    # __repr__ is invoked to get the object string to be displayed
    # "f{obj!r}"
    # use the repr()
    def __repr__(self):
        return f"Employee({self.id}, '{self.firstName}', '{self.lastName}')"
    
    def mark_attendance(self):
        self.days_worked += 1
    
    # @property makes the 'id' member accessible as an attribute (ex: e.id) and NOT as a method
    @property
    def id(self):
        print("id getter invoked")
        return self._id
    # by not creating a setter for 'id', we are making the 'id' readonly

    # getter & setter for "firstName"
    @property
    def firstName(self):
        return self._first_name
    
    @firstName.setter
    def firstName(self, value):
        if value == "":
            raise Exception()
        self._first_name = value
    
    # getter & setter for "lastName"
    @property
    def lastName(self):
        return self._last_name
    
    @lastName.setter
    def lastName(self, value):
        if value == "":
            raise Exception()
        self._last_name = value

# FullTimeEmployee inherits Employee
class FullTimeEmployee(Employee):
    def __init__(self, id, fName="", lName="", benefits=""):
        super().__init__(id, fName, lName)
        self.benefits = benefits

    def __repr__(self):
        return f"FullTimeEmployee({self.id}, '{self.firstName}', '{self.lastName}','{self.benefits}')"
    
    def __str__(self):
        return f"{super().__str__()}, benefits={self.benefits}"
    
    