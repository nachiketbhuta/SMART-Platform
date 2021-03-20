<template>
    <v-app>
        <v-app-bar dense app>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-slide-x-transition>
                <h1 v-show="!drawer" class="text-h6">{{ pageTitle }}</h1>
            </v-slide-x-transition>
            <v-spacer />

            <v-btn depressed @click="logout">Logout</v-btn>
        </v-app-bar>
        <v-navigation-drawer color="teal" v-model="drawer" bottom app>
            <v-list-item>
                <v-list-item-content>
                    <v-list-item-title class="title">
                        Commercio
                    </v-list-item-title>
                    <v-list-item-subtitle> {{ $store.getters.email }} </v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list dense nav>
                <v-list-item v-for="item in navItems" :key="item.title" link :to="item.to">
                    <v-list-item-icon>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-main>
            <nuxt />
        </v-main>
    </v-app>
</template>

<script lang="ts">
import Vue from "vue";

import '@/utils/firebaseConfig' //To initialize app if not done already (i.e. when refreshing)
import firebase from 'firebase'

export default Vue.extend({
    data: () => ({
        drawer: true,
        navItems: [
            { title: "Dashboard", icon: "mdi-view-dashboard", to: "/dashboard" },
            { title: "Watchlist", icon: "mdi-image", to: "/watchlists" },
            { title: "Media Analysis", icon: "mdi-help-box", to: "/analysis" },
        ],
    }),
    computed:{
        pageTitle(){
            return this.$store.getters.pageTitle
        }
    },
    methods: {
        logout() {
            this.$store.commit("setEmail", "");
            this.$store.commit("setDisplayName", "");
            this.$store.commit("setToken", "");

            firebase.auth().signOut()

            this.$router.push("/");
        },
    },
});
</script>
