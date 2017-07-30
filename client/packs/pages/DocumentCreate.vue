<template>
  <form enctype="multipart/form-data" @submit.prevent="createDocument()">
    <div>
      <h1 class="display-1">New Document</h1>
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

      <div v-if="category == 'pdf'" class="input-group input-group--text-field">
        <div class="input-group__input">
        <input name="pdf_file" type="file" @change="processFile($event)" accept="application/pdf">
        </div>
        <div class="input-group__details">
          <div class="input-group__messages"></div>
        </div>
      </div>

      <v-text-field
      name="remarks"
      label="Remarks"
      multi-line
      ></v-text-field>

      <div>
        <v-btn dark large type="submit">Create</v-btn>
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
      pdf_file: '',
      remarks: '',
    }
  },
  methods: {
    createDocument() {
      const form = new FormData()
      form.append('document[name]', this.name)
      form.append('document[category]', this.category)
      form.append('document[url]', this.url)
      form.append('document[remarks]', this.remarks)
      form.append('document[pdf_file]', this.pdf_file)

      var config = { headers: { 'Content-Type': 'multipart/form-data' } }

      var that = this

      axios.post('/documents', form, config
      ).then(function (response) {
        console.log(response);
        that.$router.push(`/documents/${response.data.id}`)
      }).catch(function (error) {
        console.log(error);
      });
    },
    processFile(event) {
      this.pdf_file = event.target.files[0]
      console.log(event.target.files)
    }
  }
}
</script>
