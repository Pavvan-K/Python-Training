import <module_name>
 this does not make the module contents 
 
 From the caller, objects in the module are only accessible when prefixed with <module_name> via dot notation, as illustrated below
 
 import mod
 
 print(s) (Object inside mod.py) (ERROR)
 print(foo('quuz')) (function inside mod.py) (ERROR)
 
 mod.s (OK)
 mod.foo (OK)
 
 An alternate form of the import statement allows individual objects from the module to be imported directly into the caller’s 
 
 from <module_name> import
 
 from mod import s, foo
 print(s)(OK)
 print(foo('quux'))(OK)
 
 
 from mod import *
 print(s)(OK)
 print(a)(OK)
 print(foo('quux'))(OK)
 
from <module_name> import <name> as <alt_name>


If your script already contain same object names which as in module then we can use alternative names while importing 
objects into python


s = 'foo'
a = ['foo', 'bar', 'baz']

from mod import s as string, a as alist

print(string)
print(a)
print(s)
print(alist)


#You can also import an entire module under an alternate name:
import <module_name> as <alt_name>
import mod as my_module
my_module.a
my_module.foo('qux')


#Module contents can be imported from within a function definition. In that case, the import does not occur until the function is called:

def bar():
	from mod import foo
	foo('corge')
	
bar()


dir()
-----
The built-in function dir() returns a list of defined names in a namespace
It produces an alphabetically sorted list of names in the current local symbol table:
This can be useful for identifying what exactly has been added to the namespace by an import statement:



When given an argument that is the name of a module, dir() lists the names defined in the module
 import mod
 dir(mod) #lists the names defined in the mod module
 
 Executing a Module as a Script
 -------------------------------
What if we want to execute our module as a python script

 