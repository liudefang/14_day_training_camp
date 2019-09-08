import Vue from 'vue'
import App from './App.vue'


// 1.引入全局的组件
import Header from './components/Common/Header.vue'
// 2.注册全局组件
Vue.component(Header.name, Header);
new Vue({
  el: '#app',
  render: h => h(App)
})
