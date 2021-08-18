import request from '@/utils/request'


// profile 
export function updateProfile(data) {
    return request({
        url: '/api/profile/1/',
        method: 'put',
        data
    })
}