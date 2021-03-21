<template>
    <trading-vue :width="width" :data="this.$data"></trading-vue>
    
    <!-- <trading-vue :width="width" :data="thedata"></trading-vue> -->
</template>
<script>

import TradingVue from 'trading-vue-js'

export default {
    name: 'app',
    components: { TradingVue },
    props: ['width', 'thedata'],
    data() {
        return {
            ohlcv: this.thedata
        }
    }
}

</script>