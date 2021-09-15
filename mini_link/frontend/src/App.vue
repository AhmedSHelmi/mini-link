<template lang="html">
  <div class="container ">
  <div class="_fixed-top _clearfix">
    <i-button @click="$router.push('/')"> <i-icon icon="home" /></i-button>
    <!--Dark mode ;)-->
    <i-button @click="toggleDarkMode" class="_float-left"> <i-icon icon="light" /></i-button>
    <i-button @click="$router.push('/login')" class="_float-right">login</i-button>
    <i-button @click="$router.push('/register')" class="_float-right">Register</i-button>

  </div>
    <router-view class="v-centered"/>
  <footer class="_fixed-bottom">
    <center>Developed by Ahmed Helmi</center>
  </footer>
  </div>
</template>

<script>

export default {
  name: 'MiniLink',
  components: { 
  },
  data(){
    return{

    }
  },
  methods:{
      toggleDarkMode() {
            this.$inkline.config.variant = this.$inkline.config.variant === 'light' ? 'dark' : 'light';
        },

  }

}
</script>
<style scoped>
.v-centered{
  padding-top:100px
  
  

}
</style>