import request from '@/utils/request'


// profile 数据库 理论只存在一条
export function fetchProfile() {
  return request({
    url: '/api/profile/1/',
    method: 'get',
    
  })
}



