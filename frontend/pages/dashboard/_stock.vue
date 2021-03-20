<template>
    <client-only>
        <div>
            <v-card color="teal" class="my-3">
                <v-card-title> {{ stock }} </v-card-title>
                <v-card-subtitle> {{ price }} </v-card-subtitle>
                <v-card-actions>
                    <v-btn v-if="!watchlist.includes(stock)" @click="addToWatchlist" color="teal" depressed>Add to Watchlist</v-btn>
                    <v-btn v-else @click="removeFromWatchlist" color="teal" depressed>Remove from Watchlist</v-btn>
                </v-card-actions>
            </v-card>
            <trading-vue
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
import Vue from "vue";
import firebase from 'firebase'
import sample_data from "@/utils/sample_data.json";

// import SetupIndicator from '~/components/SetupIndicator';
// Importing manually will also throw `windows is not defined error`
// Using `components: true` in nuxt.config.js
// import TradingVue from 'trading-vue-js'
export default Vue.extend({
    async asyncData({ params }) {
        const stock = params.stock.toUpperCase();
        return {
            stock,
        };
    },
    name: "StockChart",

    // Importing manually will also throw `windows is not defined error`
    // Using `components: true` in nuxt.config.js
    // components: { TradingVue }
    computed: {
        ext() {
            // TODO: For some reason the injections are initially
            // 'undefined'
            return Object.values(this.$ChartExtensions || {});
        },
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
        watchlist(){
            return this.$store.getters.watchlist
        }
    },
    data() {
        return {
            price: 967.8,
            // TODO: For some reason the injections are initially
            // 'undefined'
            tradingVue: this.$DataCube
                ? new this.$DataCube({
                      chart: {
                          type: "Candles",
                          data: sample_data.chart.data,
                          //   data: [
                          //       [1551128400000, 33, 37.1, 14, 14, 196],
                          //       [1551132000000, 13.7, 30, 6.6, 30, 206],
                          //       [1551135600000, 29.9, 33, 21.3, 21.8, 74],
                          //       [1551139200000, 21.7, 25.9, 18, 24, 140],
                          //       [1551142800000, 24.1, 24.1, 24, 24.1, 29],
                          //   ],
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
                : {},
            overlays: [this.$SetupIndicator],
        };
    },

    methods:{
        addToWatchlist(){
            // @ts-ignore
            this.watchlist.push(this.stock)
            let new_watchlist = this.watchlist
            const db = firebase.firestore()
            db.collection('users').doc(this.$store.getters.email).update({
                watchlist: new_watchlist
            })
            this.$store.commit('setWatchlist', new_watchlist)

        },
        removeFromWatchlist(){
            // @ts-ignore
            let new_watchlist = this.watchlist.filter(e => e != this.stock)
            const db = firebase.firestore()
            db.collection('users').doc(this.$store.getters.email).update({
                watchlist: new_watchlist
            })
            this.$store.commit('setWatchlist', new_watchlist)
        }
    }
});
</script>
