import pyrebase
config={
    'apiKey': "AIzaSyDLzBjNqg37fRiCBClXzamhjdVN2jr4nX8",
    'authDomain': "fir-9f329.firebaseapp.com",
    'databaseURL':"https://fir-9f329.firebaseio.com",
    'projectId': "fir-9f329",
    'storageBucket': "fir-9f329.appspot.com",
    'messagingSenderId': "1022042387286",
    'appId': "1:1022042387286:web:efbafb88c136023dd0dcf7",
    'measurementId': "G-F8NR0833P8"
}
firebase= pyrebase.initialize_app(config)
storage=firebase.storage()
path_local= input("enter name of file")
storage.child(path_on_cloud).put(path_local)
Url=storage.child(path_on_cloud).get_url(None)
print(Url)
