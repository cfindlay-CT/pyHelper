import mongoHelper.mongoClient as mongoClient
import systemHelper.osHelper as osHelper
import json
from bson import ObjectId 

if __name__ == "__main__":
    # Example usage
    configJson = osHelper.getEnvValue("LV_SETTINGS")
    configJson = json.loads(configJson)
    mongoConfig = configJson['MONGO']

    # print(f"MongoDB Uri: {mongoConfig['Uri']}")

    db_name = mongoConfig['DB']
    # print(f"Database Name: {db_name}")

    client_helper = mongoClient.MongoClientHelper(mongoConfig['Uri'])
    client_helper.connect(db_name)
    ping_results = client_helper.ping_db()

    if ping_results['ok'] == 1:
        print(f"Successfully connected to the database '{db_name}'.")
        notifications = client_helper.get_collection('notifications')

        for doc in notifications.find():
            # print(doc)

            content = client_helper.get_collection('localizedcontents').find_one({"recordId": ObjectId(doc['_id'])})
            print(f"Notification ID: {doc['_id']}, Content: {content}")
        
        
    client_helper.close()