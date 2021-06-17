<template>
  <v-banner elevation="2" class="mb-4">
    <h4 class="light-blue--text mb-1">
      {{ project.name }}. Команда: {{ project.team }}
    </h4>
    {{ project.description }}
    <p class="subtitle-1">
      Даты проекта: от {{ project.dateStart }} до {{ project.dateEnd }}
    </p>
    {{ project.links }}
  </v-banner>
</template>
<script>
export default {
  name: "Project",
  props: ["project"]
};
</script>
<style lang="scss" scoped></style>
