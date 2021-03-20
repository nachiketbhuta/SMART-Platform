<template>
    <v-list>
        <p>Selected item no: {{ selected }}</p>
        <v-list-item-group color="info" mandatory v-model="selected">
            <v-list-item v-for="(item, i) in items" :key="i">
                <!-- <v-list-item-icon>
                                <v-icon v-text="item.icon"></v-icon>
                            </v-list-item-icon> -->
                <v-list-item-content>
                    <v-list-item-title v-text="item.text"></v-list-item-title>
                    <v-list-item-subtitle>
                        {{ item.price }}
                    </v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>
        </v-list-item-group>
    </v-list>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
    props: {
        items: {
            type: Array,
            required: true,
        },
    },
    data: () => ({
        selected: 0,
    }),
});
</script>
