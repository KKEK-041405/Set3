DESCRIPTIO

N

:

Given an integer basic and a character grade which denotes the basic salary and grade of a person

respectively, the task is to find the gross 

salary of the person.

Gross Salary: The final salary computed after the additions of DA, HRA and other allowances. 

The idea is to find the allowance on the basis of the grade and then compute the HRA, DA, and PF

on the basis of the basic salary. Below is 

the illustration of the computation of HRA, DA, and PF

.

PROGRAM:

def computeSalary( basic, grade):

 

 hra 

= 0.2

* basic

 da 

= 0.5

* basic

 pf 

= 0.11

* basic

 

 # Condition to compute the

 # allowance for the person

 if grade 

=

=

'A'

:

 allowance 

= 1700.0

 elif grade == 'B'

:

 allowance 

= 1500.0

 else

:

 allowance 

= 1300.0

;

 

 

gross 

= round(basic 

+ hra 

+ da 

+allowance 

- pf)

 

 return gross

# Driver code

if __name__ == '__main__'

:

 

 basic 

= 10000

 grade 

= 'A'

 

 # Function call

 print(computeSalary(basic, grade));

OUTPUT:

17600 
