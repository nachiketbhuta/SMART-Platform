<!-- API for searching: https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=SBI&apikey=XYZ -->
<template>
    <div>
        <v-combobox
            @input="fetchStocks"
            @change="onSelected"
            color="secondary"
            placeholder="Search stocks"
            style="max-height: fit-content !important; height: 50px"
            solo
            v-model="selected"
            :items="items"
        >
            <template v-slot:no-data>
                <v-list-item>
                    <span class="subheading">No results</span>
                </v-list-item>
            </template>
            <template v-slot:item="{ index, item }">
                <v-chip-group>
                    <v-chip color="teal" dark label small>
                        {{ item[Object.keys(item)[0]] }}
                    </v-chip>
                    <v-chip color="secondary" dark label small>
                        {{ item[Object.keys(item)[1]] }}
                    </v-chip>
                </v-chip-group>
            </template>
        </v-combobox>
    </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
    data: () => ({
        selected: "",
        editing: null,
        items: [],
    }),

    methods: {
        fetchStocks() {
            this.$axios
                .$get(
                    `https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=${this.selected}&apikey=XYZ`
                )
                .then((data) => {
                    this.items = data.bestMatches;
                    console.log(data);
                });
        },
        onSelected() {
            //Phew. This finally does it!
            if (typeof this.selected == "object") {
                this.$router.push(
                    "/dashboard/" + this.selected[Object.keys(this.selected)[0]]
                );
                this.selected = "";
            }
        },
    },
});
</script>
