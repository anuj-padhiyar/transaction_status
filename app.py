from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask, jsonify, request, send_file
import datetime
import requests
import pandas as pd
from dateutil.parser import parse
from bson import ObjectId

app = Flask(__name__)

# connect DB
uri = "mongodb+srv://user1:user123456@cluster1.z3wg4dp.mongodb.net/"
MONGO_CLIENT = MongoClient(uri)
transaction_db = MONGO_CLIENT['zvya']['transaction_details']


# DB functions
def insert(document):
    data = find_one_by_query(query={'Card ID':document['Card ID']})
    if data is not None:
        update(id = str(data['_id']),document=document)
    else:
        document['created_at'] = datetime.datetime.utcnow()
        document['updated_at'] = datetime.datetime.utcnow()
        return transaction_db.insert_one(document=document)

def update(id, document, unset_doc={}):
    document['updated_at'] = datetime.datetime.utcnow()
    transaction_db.find_one_and_update(filter={'_id': ObjectId(id)},update={'$set': document, '$unset': unset_doc})

def find_one_by_query(query):
    return transaction_db.find_one(filter=query)



# helper functions
def get_status(val):
    if val == 'pickup':
        return 'Pickup'
    if val == 'delivery_exceptions':
        return 'Delivery Exceptions'
    if val == 'delivered':
        return 'Delivered'
    if val == 'returned':
        return 'Returned'
    return None

def read_and_add_data():
    for file in ['pickup','delivery_exceptions','delivered','returned']:
        try:
            df = pd.read_csv('./data/%s.csv' % file)
            for index, row in df.iterrows():
                try:
                    row_json = row.to_dict()
                    row_json['status'] = get_status(file)
                    row_json['Timestamp'] = parse(row_json['Timestamp']) if 'Timestamp' in row_json else None
                    insert(row_json)
                except Exception as ex:
                    print(ex)
        except Exception as ex:
            print(ex)


def read_details_from_db(card_id):
    transaction = find_one_by_query(query={'Card ID':card_id})
    if transaction is not None:
        return {
            'Card ID':transaction['Card ID'],
            'Comment':transaction['Comment'] if 'Comment' in transaction else None,
            'Status':transaction['status'] if 'status' in transaction else None,
            'User Mobile':transaction['User Mobile'] if 'User Mobile' in transaction else None,
            'Timestamp':transaction['Timestamp'] if 'Timestamp' in transaction else None
        }
    return {'error':'No Card Data Available'}

    

# APIs
@app.route('/')
def home():
    return "<h2>Below is the two API details</h1><br><h3>/update_details</h3> => For Update Databse with csv files.<br><br><h3>/get_card_details/[card_id]</h3> => For Get status using Card ID."

@app.route('/update_details')
def update_details():
    read_and_add_data()
    return {'status':'Database Updated with csv files.'}

@app.route('/get_card_details/<card_id>', methods=['GET'])
def email_opened(card_id):
    status = read_details_from_db(card_id)
    return jsonify(status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)