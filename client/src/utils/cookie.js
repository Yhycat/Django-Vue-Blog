import VueCookies from 'vue-cookies'

export function get_token(name) {
    return VueCookies.get(name)
}