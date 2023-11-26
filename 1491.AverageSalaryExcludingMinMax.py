from typing import List
def average(salary: List[int]) -> float:
    salary = sorted(salary)
    average = 0
    count = 0
    for i in range(1, len(salary)-1):
        average += salary[i]
        count += 1
    return average/count
def averageOptimum(salary: List[int]) -> float:
    minSalary = float('inf')
    maxSalary = float('-inf')
    average = 0
    for sal in salary:
        average += sal
        minSalary = min(minSalary, sal)
        maxSalary = max(maxSalary, sal)
    return (average-minSalary-maxSalary) / (len(salary) - 2)

salary = [4000,3000,1000,2000]
salary1 = [1000,2000,3000]
print(average(salary))
print(average(salary1))
print(averageOptimum(salary))
print(averageOptimum(salary1))