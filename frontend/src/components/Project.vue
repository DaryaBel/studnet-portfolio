<template>
  <div>
    <v-banner elevation="2" class="d-print-none mb-4">
      <h4 class="light-blue--text mb-1">
        {{ project.project.name }}. Команда: {{ project.name }}
      </h4>
      {{ project.project.description }}
      <p class="subtitle-1">
        Даты проекта: от {{ formatDate(project.project.dateStart) }} до
        {{ formatDate(project.project.dateEnd) }}
      </p>
      {{ project.project.links }}
    </v-banner>

    <v-banner elevation="0" class="mb-4 my-print">
      <h4 class="mb-1">
        {{ project.project.name }}. Команда: {{ project.name }}
      </h4>
      {{ project.project.description }}
      <p class="subtitle-1">
        Даты проекта: от {{ formatDate(project.project.dateStart) }} до
        {{ formatDate(project.project.dateEnd) }}
      </p>
      {{ project.project.links }}
    </v-banner>
  </div>
</template>
<script>
export default {
  name: "Project",
  props: ["project"],
  methods: {
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    }
  }
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
