<template>
    <v-container>
        <h1>Analysis</h1>
    </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
    layout: 'main',
     created(){
        this.$store.commit('setPageTitle', 'Sentiment Analysis of Media')
    }
})
</script>
