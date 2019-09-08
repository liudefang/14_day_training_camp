import Vue from 'vue'
import Router from 'vue-router'
// @绝对路径，检索到....src/

// 如果我们Router当做局部模块使用，一定要vue.use（Router）
// 以后在组件中，可以通过this.$router获取Router实例化对象
// 路由信息对象this.$route

import Home from '../components/Home/Home'
import Course from '../components/Course/Course'
import LightCourse from '../components/LightCourse/LightCourse'
import Micro from '../components/Micro/Micro'

Vue.use(Router);

// 配置路由规则
export default new Router({
  routes: [
    {
      path: '/',
      redirect:'/home'
      // component: HelloWorld
    },
    {
    	path:"/home",
    	name:'Home',
    	component:Home
    },
    {
    	path:"/course",
    	name:'Course',
    	component:Course
    },
    {
    	path:"/home/light-course",
    	name:'LightCourse',
    	component:LightCourse
    },
    {
    	path:"/micro",
    	name:'Micro',
    	component:Micro
    },
  ]
})
