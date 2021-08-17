<template>
    <el-row type="flex" justify="center" align="middle">

        <el-card>
            <el-row type="flex" justify="center" align="middle">
                <el-form ref="loginForm" :model="loginForm" label-width="80px" label-position="left">
                    <el-form-item label="账户">
                        <el-input v-model="loginForm.username" placeholder="请输入账号"></el-input>
                    </el-form-item>
                    <el-form-item label="密码">
                        <el-input v-model="loginForm.password" @keyup.enter.native="handleLogin" placeholder="请输入密码"
                            show-password></el-input>
                    </el-form-item>

                    <el-row>
                        <el-button type="primary" @click="handleLogin">立即登录</el-button>
                    </el-row>
                </el-form>
            </el-row>

        </el-card>
    </el-row>

</template>

<script>
    import {
        login
    } from '@/api/user.js'
    import {
        successMessage
    } from '@/utils/message.js'

    export default {
        name: 'Login',
        props: {

        },
        components: {

        },

        data() {
            return {
                loginForm: {
                    "username": "admin",
                    "password": "admin"
                },

            }
        },
        created() {

        },
        methods: {
            handleLogin() {

                login(this.loginForm).then(response => {

                    var token = response.data.token
                    var expire_times = response.data.expire_times
                    this.$cookies.set("jwt_token", token, expire_times)

                    successMessage("登录成功")
                    return this.$router.push("/admin")


                })
            },

        }
    }
</script>

<style scoped>
    .el-form-item {
        text-align: center;
        margin-top: 30px;
    }

    .el-card {
        text-align: center;
        height: 500px;
        width: 500px;
    }

    .el-form {
        width: 300px;
        margin-top: 15%;
        text-align: center;
    }

    .el-checkbox {
        float: left;
        margin-top: 20px;
    }

    .el-button {
        margin-top: 30px;
        width: 300px;
    }
</style>