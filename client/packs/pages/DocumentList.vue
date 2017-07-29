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
            <v-btn small warning :to="'/documents/' + props.item.id + '/edit'">Edit</v-btn>
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
            sortable: false,
            value: 'id'
          },
          { text: 'Name', value: 'name' },
          { text: 'Title', value: 'title' },
          { text: '', value: 'action' }
        ],
        items: [
          {
            id: 1,
            name: 'Frozen Yogurt',
            title: 'Random title',
          },
          {
            id: 2,
            name: 'Frozen Yogurt 2',
            title: 'Random title 2',
          },
          {
            id: 3,
            name: 'Frozen Yogurt 3',
            title: 'Random title 3',
          },
          {
            id: 4,
            name: 'Frozen Yogurt 4',
            title: 'Random title 4',
          },
        ]
      }
    },
    mounted() {
     console.log('fetching data ......')
    }
  }
</script>
