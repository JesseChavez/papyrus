/* eslint no-console: 0 */

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './pages/Home.vue'
import Register from './pages/Register.vue'
import Login from './pages/Login.vue'

import App from './app.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Home },
  { path: '/register', component: Register },
  { path: '/login', component: Login },
]

const router = new VueRouter({
  routes, // short for `routes: routes`
  // mode: 'history'
})

document.addEventListener('DOMContentLoaded', () => {
  const node = document.getElementById('app')
  const data = JSON.parse(node.getAttribute('data'))

  const app = new Vue({
    el: '#app',
    router,
    components: { App },
    render: h => h(App, { props: { props: data} }),
  })
})
