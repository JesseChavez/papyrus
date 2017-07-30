<template>
  <section>
    <div>
      <h1 class="display-1">Documents</h1>
    </div>
    <div>
      <v-subheader>
        <v-btn dark to="/documents/new">New Document</v-btn>
      </v-subheader>

      <v-data-table v-bind:headers="headers" :items="items" hide-actions>
        <template slot="items" scope="props">
          <td>{{ props.item.id }}</td>
          <td class="text-xs-right">{{ props.item.name }}</td>
          <td class="text-xs-right">{{ props.item.title }}</td>
          <td class="text-xs-right">
            <v-btn small primary :to="'/documents/' + props.item.id">View</v-btn>
          </td>
        </template>
      </v-data-table>
    </div>
  </section>
</template>

<script>
  export default {
    props: ['props'],
    data: function() {
      return {
        headers: [
          {
            text: '#',
            align: 'left',
            sortable: true,
            value: 'id'
          },
          { text: 'Name', value: 'name' },
          { text: 'Title', value: 'title' },
          { text: '', value: 'action' }
        ],
        items: []
      }
    },
    mounted() {
      var that = this
     console.log('fetching data ......')
      axios.get('/documents', {
        params: {}
      }).then(function (response) {
        console.log(response);
        that.items = response.data
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
</script>
