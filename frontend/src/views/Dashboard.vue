<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Дашборд</h2>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "LineChartContainer",
  data: () => ({
    loaded: false,
    chartdata: {
      labels: ["dfjkdfl", "fdfjkdhkj"],
      data: [15, 87]
    }
  })
};
</script>
<style lang="scss" scoped>
@media (max-width: 365px) {
  div.container.my-container {
    padding: 8px !important;
  }
}
</style>
