<template>
    <div>
        <v-row>
            <v-col cols="12" md="6">
                <v-card class="mt-5" color="secondary">
                    <v-row align="center" justify="start">
                        <v-col cols="12" md="3">
                            <v-row align="center" justify="center" class="mt-3 ma-md-0">
                                <v-avatar color="primary" size="80">
                                    <v-img :src="photoURL"></v-img>
                                </v-avatar>
                            </v-row>
                        </v-col>
                        <v-col>
                            <v-card-title class="justify-center justify-md-start">
                                {{ $store.getters.displayName }}
                            </v-card-title>
                            <v-card-subtitle class="text-center text-md-left">
                                {{ $store.getters.email }}
                            </v-card-subtitle>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
        <h1 class="text-subtitle-1 mt-5">Watchlist</h1>

        <watchlist :items="watchlist" />
    </div>
</template>

<script lang="ts">
import Vue from "vue";
import firebase from "firebase";
import Watchlist from "~/components/Watchlist.vue";
import { refresh } from "less";

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
                        "User doc not found in system."
                    );
                } else {
                    // @ts-ignore
                    this.watchlist = doc.data().watchlist as string[];
                    // @ts-ignore
                    this.$store.commit('setWatchlist', doc.data().watchlist as string[])
                }
            });
    },
});
</script>

<style>
</style>