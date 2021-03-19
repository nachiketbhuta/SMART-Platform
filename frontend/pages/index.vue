<template>
    <v-row align="center" style="outline: 1px solid red">
        <v-col class="text-center">
            <h1 class="text-h3 text-md-h2">Your entry into the Stock Market</h1>
            <h5 class="text-h5 mt-2">
                Get started with
                <span class="teal--text text--accent-4">Commercio</span>
            </h5>
            <v-btn @click="login" class="white black--text mt-2">
                <v-img height="20" width="20" :src="googleIcon"></v-img>
                <span class="ml-2">Login with Google</span>
            </v-btn>
            <br />
            {{ email }}<br />
            {{ displayName }}
        </v-col>
    </v-row>
</template>

<script lang="ts">
import Vue from "vue";
import firebase from 'firebase'
import { provider } from "@/utils/firebaseConfig";

export default Vue.extend({
    data() {
        return {
            googleIcon: require("@/assets/img/google-icon.svg"),
            email: '',
            displayName: '',
            token: '',
        };
    },
    methods: {
        login() {
            firebase.auth().signInWithPopup(provider)
            .then((result) => {
                /** @type {firebase.auth.OAuthCredential} */
                let credential = result.credential
                // @ts-ignore
                let token = credential.accessToken
                let user = result.user
                
                console.log(user)
                console.log(token)

                if(user?.email && user?.displayName){
                    this.email = user?.email
                    this.displayName = user?.displayName
                    this.token = token

                    this.$store.commit('setEmail', this.email)
                    this.$store.commit('setDisplayName', this.displayName)
                    this.$store.commit('setToken', token)
                }
               

            })
            .catch((error) => {
                console.error("Error while trying to sign in: \n" + error)
            })
        },
    },
});
</script>
