<template>
  <form @submit.prevent="updateDocument()">
    <div>
      <h1 class="display-1">Edit Document</h1>
    </div>
    <v-text-field
      name="name"
      label="Name"
      v-model="name"
      required
      ></v-text-field>

      <v-layout row wrap>
        <v-flex xs6>
          <v-radio label="Pdf" v-model="category" value="pdf"></v-radio>
        </v-flex>
        <v-flex xs6>
          <v-radio label="Url" v-model="category" value="url"></v-radio>
        </v-flex>
      </v-layout>

    <v-text-field
      v-if="category == 'url'"
      name="url"
      label="Url"
      v-model="url"
      ></v-text-field>

      <v-text-field
      v-if="category == 'pdf'"
      name="file"
      label=""
      v-model="file"
      type="file"
      ></v-text-field>

      <v-text-field
      name="remarks"
      label="Remarks"
      multi-line
      ></v-text-field>

      <div>
        <v-btn dark large type="submit">Update</v-btn>
        <v-btn large to="/documents">Cancel</v-btn>
      </div>
  </form>
</template>

<script>
export default {
  props: ['props'],
  data: function () {
    return {
      name: '',
      category: 'pdf',
      url: '',
      file: '',
      remarks: '',
    }
  },
  methods: {
    updateDocument() {
      console.log('----> patch doc')
    }
  }
}
</script>
