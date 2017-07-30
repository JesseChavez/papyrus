<template>
  <form @submit.prevent="register()">
    <div>
      <h1 class="display-1">Register</h1>
    </div>
    <v-text-field
      name="first_name"
      label="First name"
      v-model="first_name"
      required
      ></v-text-field>

    <v-text-field
      name="last_name"
      label="Last name"
      v-model="last_name"
      required
      ></v-text-field>

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

    <v-text-field
      name="password_confirmation"
      label="Confirm your password"
      v-model="password_confirmation"
      required
      type="password"
      counter
      ></v-text-field>

      <div>
        <v-btn dark large type="submit">Submit</v-btn>
      </div>
  </form>
</template>

<script>
export default {
  props: ['props'],
  data: function () {
    return {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      password_confirmation: '',
    }
  },
  methods: {
    register() {
      console.log('-----> post register form')
    }
  }
}
</script>
