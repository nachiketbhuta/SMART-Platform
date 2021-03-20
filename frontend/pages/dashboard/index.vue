<template>
    <div>
        <v-card class="mt-5" color="secondary">
            <v-row align="center" justify="start">
                <v-col cols="12" md="3">
                    <v-row align="center" justify="center">
                        <v-avatar color="primary" size="80">
                            <v-img :src="photoURL"></v-img>
                        </v-avatar>
                    </v-row>
                </v-col>
                <v-col class="text-center text-md-left">
                    <v-card-title>
                        {{ $store.getters.displayName }}
                    </v-card-title>
                    <v-card-subtitle>
                        {{ $store.getters.email }}
                    </v-card-subtitle>
                </v-col>
            </v-row>
        </v-card>
        <h1 class="text-subtitle-1 mt-5">Watchlist</h1>

        <watchlist :items="watchlist" />
    </div>
</template>

<script lang="ts">
import Vue from "vue";
import firebase from "firebase";
import Watchlist from "~/components/Watchlist.vue";

export default Vue.extend({
    components: { Watchlist },
    data: () => ({
        watchlist: [] as string[],
        photoURL: firebase.auth().currentUser?.photoURL,
    }),
    mounted() {
        //Set photoURL for first load
        this.photoURL = firebase.auth().currentUser?.photoURL;
        //Fetch user's watchlist
        const db = firebase.firestore();
        db.collection("users")
            .doc(this.$store.getters.email)
            .get()
            .then((doc) => {
                if (!doc.exists) {
                    alert(
                        "User data not found in the database. Logout and Login again"
                    );
                } else {
                    // @ts-ignore
                    this.watchlist = doc.data().watchlist as string[];
                }
            });
    },
});
</script>

<style>
</style>