import numpy as np
jeff_salary=[2700, 3000, 3000]
nick_salary=[2600, 2800, 2800]
tom_salary=[2300, 2500, 2500]
base_salary=np.array([jeff_salary,nick_salary,tom_salary])
jeff_bonus=[400,400,500]
nick_bonus=[600,300,400]
tom_bonus=[200,500,400]
bonus_salary=np.array([jeff_bonus,nick_bonus,tom_bonus])
salary_bonus=base_salary+bonus_salary
print(salary_bonus)
axis1=np.max(salary_bonus,axis=1)
axis0=np.max(salary_bonus,axis=0)
print(f'Max axis0 = {axis0}')
#axis 0 is the vertical or column
print(f'Max axis1 = {axis1}')
#axis 1 is the horizontal or row
np_amax=np.amax(salary_bonus)
np_median=np.median(salary_bonus)
np_average=np.average(axis0)
print(f'aMax axis0 = {np_amax}')
print(f'Median axis0 = {np_median}')
print(f'average axis0 = {np_average}')