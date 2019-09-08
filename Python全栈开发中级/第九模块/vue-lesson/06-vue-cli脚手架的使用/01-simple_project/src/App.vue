<template>
  <div id="app">
    <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <div v-html="title"></div>
    <ul>
      <li v-for="(item,index) in datas":key = 'index'>
        {{item}}
      </li>
    </ul>
  <Home :text="text" @add="addHandler"/>
    <Header/>

  </div>
</template>

<script>
  // 导入
import Home from './components/Home/Home.vue'


  // 组件内部的业务逻辑
export default {
  name: 'app',
  components: {Home},
  data () {
    return {
      msg: '我们来学习vue-cli脚手架项目',
      title: '<h3>mike</h3>',
      datas:['跑步','爬山','马拉松'],
      text:"我是父组件的内容"
    }
  },
  // 挂载
  comments:{
    Home
  },
  methods:{
    addHandler(data){
      console.log(data);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
