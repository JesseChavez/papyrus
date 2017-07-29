<template>
  <div id="app">
    <p>
    <router-link to="/">Home</router-link>
    <router-link to="/register">register</router-link>
    <router-link to="/login"> log in </router-link>
    </p>
    <hr>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  props: ['props'],
  data: function () {
    return {
      message: "Hello Vue!"
    }
  }
}
</script>

<style scoped>
p {
  font-size: 2em;
  text-align: center;
}
</style>
