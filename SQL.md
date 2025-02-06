#Write a query to get the first  and last record from a table 
select * from Student where RowID = select max(RowID) from Student;
select * from Student where RowID = select min(RowID) from Student;  -- or  select * from Student where Rownum = 1;
#--------------------------------------------------------------------------------------------------------------------------------

# dislay first 10 records
select * from Student where Rownum <= 10;  -- or  select top 10 *  from Student;
#--------------------------------------------------------------------------------------------------------------------------------

#create table like copy
Create table Student2 as Select * from Student;
#--------------------------------------------------------------------------------------------------------------------------------

