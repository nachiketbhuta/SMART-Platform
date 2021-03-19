<template>
    <v-container fluid>
        <nuxt-link to="/">Home</nuxt-link>
        <h1>Dashboard</h1>
        <h2>Hello there, {{ $store.getters.displayName }}!</h2>
        <v-btn @click="logout">Log out</v-btn>
        <v-row>
            <v-col cols="12" md="6">
                <watchlist :items="items" />
            </v-col>
            <v-col cols="12" md="6"> Chart </v-col>
        </v-row>
    </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Watchlist from "~/components/Watchlist.vue";
export default Vue.extend({
    components: { Watchlist },
    async asyncData({ store, redirect }) {
        if (store.getters.email == "" || store.getters.email == undefined) {
            redirect(200, "/");
        }
    },
    data: () => ({
        items: [
            {
                text: "INFY",
            },
            {
                text: "TCS",
            },
            {
                text: "TATASTEEL",
            },
            {
                text: "WIPRO",
            },
        ],
    }),
    methods: {
        logout() {
            this.$store.commit("setEmail", "");
            this.$store.commit("setDisplayName", "");
            this.$store.commit("setToken", "");

            this.$router.push('/')
        },
    },
});
</script>
