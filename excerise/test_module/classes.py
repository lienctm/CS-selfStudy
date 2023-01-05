# There are 2 ways to import a module
# each function in the module is available through the following syntax :

# "import" statement
import students
students.full_name('Emily', 'Hank')
students.full_name('Ken', 'Nguyen')

print("---------------------")
# from module_name import function_name
from students import full_name
full_name('Steven', 'Tran')
full_name('Daniel', 'Job')