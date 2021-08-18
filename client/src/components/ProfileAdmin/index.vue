<template>

    <el-row type="flex" justify="start">
        <el-form :model="form" label-position="left" label-width="80px">
            <el-form-item label="头像">
                <el-row type="flex" justify="space-between">
                    <el-col :span="12">
                        <el-avatar :size="100" :src="form.avater">
                        </el-avatar>
                    </el-col>
                    <el-col :span="12">
                        <el-upload action="#" ref="avatarUpload" :on-change="handleChange" :auto-upload="false">
                            <el-button size="small" type="primary">点击上传</el-button>

                        </el-upload>
                    </el-col>
                </el-row>
            </el-form-item>
            <el-form-item label="个人简介">
                <el-input v-model="form.descriotion" type="textarea" autosize></el-input>
            </el-form-item>
            <el-form-item label="邮箱">
                <el-input v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item label="Github">
                <el-input v-model="form.github"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="handleSave" round>保存</el-button>
            </el-form-item>
        </el-form>
    </el-row>


</template>

<script>
    import {
        fetchProfile
    } from "@/api/common.js"
    import {
        updateProfile
    } from "@/api/backend.js"

    export default {
        name: 'ProfileAdmin',
        props: {

        },
        components: {

        },

        data() {
            return {
                form: {}

            }
        },
        created() {
            this.handleProfile()
        },
        methods: {
            handleSave() {
                var fd = new FormData();
                // if (this.$refs.avatarUpload.uploadFiles.length != 0) {
                fd.append('avater', this.$refs.avatarUpload.uploadFiles[0].raw); //传文件
                // }
                fd.append('descriotion',this.form.descriotion)
                fd.append('email',this.form.email)
                fd.append('github',this.form.github)
                updateProfile(fd).then(response => {
                    console.log(response)
                })


            },

            handleProfile() {
                fetchProfile().then(response => {
                    console.log(response)
                    if (response.code == 1) {
                        this.form = response.data
                    }
                })
            },

            handleChange(file, fileList) {
                console.log(file, fileList)
            }

        },



    }
</script>

<style scoped>
    .el-row {
        margin-top: 5%;
        margin-left: 10%;
    }

    .el-input {
        width: 300px;
    }
</style>