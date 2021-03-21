<template>
    <v-container>
        <v-row id="chartContainer">
            <v-col>
                <nuxt-child />
            </v-col>
        </v-row>
    </v-container>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
    layout: "main",
    async asyncData({ store, redirect }) {
        if (store.getters.email == "" || store.getters.email == undefined) {
            redirect(200, "/");
        }
    },
    data: () => ({}),
    created() {
        this.$store.commit("setPageTitle", "Dashboard");
    },
});
</script>
