<template>
  <el-container>
    <el-header height="30px">
      <div class="header">
        <NavHeader />
      </div>

    </el-header>
    <el-main>
      <div class="content">
        <el-row type="flex" :gutter="10" justify="space-between">
          <el-col :span="5">
            <Profile />
          </el-col>

          <el-col :span="14">
            <ArticleCardList />
          </el-col>

          <el-col :span="5">
            <PieChart />
          </el-col>
        </el-row>
      </div>


    </el-main>
  </el-container>
</template>

<script>
  // @ is an alias to /src
  import NavHeader from '@/components/NavHeader/index.vue'
  import Profile from '@/components/Profile/index.vue'
  import PieChart from '@/components/EchartGraph/PieChart.vue'
  import ArticleCardList from '@/components/ArticleCardList/index.vue'

  export default {
    name: 'Home',
    components: {
      NavHeader,
      Profile,
      PieChart,
      ArticleCardList
    }
  }
</script>


<style scoped>
  .el-main {
    background-color: #f5f4f4;
    height: 100%;
    padding-top: 0px;
  }

  .content {
    padding-top: 10px;
    padding-left: 5%;
    padding-right: 5%;

  }

  .header {
    padding-left: 5%;
    padding-right: 5%;
    height: 100%;


  }

  .el-container {
    height: 100%;

  }

  .NavHeader {
    margin: auto;
    position: absolute;
  }
</style>