<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          msf-pvp
          <!-- <q-img src="static/marvelstrikeforce_lob_log_01.png"></q-img>-->
        </q-toolbar-title>
        <div class="gt-sm">
          <q-btn outline rounded label="sign up" class="q-mr-sm"></q-btn>
          <q-btn outline rounded label="sign in"></q-btn>
        </div>
        <div>
          <q-btn
            class="lt-md"
            flat
            dense
            round
            @click="leftDrawerOpen = !leftDrawerOpen"
            icon="menu"
            aria-label="Menu"
          />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" bordered content-class="bg-grey-1">
      <q-list>
        <q-item-label header class="text-grey-8">Menu</q-item-label>
        <EssentialLink v-for="link in essentialLinks" :key="link.title" v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
// import EssentialLink from 'components/EssentialLink.vue'

const linksData = [
  {
    title: 'Sign up',
    caption: 'registration0',
    icon: 'school',
    link: 'registration1'
  },
  {
    title: 'Sign in',
    caption: 'log in0',
    icon: 'favorite',
    link: 'log in1'
  }
]

export default {
  name: 'MainLayout',
  // components: { EssentialLink },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  }
}
</script>
