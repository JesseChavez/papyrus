/* eslint no-console: 0 */

import Vue from 'vue'
import App from './app.vue'

document.addEventListener('DOMContentLoaded', () => {
  const node = document.getElementById('app')
  const data = JSON.parse(node.getAttribute('data'))

  const app = new Vue({
    el: '#app',
    components: { App },
    render: h => h(App, { props: { props: data} }),
  })
})
