import Vue from 'vue'
import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'
import App from './App'

Vue.use(MintUI)

/* eslint-disable no-new */
Vue.config.productionTip = false

new Vue({
    render: h => h(App),
}).$mount('#app')
