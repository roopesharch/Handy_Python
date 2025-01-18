### MongoDB syntax and rules

# insert one
db.collection.insertOne( { item: "card", qty: 15 } );  
**Returns:**  
{
   "acknowledged" : true,
   "insertedId" : ObjectId("56fc40f9d735c28df206d078")
}

# insert Many
   db.products.insertMany( [  
      { item: "card", qty: 15 },  
      { item: "envelope", qty: 20 },  
      { item: "stamps" , qty: 30 }  
   ] );
**Return** 
{
   "acknowledged" : true,
   "insertedIds" : [
      ObjectId("562a94d381cb9f1cd6eb0e1a"),
      ObjectId("562a94d381cb9f1cd6eb0e1b"),
      ObjectId("562a94d381cb9f1cd6eb0e1c")
   ]
}
   

