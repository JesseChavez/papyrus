/* eslint no-console: 0 */

import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuetify from 'vuetify'

import App from './app.vue'
import Home from './pages/Home.vue'
import Register from './pages/Register.vue'
import Login from './pages/Login.vue'
import DocumentList from './pages/DocumentList.vue'
import DocumentCreate from './pages/DocumentCreate.vue'
import DocumentRead from './pages/DocumentRead.vue'
import DocumentUpdate from './pages/DocumentUpdate.vue'

Vue.use(VueRouter)
Vue.use(Vuetify)

const routes = [
  { path: '/', component: Home },
  { path: '/register', component: Register },
  { path: '/login', component: Login },
  { path: '/documents', component: DocumentList },
  { path: '/documents/new', component: DocumentCreate },
  { path: '/documents/:id', component: DocumentRead },
  { path: '/documents/:id/edit', component: DocumentUpdate },
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
