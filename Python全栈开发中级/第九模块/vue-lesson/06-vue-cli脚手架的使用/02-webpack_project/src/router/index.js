// 整个路由的配置文件
// 让Vue使用此插件
import Vue from "vue";
import VueRouter from "vue-router";
import Home from '../components/Home/Home.vue'
import FreeCourse from '../components/FreeCourse/FreeCourse.vue'


// 使用此组件
Vue.use(VueRouter);

// Vue.protoype.$router = VueRouter


var router = new VueRouter({
	routes:[
		{
			path:'/',
			name:'Home',
			component:Home
		},
		{
			path:'/free',
			name:'FreeCourse',
			component:FreeCourse
		}

	]
})
export default router;
