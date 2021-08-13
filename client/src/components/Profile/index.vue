<template>

    <el-card>
        <el-row type="flex" align="middle" justify="center">
            <div>
                <el-avatar :size="100" :src="profile.avatar_url">
                </el-avatar>
            </div>
        </el-row>
        <el-row type="flex" align="middle">
            <span class="text">There is only one success to be able to spend your life in your own favorite way.</span>
        </el-row>

        <el-row type="flex" class="tag" align="middle" justify="space-between">
            <el-col :span="8">
                Article
            </el-col>
            <el-col :span="8">
                Category
            </el-col>
            <el-col :span="8">
                Tag
            </el-col>
        </el-row>
        <el-row type="flex" class="tag" align="middle" justify="space-between">
            <el-col :span="8">
                <el-link :underline="false" class="number-link">2</el-link>

            </el-col>
            <el-col :span="8">
                <el-link :underline="false" class="number-link">2</el-link>

            </el-col>
            <el-col :span="8">
                <el-link :underline="false" class="number-link">2</el-link>

            </el-col>
        </el-row>
    </el-card>

</template>

<script>
    export default {
        name: 'Profile',
        props: {

        },
        components: {

        },

        data() {
            return {

                profile: {}

            }
        },
        created() {

        },
        methods: {

        },



    }
</script>

<style scoped>
    .el-card {
        width: 100%;

    }

    .el-row {
        margin-bottom: 20px;
    }

    .number-link {
        font-size: 32px;

    }

    .text {
        text-align: center;

    }

    .tag {
        text-align: center;
        font-size: 16px;

    }
</style>