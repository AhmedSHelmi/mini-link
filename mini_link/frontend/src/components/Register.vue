<template>
<div>
  <h1>Register</h1>
    <div class="container _margin-x-auto">
      <form @submit.prevent="">
      <i-form-group>
      <i-input type="text" placeholder="First Name" required></i-input>
      </i-form-group>
      <i-form-group>
      <i-input type="text" placeholder="Last Name" required></i-input>
      </i-form-group>
      <i-form-group>
      <i-input type="email" placeholder="email" required></i-input>
      </i-form-group>
      <i-form-group>
      <i-input type="password" placeholder="password" required></i-input>
      </i-form-group>
      <i-form-group>
        <i-button type="submit">Register</i-button>
      </i-form-group>
      </form>
  </div>
</div>
</template>

<script>
export default {
name:"Register",
data(){
    return{

    }
}, methods:{

}
}
</script>

<style>

</style>