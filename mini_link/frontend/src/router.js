import Vue from 'vue'
import VueRouter from 'vue-router'

import Searchbar from '@/components/SearchBar.vue'
import Login from '@/components/Login.vue'
import MyUrls from '@/components/MyUrls.vue'
import Register from '@/components/Register.vue'



const routes = [
  {path: '/', component: Searchbar},
  {path: '/login', component: Login},
  {path: '/register', component: Register},
  {path: '/urls', component: MyUrls},
  {path: '*', component: Searchbar},
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes
})

export default router
