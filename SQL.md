# Write a query to get the first  and last record from a table 
select * from Student where RowID = select max(RowID) from Student;   
select * from Student where RowID = select min(RowID) from Student;  -- or  select * from Student where Rownum = 1;    
#--------------------------------------------------------------------------------------------------------------------------------  

# dislay first 10 records
select * from Student where Rownum <= 10;  -- or  select top 10 *  from Student;  
#--------------------------------------------------------------------------------------------------------------------------------  

# create table like copy
Create table Student2 as Select * from Student;  
#--------------------------------------------------------------------------------------------------------------------------------  

## hirarchy code
WITH Employee_CTE(employeeid,hierarchy_level,name) AS    
(  
   SELECT employeeid,1 as level,name from employee  where employeeid=1   
   UNION ALL    
   SELECT e.employeeid,level +1, e.name   
   from employee e     
   INNER JOIN Employee_CTE c ON e.employeeid = c.managerid   
)   
SELECT * FROM Employee_CTE order by employeeid    


##https://www.w3schools.com/sql/
