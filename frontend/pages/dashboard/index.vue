<template>
    <div>
        <h1 class="text-h3">Select a stock from your watchlist to monitor</h1>
        <watchlist :items="watchlist" />
    </div>
</template>

<script lang="ts">
import Vue from 'vue'
import firebase from 'firebase'
import Watchlist from '~/components/Watchlist.vue'

export default Vue.extend({
  components: { Watchlist },
    data: () => ({
        watchlist: [] as string[]
    }),
    mounted(){
        //Fetch user's watchlist
        const db = firebase.firestore()
        db.collection('users').doc(this.$store.getters.email).get()
        .then((doc) => {
            if(!doc.exists){
                alert("User data not found in the database. Logout and Login again")
            }
            else{
                // @ts-ignore
                this.watchlist = doc.data().watchlist as string[]
            }
        })
    }
})
</script>

<style>

</style>