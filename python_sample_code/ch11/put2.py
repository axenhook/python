from firebase import firebase
url = 'https://chiouapp01-74bde.firebaseio.com'
fb = firebase.FirebaseApplication(url, None)
fb.put(url + '/test/', data={"name":"Mary"}, name="mykey") 