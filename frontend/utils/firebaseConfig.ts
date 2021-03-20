import firebase from 'firebase/app'
import 'firebase/auth'

const firebaseConfig = {
    apiKey: process.env.FIREBASE_API_KEY,
    authDomain: process.env.FIREBASE_AUTH_DOMAIN,
    projectId: process.env.FIREBASE_PROJECT_ID,
    storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
    messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
    appId: process.env.FIREBASE_APP_ID,
    measurementId: process.env.FIREBASE_MEASUREMENT_ID
};
console.log('Before Initialization: ', firebaseConfig);
const provider = new firebase.auth.GoogleAuthProvider()

if(!firebase.apps.length){
    firebase.initializeApp(firebaseConfig)
    console.log('After Initialization: ', firebaseConfig);
}

console.log('After If Initialization: ', firebaseConfig);
export { provider }
