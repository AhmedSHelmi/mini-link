<template>
<div>
  <h1>Login</h1>
  <div class="container _margin-x-auto">
      <form @submit.prevent="">
      <i-form-group>
      <i-input type="email" placeholder="email" required></i-input>
      </i-form-group>
      <i-form-group>
      <i-input type="password" placeholder="password" required></i-input>
      </i-form-group>
      <i-form-group>
        <i-button type="submit">Login</i-button>
      </i-form-group>
      </form>
  </div>
</div>
</template>

<script>
export default {
name:"Login",
data(){
    return{

    }
}, methods:{

}
}
</script>

<style scoped>
.container{
    margin-top:10%;
    width:40%;
}
</style>