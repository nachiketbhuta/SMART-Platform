<template>
    <v-container fluid>
        <h1>Dashboard</h1>
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
});
</script>
