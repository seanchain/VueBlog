// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App'
import router from './router'
import VueHighlightJS from 'vue-highlight.js'

require('shoelace-css/dist/shoelace.css')
require('highlight.js/styles/github.css')

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(VueHighlightJS)

import 'highlight.js/styles/github.css'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
