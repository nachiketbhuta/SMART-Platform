<template>
    <v-container>
        <nuxt-link to="/">Home</nuxt-link>
        <br />
        <v-row id="chartContainer">
            <!-- <v-col cols="12" md="6">
                <watchlist :items="items" />
            </v-col> -->
            <v-col cols="12" md="6">
                <!-- <chart
                    :width="chartWidth"
                    :height="200"
                    :colors="{
                        back: '#2c2c2c',
                        grid: '#cccccc',
                        text: 'white',
                        tvTitle: 'red',
                    }"
                /> -->
                <chart-2 />
            </v-col>
        </v-row>

        <br />

        <v-row>
            <v-col cols="12" md="6">
                <h1 class="text-h5">Top Tweets</h1>
            </v-col>
            <v-col cols="12" md="6">
                <h1 class="text-h5">Top News</h1>
            </v-col>
        </v-row>
    </v-container>
</template>

<script lang="ts">
import Vue from "vue";
import Chart from "~/components/Chart.vue";
import Watchlist from "~/components/Watchlist.vue";
export default Vue.extend({
    layout: "main",
    components: { Watchlist, Chart },
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
    computed: {
        chartWidth() {
            switch (this.$vuetify.breakpoint.name) {
                case "xs":
                    return 450;
                case "sm":
                    return 450;
                case "md":
                    return 800;
                case "lg":
                    return 1000;
                case "xl":
                    return 1100;
            }
        },
    },
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
