<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card">
      <q-card-section class="bg-primary text-white">
        <div class="text-h6">First pvp tournament</div>
        <div class="text-subtitle2">by Petruha</div>
      </q-card-section>

      <q-separator />

      <q-card-actions align="right">
        <q-btn flat>Register now</q-btn>
        <q-btn flat>Follow</q-btn>
      </q-card-actions>
    </q-card>

    <q-card class="my-card">
      <q-card-section class="bg-purple text-white">
        <div class="text-h6">Second pvp tournament</div>
        <div class="text-subtitle2">by Sookast</div>
      </q-card-section>

      <q-card-actions align="around">
        <q-btn flat>Register now</q-btn>
        <q-btn flat>Follow</q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {
  name: 'PageIndex'
}
</script>
