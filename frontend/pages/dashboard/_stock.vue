<template>
    <client-only>
        <div>
            <v-card color="teal" class="my-3">
                <v-card-title> {{ stock }} </v-card-title>
                <v-card-subtitle> {{ price }} </v-card-subtitle>
                <v-card-actions>
                    <v-btn
                        v-if="!watchlist.includes(stock)"
                        @click="addToWatchlist"
                        color="teal"
                        depressed
                        >Add to Watchlist</v-btn
                    >
                    <v-btn
                        v-else
                        @click="removeFromWatchlist"
                        color="teal"
                        depressed
                        >Remove from Watchlist</v-btn
                    >
                </v-card-actions>
            </v-card>
            <trading-vue
                ref="tradingVueRef"
                :width="chartWidth"
                :data="tradingVue"
                :overlays="overlays"
                :extensions="ext"
                :legend-buttons="['display']"
            >
            </trading-vue>

            <v-row>
                <v-col cols="12" md="6">
                    <h1 class="text-h5">Top Tweets</h1>
                </v-col>
                <v-col cols="12" md="6">
                    <h1 class="text-h5">Top News</h1>
                </v-col>
            </v-row>
        </div>
    </client-only>
</template>

<script lang="ts">
//API: http://smart-platform-hacknitr.herokuapp.com/docs#/
//Single Stock Quote: https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=demo

import Vue from "vue";
import firebase from "firebase";
// @ts-ignore: Dont check
// import sample_data from "@/utils/sample_data.json";
// import INFY_MONTHLY from "@/utils/INFY_MONTHLY.json";

// import SetupIndicator from '~/components/SetupIndicator';
// Importing manually will also throw `windows is not defined error`
// Using `components: true` in nuxt.config.js
// import TradingVue from 'trading-vue-js'
export default Vue.extend({
    // @ts-ignore: Dont check
    async asyncData({ params, store, $axios }) {
        const stock = params.stock.toUpperCase();
        const api_url = store.getters.api_url;

        const stock_data = await $axios.$get("http://" + api_url + `/alpha/timeseries/${stock}/TIME_SERIES_MONTHLY`)

        //Testing purpose
        // const stock_data = INFY_MONTHLY;

        return {
            stock,
            stock_data,
        };
    },
    name: "StockChart",

    // Importing manually will also throw `windows is not defined error`
    // Using `components: true` in nuxt.config.js
    // components: { TradingVue }
    computed: {
        ext(): any {
            // TODO: For some reason the injections are initially
            // 'undefined'
            // @ts-ignore: Dont check
            return Object.values(this.$ChartExtensions || {});
        },
        chartWidth(): any {
            // @ts-ignore: Dont check
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
        watchlist(): any {
            return this.$store.getters.watchlist;
        },
        tradingVue() {
            // @ts-ignore
            return this.$DataCube
                ? // @ts-ignore: Dont check
                  new this.$DataCube({
                      chart: {
                          type: "Candles",
                          // @ts-ignore
                          data: this.$store.getters.stockData,
                      },
                      onchart: [
                          {
                              name: "Setups",
                              type: "Setups",
                              data: [[1551128400000, 1, 35]],
                              settings: {},
                          },
                      ],
                  })
                : {};
        },
    },
    data() {
        return {
            price: 967.8,
            finalData: [] as any[],

            // @ts-ignore: Dont check
            overlays: [this.$SetupIndicator],
        };
    },

    methods: {
        process_raw_stock_data() {
            // @ts-ignore
            const data = this.stock_data["Monthly Time Series"];
            let new_data: any[][] = [];

            for (const [key, value] of Object.entries(data)) {
                //Convert key in normal date form to seconds and put in array as first
                let to_push = [new Date(key).getTime()];
                for (const [key2, value2] of Object.entries(value as Object)) {
                    to_push.push(+value2);
                }
                new_data.push(to_push);
            }
            //Finally reverse the array, as we need in ascending order dates low to high
            new_data.reverse();
            console.log(new_data);

            this.$store.commit("setStockData", new_data);

            this.finalData = new_data;
        },
        addToWatchlist() {
            // @ts-ignore
            this.watchlist.push(this.stock);
            let new_watchlist = this.watchlist;
            const db = firebase.firestore();
            db.collection("users").doc(this.$store.getters.email).update({
                watchlist: new_watchlist,
            });
            this.$store.commit("setWatchlist", new_watchlist);
        },
        removeFromWatchlist() {
            // @ts-ignore
            let new_watchlist = this.watchlist.filter((e) => e != this.stock);
            const db = firebase.firestore();
            db.collection("users").doc(this.$store.getters.email).update({
                watchlist: new_watchlist,
            });
            this.$store.commit("setWatchlist", new_watchlist);
        },
    },
    created() {
        this.process_raw_stock_data();
    },
    mounted() {},
});
</script>
