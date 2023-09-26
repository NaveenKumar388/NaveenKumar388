



class datatype:
 def list(self):
   # Create an empty list
   my_list = []
   # Use the dir() function to list    available methods and attributes
   list_operations = [attr for attr in dir(my_list) if not attr.startswith("__")]
   # Print the list of available list operations
   print("List of available list operations in Python:")
   count=0
   for operation in list_operations:
      count+=1
      print(count,operation)
   print('total list  operations is',count,'.')

 def tuple(self):
   # Create an empty tuple
   my_tuple = ()
   # Use the dir() function to list available methods and attributes
   tuple_op = (attr for attr in dir(my_tuple) if not attr.startswith("__"))
   # Print the list of available tuple operations
   print("List of available tuple operations in Python:")
   count=0
   for operation in tuple_op:
      count+=1
      print(count,operation)
   print('total tuple operations is',count,'.')

 def set(self):
   # Create an empty set
   my_set = set()
   # Use the dir() function to set available methods and attributes
   set_op = {attr for attr in dir(my_set) if not attr.startswith("__")}
   # Print the list of available set operations
   print("List of available set operations in Python:")
   count=0
   for operation in set_op:
      count+=1
      print(count,operation)
   print('total set operations is',count,'.')


 def dictionary(self):
   # Create an empty dictionary
   my_dict = {}

   # Use dir() to set all attributes and methods of the dictionary
   dict_op={attr for attr in dir(my_dict) if not attr.startswith("__")}
   #print the list of available dictionary functions
   print("List of available dictionary operations in python:")
   count=0
   for operation in dict_op:
       count+=1
       print (count,operation)
   print ("total dictionary operations is ",count)


x=datatype()
x.list()
x.tuple()
x.dictionary()
x.set()











