<template>
  <div>
    <v-banner elevation="2" class="d-print-none mb-4">
      <h4 class="light-blue--text mb-1">
        {{ project.name }}. Команда: {{ project.team }}
      </h4>
      {{ project.description }}
      <p class="subtitle-1">
        Даты проекта: от {{ project.dateStart }} до {{ project.dateEnd }}
      </p>
      {{ project.links }}
    </v-banner>

    <v-banner elevation="0" class="mb-4 my-print">
      <h4 class="mb-1">
        {{ project.name }}. Команда: {{ project.team }}
      </h4>
      {{ project.description }}
      <p class="subtitle-1">
        Даты проекта: от {{ project.dateStart }} до {{ project.dateEnd }}
      </p>
      {{ project.links }}
    </v-banner>
  </div>
</template>
<script>
export default {
  name: "Project",
  props: ["project"]
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
