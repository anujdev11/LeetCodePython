# Write your MySQL query statement below

Select a.name as 'Employee' from Employee as a Join Employee as b
                    on a.ManagerId = b.Id
                    And a.Salary > b.Salary; 