import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '@/assets/css/global.css'
import App from './App.vue';
import router from '@/router/index'
import VueCookies from 'vue-cookies'
import {
  auth
} from '@/api/user.js'

Vue.use(ElementUI);
Vue.use(VueCookies);

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')


router.beforeEach((to, from, next) => {
  //to: 去哪个路由
  //from: 从哪个路由来
  //next：是一个方法，使用路由拦截，必须在后面添加next()，否则路由无法跳转

  console.log(to)
  console.log(from)

  if (to.name == "Admin") {
    // 权限确认
    auth().then(response => {
      console.log(response)
      if (response.data.is_superuser) {
        next()
      } else {
        router.push("/404")
      }
    })
  } else {
    next()
  }




  //路由拦截可根据项目返回的权限自行调整，这里只是做了一个简单的例子
})