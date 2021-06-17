<template>
  <v-banner elevation="2" class="mb-4">
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
</template>
<script>
export default {
  name: "Event",
  props: ["event"]
};
</script>
<style lang="scss" scoped></style>
