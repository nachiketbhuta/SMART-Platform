<template>
    <v-container>
        <nuxt-link to="/">Home</nuxt-link>
        <br />
        <v-row id="chartContainer">
            <v-col>
               <nuxt-child />
            </v-col>
        </v-row>

    </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Watchlist from "~/components/Watchlist.vue";
export default Vue.extend({
    layout: "main",
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
                price: 300.85,
            },
            {
                text: "TCS",
                price: 300.85,
            },
            {
                text: "TATASTEEL",
                price: 300.85,
            },
            {
                text: "WIPRO",
                price: 300.85,
            },
        ],
    }),
   
    //  mounted() {
    //      //Call tickrate more for this fix: https://nuxtjs.org/docs/2.x/features/nuxt-components/#the-client-only-component
    //     // this.initClientOnlyComp();
    //     console.log(this.$refs)
    // },
    // methods: {
    //     initClientOnlyComp(count = 10) {
    //         this.$nextTick(() => {
    //             if (this.$refs.myComp) {
    //                 //...
    //             } else if (count > 0) {
    //                 this.initClientOnlyComp(count - 1);
    //             }
    //         });
    //     },
    // },
    created() {
        this.$store.commit("setPageTitle", "Dashboard");
    },
});
</script>
