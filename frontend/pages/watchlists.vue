<template>
    <v-container>
        <h1>Watchlist</h1>
        {{ valid }}
        <v-form @submit.prevent="searchAndAdd" ref="form" v-model="valid">
            <v-text-field
                :rules="rules"
                placeholder="Add a stock"
                solo
                v-model="search"
            ></v-text-field>
        </v-form>

        <v-list>
            <v-list-item v-for="(item, i) in watchlist" :key="i">
                <v-list-item-content>
                    <v-list-item-title v-text="item"></v-list-item-title>
                </v-list-item-content>
                <v-list-item-action>
                    <v-row>
                        <v-btn :to="'/dashboard/' + item" icon>
                            <v-icon>mdi-open-in-new</v-icon>
                        </v-btn>
                        <v-btn
                            color="red"
                            @click="removeFromWatchlist(item)"
                            icon
                        >
                            <v-icon>mdi-close</v-icon>
                        </v-btn>
                    </v-row>
                </v-list-item-action>
            </v-list-item>
        </v-list>
    </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import firebase from "firebase";

export default Vue.extend({
    layout: "main",
    data: () => ({
        watchlist: [] as string[],
        search: "",
        valid: false,
    }),
    computed: {
        regex_for_rules() {
            return new RegExp(this.watchlist.join("|"), "i");
        },
        rules() {
            return [
                (v: string) => !!v || "Value is required",
                (v: string) => {
                    const alreadyExists: Boolean = this.regex_for_rules.test(v);
                    return !alreadyExists || "Already in Watchlist";
                },
            ];
        },
    },
    created() {
        this.$store.commit("setPageTitle", "Watchlist");
    },
    mounted() {
        this.getWatchlist();
    },
    methods: {
        getWatchlist() {
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
        searchAndAdd() {
            if(this.valid){
                alert(this.search);
            }
        },
        removeFromWatchlist(item: string) {
            const db = firebase.firestore();
            db.collection("users")
                .doc(this.$store.getters.email)
                .update({
                    watchlist: this.watchlist.filter((e) => e != item),
                })
                .catch((err) => {
                    console.error("Error while deleting item in database: ")
                    console.log(err)
                })
            
            this.getWatchlist()
        },
    },
});
</script>
