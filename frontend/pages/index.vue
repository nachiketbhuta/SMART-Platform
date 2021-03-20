<template>
    <v-container fill-height fluid>
        <v-row align="center">
            <v-col class="text-center">
                <h1 class="text-h3 text-md-h2">
                    Your entry into the Stock Market
                </h1>
                <h5 class="text-h5 mt-2">
                    Get started with
                    <span class="teal--text text--accent-4">Commercio</span>
                </h5>
                <v-btn
                    v-if="!loggedIn"
                    @click="login"
                    class="white black--text mt-2"
                >
                    <v-img height="20" width="20" :src="googleIcon"></v-img>
                    <span class="ml-2">Login with Google</span>
                </v-btn>
                <v-btn @click="$router.push('/dashboard')" class="mt-3" v-else>
                    Go to Dashboard
                </v-btn>
                <br />
            </v-col>
        </v-row>
    </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import firebase from "firebase";
import { provider } from "@/utils/firebaseConfig";

export default Vue.extend({
    data() {
        return {
            googleIcon: require("@/assets/img/google-icon.svg"),
            email: "",
            displayName: "",
            token: "",
            loggedIn: false,
        };
    },
    created() {
        if (this.$store.state.email != "") {
            this.loggedIn = true;
        }
    },
    methods: {
        login() {
            firebase
                .auth()
                .signInWithPopup(provider)
                .then((result) => {
                    /** @type {firebase.auth.OAuthCredential} */
                    let credential = result.credential;
                    // @ts-ignore
                    let token = credential.accessToken;
                    let user = result.user;

                    console.log(user);
                    console.log(token);

                    if (user?.email && user?.displayName) {
                        this.email = user?.email;
                        this.displayName = user?.displayName;
                        this.token = token;

                        this.$store.commit("setEmail", this.email);
                        this.$store.commit("setDisplayName", this.displayName);
                        this.$store.commit("setToken", token);

                        //Check if new user
                        const db = firebase.firestore();
                        const userRef = db.collection("users").doc(user.email);
                        userRef
                            .get()
                            .then((docSnapshot) => {
                                if (!docSnapshot.exists) {
                                    userRef.set({
                                        email: user?.email,
                                        watchlist: [
                                            "INFY",
                                            "TCS",
                                            "ASIANPAINT",
                                            "WIPRO",
                                            "TATASTEEL",
                                        ],
                                    });
                                }
                            })
                            .catch((err) => {
                                console.error(
                                    "Failed to fetch user data from firestore: "
                                );
                                console.log(err);
                            });
                        //End of check new user

                        this.$router.push("/dashboard");
                    }
                })
                .catch((error) => {
                    console.error("Error while trying to sign in: \n" + error);
                });
        },
    },
});
</script>
