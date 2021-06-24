<template>
  <div>
    <v-banner class="d-print-none mb-4" elevation="2">
      <v-avatar slot="icon" color="light-blue" size="40">
        <v-icon v-if="event.role == 'Призер'" icon="mdi-seal" color="white">
          mdi-seal
        </v-icon>
        <v-icon
          v-if="event.role == 'Победитель'"
          icon="mdi-seal-variant"
          color="white"
        >
          mdi-seal-variant
        </v-icon>
        <v-icon
          v-if="event.role == 'Участник'"
          icon="mdi-emoticon-happy"
          color="white"
        >
          mdi-emoticon-happy
        </v-icon>
        <v-icon
          v-if="event.role == 'Волонтер'"
          icon="mdi-hand-heart"
          color="white"
        >
          mdi-hand-heart
        </v-icon>
      </v-avatar>
      <h4 class="light-blue--text mb-1">{{ event.role }}</h4>
      {{ event.name }}
      <p class="subtitle-1">{{ event.date }}</p>
    </v-banner>

    <v-banner elevation="0" class="mb-4 my-print">
      <h4 class="mb-1">{{ event.role }}</h4>
      {{ event.name }}
      <p class="subtitle-1">{{ event.date }}</p>
    </v-banner>
  </div>
</template>
<script>
export default {
  name: "Event",
  props: ["event"]
};
</script>
<style lang="scss" scoped>
.my-print {
  display: none;
}
@media print {
  .my-print {
    display: block !important;
  }
}
</style>
