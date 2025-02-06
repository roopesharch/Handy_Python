# python Dictionary methods

Invalid dictionary  
Error: using a list as a key is not allowed hence use tuple  
dictionary cannot have duplicate keys   
  
my_dict = {  
  1: "Hello",   
  (1, 2): "Hello Hi",   
}  
print(my_dict)  
a= my_dict.items()  
print(a)  

# print(my_dict)
v=[]
k=[]
for i,j in zip(my_dict.values(),my_dict.keys()):
    v.append(i)
    k.append(j)
    
print(v,k)
  
  
country_capitals = {  
  "United States": "New York",   
  "Italy": "Naples",   
  "England": "London"  
}  
 
 
 
print(country_capitals)  
print("=====================================")  
# change the value of "Italy" key to "Rome"  
country_capitals["Italy"] = "Rome"  
  
print(country_capitals)  



country_capitals = {  
  "United States": "New York",   
  "Italy": "Naples"   
}  
print("=====================================")  
# add an item with "Germany" as key and "Berlin" as its value  
country_capitals["Germany"] = "Berlin"  
  
print(country_capitals)  
  

print("=====================================")  
# delete item having "United States" key or also pop or popitem()  remove last element  

country_capitals = {  
  "United States": "New York",   
  "Italy": "Naples" ,  
  "mars":"planet",  
  "earth":"ours"  
}  
print(country_capitals)  
  
print(country_capitals.pop('Italy'))  
del country_capitals["United States"]  
print(country_capitals.popitem())  
print(country_capitals)  
  
print("=====================================")  
# to copy and clear dict   
a=country_capitals.copy()  
print(a,country_capitals)  
a.clear()  
print(a,country_capitals)  
  
print("=====================================")  
# update dictionary value  
    
print(country_capitals)  
country_capitals['mars']='solar'  
print(country_capitals)  
  
  
#sort dictionary by val and key  
a = sorted(dict_name.items(), key=lambda x:x[0]) # by Key  
a = sorted(dict_name.items(), key=lambda x:x[1]) # by Value  





