<template>
  <section>
    <h3 class="display-1 grey--text lighten-1"><b>Name: </b>{{ dataset.name }}</h3>
    <h1 class="display-1 blue--text darken-1"><b>Title: </b>{{ dataset.title }}</h1>
    <h1 class="display-1 blue--text darken-1"><b>Summary:</b></h1>
    <blockquote class="mb-5">
      {{ dataset.summary }}
    </blockquote>
    <div>
      <v-btn large to="/documents">List</v-btn>
    </div>
  </section>
</template>

<script>
export default {
  props: ['props'],
  data: function () {
    return {
      dataset: {
        id: null,
        name: '',
        title: '',
        summary: ''
      }
    }
  },
  methods: {
  },
  mounted() {
    var that = this
    console.log(this.$route)
    axios.get(`/documents/${this.$route.params.id}`, {
     params: {}
    }).then(function (response) {
      console.log(response);
      that.dataset = response.data
    }).catch(function (error) {
      console.log(error);
    });
  }
}
</script>
