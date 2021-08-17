import axios from 'axios'
import {
  Message
} from 'element-ui'
import {
  get_token 
} from '@/utils/cookie'

// create an axios instance
const service = axios.create({
  baseURL: '/', // url = base url + request url
  timeout: 60000 // request timeout
})

// request interceptor
service.interceptors.request.use(
  config => {
      // 后端配合 Django jwt 验证
      if (get_token("jwt_token")){
        config.headers['Authorization'] = 'JWT ' + get_token("jwt_token")

      }
    


    return config
  },
  error => {
    console.log(error) // for debug
    return Promise.reject(error)
  }
)

service.interceptors.response.use(

  response => {
    // const res = response.data

    // if the custom code is not 20000, it is judged as an error.
    if (response.status !== 200) {
      Message({
        message: response.data.errors || 'Error',
        type: 'error',
        duration: 5 * 1000
      })


      return Promise.reject(new Error(response.data.errors || 'Error'))
    } else {
      return response.data
    }
  },
  error => {
    console.log(error) // for debug
    // Message({
    //   message: '请求错误,请联系系统管理员',
    //   type: 'error',
    //   duration: 5 * 1000
    // })
    // return Promise.reject(error)
  }
)

export default service