import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



# initializations 
cred = credentials.Certificate('sportsden-admin-firebase-adminsdk-qvcpx-eaab4bee80.json')
firebase_admin.initialize_app(cred)
db = firestore.client()






#Reading the data

emp_ref = db.collection('users')
docs = emp_ref.stream()

for doc in docs:
    if "friends" in doc.to_dict():

        print('{} => {} '.format(doc.id, doc.to_dict()))
    else:
        print('{} => {} '.format(doc.id, doc.to_dict()))
        emp_ref.document(doc.id).set({
            "friends": []
        }, merge=True)
    if "followers" in doc.to_dict():

        print('{} => {} '.format(doc.id, doc.to_dict()))
    else:
        print('{} => {} '.format(doc.id, doc.to_dict()))
        emp_ref.document(doc.id).set({
            "followers": []
        }, merge=True)
