from pymongo import MongoClient
client = MongoClient('localhost',27017)
mydb=client["testdb"]
mycol=mydb["testcollection"]
# mydist=[{"_id":3,"name":"Tiger","Age":30,"Occupation":"Product"},
#         {"_id":2,"name":"Jack","Age":20}]
# x = mycol.insert_many(mydist)

#x=mycol.find_one({"name":"Tiger"})

mycol.update_many({"name":"Tiger"},{"$set":{"name":["John","Mario"]}})

for i in mycol.find():
    print(i)

###test1111