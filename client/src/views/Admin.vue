<template>

    <el-container class="content">
        <el-aside :width="asideWidth">
            <el-menu ref="menu" :default-active="defaultActive" @select="handleSelect">
                <el-menu-item index="profile">
                    <i class="el-icon-user"></i>
                    <span slot="title">博客信息</span>
                </el-menu-item>
                <el-menu-item index="tag">
                    <i class="el-icon-collection-tag"></i>
                    <span slot="title">标签管理</span>
                </el-menu-item>
                <el-menu-item index="caegory">
                    <i class="el-icon-collection-tag"></i>
                    <span slot="title">分类管理</span>
                </el-menu-item>
                <el-menu-item index="article">
                    <i class="el-icon-notebook-2"></i>
                    <span slot="title">文章管理</span>
                </el-menu-item>
            </el-menu>

        </el-aside>
        <el-container class="container-right">
            <el-header>

                <el-row class="header-row" type="flex" align="middle" justify="space-between">
                    <el-col class="header-col" :span="4">


                    </el-col>
                </el-row>

            </el-header>
            <el-main>
                <div class="main">
                    <ProfileAdmin v-if="defaultActive='profile'" />
                </div>
            </el-main>
        </el-container>
    </el-container>


</template>

<script>
    import ProfileAdmin from "@/components/ProfileAdmin/index.vue"

    export default {
        name: 'Admin',
        props: {

        },
        components: {
            ProfileAdmin

        },

        data() {
            return {
                // 侧边栏默认宽度 
                asideWidth: "200px",

                // 默认激活的菜单栏
                defaultActive: "profile"


            }
        },
        beforeCreate() {

            console.log(this)

        },
        created() {},
        methods: {


            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },


        },



    }
</script>

<style scoped>
    .el-menu:not(.el-menu--collapse) {
        height: 100%;
        width: 199px;
    }


    .content {
        height: 100%;

    }

    .el-header {
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        padding: 0 0;
    }

    .el-button {
        font-size: 30px;
        height: 100%;
        border: 0;
        line-height: 0
    }

    .header-row {
        height: 100%;
    }

    .header-col {
        height: 100%;

    }

    /* .el-main {
        height: 100%;
    } */

    /* .main {
        height: 100%;
    } */
</style>