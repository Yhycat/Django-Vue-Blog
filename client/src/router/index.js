import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/admin',
    name: 'Admin',
    redirect: '/admin/profile',
    component: () => import('@/views/Admin.vue'),
    children: [{
      path: 'profile',
      name: 'ProfileAdmin',
      component: () => import("@/components/ProfileAdmin/index"),
    }]
  },
  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '*',
    redirect: '/404',
    hidden: true
  }

]

const router = new VueRouter({
  routes
})





export default router