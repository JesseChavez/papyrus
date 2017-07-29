<template>
  <v-app id="app" standalone>
    <v-navigation-drawer temporary v-model="drawer" :mini-variant="mini" dark overflow absolute>
      <v-list class="pa-0">
        <v-list-tile v-if="mini" @click.native.stop="mini = !mini">
          <v-list-tile-action>
            <v-icon light>chevron_right</v-icon>
          </v-list-tile-action>
        </v-list-tile>
        <v-list-tile avatar tag="div">
          <v-list-tile-avatar>
            <v-icon>account_circle</v-icon>
          </v-list-tile-avatar>
          <v-list-tile-content>
            <v-list-tile-title>Freddy Mercury</v-list-tile-title>
          </v-list-tile-content>
          <v-list-tile-action>
            <v-btn icon @click.native.stop="mini = !mini">
              <v-icon>chevron_left</v-icon>
            </v-btn>
          </v-list-tile-action>
        </v-list-tile>
      </v-list>

      <v-list class="pt-0" dense>
        <v-divider light></v-divider>
        <v-list-tile v-for="item in items" :key="item.title" :to="item.path">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>

    <v-toolbar fixed dark>
      <v-toolbar-side-icon @click.native.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Papyrus</v-toolbar-title>
    </v-toolbar>
    <main>
      <v-container fluid fill-height grid-list-xs>
        <v-layout row-sm column child-flex-sm>
          <v-flex xs12 md8 offset-md2 lg6 offset-lg3>
            <v-card class="grey lighten-4 ma-1">
              <v-card-text>
                <router-view></router-view>
                <!--v-router-->
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </main>
  </v-app>
</template>
<script>

require('./stylesheets/vuetify.min.css')
require('./stylesheets/sample.css')

export default {
  props: ['props'],
  data: function () {
    return {
      drawer: null,
      items: [
        { title: 'Home', icon: 'dashboard', path: '/' },
        { title: 'Register', icon: 'person_add', path: '/register' },
        { title: 'Login', icon: 'vpn_key', path: '/login' },
        { title: 'Documents', icon: 'insert_drive_file', path: '/documents' }
      ],
      mini: false,
      right: null
    }
  }
}
</script>
