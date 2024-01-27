# Get the database using the method we defined in pymongo_test_insert file
from connect_db_test import get_database

# dbname = get_database()
# print(dbname)
# Create a new collection
# collection_name = dbname["books_by_category"]
dbname = get_database()
# collection_name = dbname["user_1_items"]
item_1 = {
  "_id" : "U1IT00003",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}
collection_name1 = dbname["books_by_category"]
# collection_name1.insert_one(item_1)
item_details = collection_name1.find()
for item in item_details:
    # This does not give a very readable output
    print(item)
