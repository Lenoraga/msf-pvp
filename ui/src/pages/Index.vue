<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" v-for="tournament in data.tournaments" :key="'tournament' + tournament.id">
      <q-card-section class="bg-primary text-white">
        <div class="text-h6">{{tournament.name}}</div>
        <div class="text-subtitle2">{{tournament.description}}</div>
      </q-card-section>

      <q-separator />

      <q-card-actions align="right">
        <q-btn flat>Register now</q-btn>
        <q-btn flat>Follow</q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
const axios = require('axios')
export default {
  name: 'PageIndex',
  data () {
    return {
      data: {}
    }
  },
  beforeMount () {
    this.getTournaments()
  },
  methods: {
    getTournaments () {
      axios
        .get('/api/tournaments')
        .then(response => (
          this.data = response.data
        ))
    }
  }
}
</script>
