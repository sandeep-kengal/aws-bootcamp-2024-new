from datetime import datetime, timedelta, timezone

from lib.ddb import Ddb
from lib.db import db
# from lib.momento import MomentoCounter

class MessageGroups:
  def run(cognito_user_id):
    model = {
      'errors': None,
      'data': None
    }

    sql = db.template('users','uuid_from_cognito_user_id') #find the handle from the uuid
    my_user_uuid = db.query_value(sql,{
      'cognito_user_id': cognito_user_id
      }) # query value that returns a single uuid

    print(f"UUID: {my_user_uuid}")

    ddb = Ddb.client() #create a new client
    data = Ddb.list_message_groups(ddb, my_user_uuid) #list out message groups while passing in uuid
    print("list_message_groups: ",data)

    #MomentoCounter.reset(f"msgs/{user_handle}")
    model['data'] = data
    return model