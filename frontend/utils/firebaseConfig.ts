import firebase from 'firebase/app'
import 'firebase/auth'

const firebaseConfig = {
    apiKey: "AIzaSyB8pz6TpdcTkNEDg_2qtFCAFBZOJZxAmDw",
    authDomain: "commerciohacknitr.firebaseapp.com",
    projectId: "commerciohacknitr",
    storageBucket: "commerciohacknitr.appspot.com",
    messagingSenderId: "310493090916",
    appId: "1:310493090916:web:99f50f48a9cd9b424c3b71",
    measurementId: "G-80SESQ99RN"
};

const provider = new firebase.auth.GoogleAuthProvider()

if(!firebase.apps.length){
    firebase.initializeApp(firebaseConfig)
}
export { provider }
