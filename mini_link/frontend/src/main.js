import Vue from 'vue'
import store from '@/store'
import router from '@/router'
import HighchartsVue from 'highcharts-vue'
import VueQRCodeComponent from 'vue-qrcode-component'
import '@inkline/inkline/dist/inkline.css';
import Inkline from '@inkline/inkline';

import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


Vue.use(HighchartsVue)
Vue.use(Inkline);
Vue.component('qr-code', VueQRCodeComponent)



import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false







new Vue({
  router,
  store,
  
render: h => h(App)
}).$mount('#app')
