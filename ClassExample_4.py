#Python Class made by Jere Sumell (jjsume@github.com)

class Employee:
	empCount = 0;
	
	def __init__(self, name, salary):
		self.name = name;
		self.salary = salary
		Employee.empCount+=1
	
	def totalEmps(self):
		print ("Total of Employees: " +str(Employee.empCount) +"!")
	
	def displayEmployee(self):
		print ("Name: " +str(self.name) +" - Salary: " +str(self.salary))

#Next we hire some Python enthusiastics...
firstEmp = Employee("Jere Sumell", 2500)
secondEmp = Employee("John Doe", 2500)
firstEmp.displayEmployee()
secondEmp.displayEmployee()
print ("" +str(Employee.empCount))