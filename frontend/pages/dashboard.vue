<template>
    <v-container>
        <nuxt-link to="/">Home</nuxt-link>
        <h1>Dashboard</h1>
        <h2>Hello there, {{ $store.getters.displayName }}!</h2>
        <h6 class="text-h6">{{ $store.getters.email }}</h6>
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
    layout: 'main',
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
                price: 300.85
            },
            {
                text: "TCS",
                price: 300.85
            },
            {
                text: "TATASTEEL",
                price: 300.85
            },
            {
                text: "WIPRO",
                price: 300.85
            },
        ],
    }),
    methods: {
        
    },
    created(){
        this.$store.commit('setPageTitle', 'Dashboard')
    }
});
</script>
