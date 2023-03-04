import Vue from 'vue'
import App from './App'
import Store from '@/store'
// MinUI
import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'

Vue.use(MintUI)

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
    store: Store,
}).$mount('#app')
