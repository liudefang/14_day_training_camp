<template>
  <div class="home">
    我是首页========={{text}}

    <button @click="addHandler">触发</button>
  </div>
    
</template>

<script>
    export default {
        name: "Home",
      methods:{
          addHandler() {
            this.$emit('add','哈哈哈')
          }
      },
      data(){
          return {

          };

      },
      // 使用props进行接收
      props:['text']
    };

</script>

<style scoped>

</style>
