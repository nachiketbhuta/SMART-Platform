<template>
    <v-container>
        <h1>Watchlists</h1>
    </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    layout: 'main',
     created(){
        this.$store.commit('setPageTitle', 'Watchlists')
    }
})
</script>
