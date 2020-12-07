# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db 


# cred = credentials.Certificate("./pc-components-8db97-firebase-adminsdk-d039v-769f8f6a52.json")

# firebase_admin.initialize_app(cred,
# {
#     "databaseURL" : "https://pc-components-8db97-default-rtdb.europe-west1.firebasedatabase.app"
#     # 'databaseAuthVariableOverride': {
#     #     'uid': 'my-service-worker'
#     # }
# }
# )

# ref = db.reference("restricted_access/secret_document")

# print(ref.get())


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./pc-components.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://pc-components-77a24-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('testing')

# posts_ref = ref.child('testing')

for i in range(5):


    ref.push(
        {
        'title': 'seconitem'+ str(i),
        'price': 'R120',
        "date": 1234567,
        "image_url":"www.google.com"
    },
      {
        'title': 'seconitem'+ str(i),
        'price': 'R120',
        "date": 1234567,
        "image_url":"www.google.com"
    }
    
    
    
    )

data = ref.get()
print(data)