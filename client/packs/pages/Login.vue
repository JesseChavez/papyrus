<template>
  <form @submit.prevent="login()">
    <div>
      <h1 class="display-1">Login</h1>
    </div>
    <v-text-field
      name="email"
      label="Email"
      v-model="email"
      required
      ></v-text-field>

    <v-text-field
      name="password"
      label="Enter your password"
      hint="At least 8 characters"
      v-model="password"
      required
      type="password"
      counter
      ></v-text-field>

      <div>
        <v-btn dark large>Submit</v-btn>
      </div>
  </form>
</template>

<script>
export default {
  props: ['props'],
  data: function () {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    login() {
      console.log('----> post login form')
    }
  }
}
</script>
