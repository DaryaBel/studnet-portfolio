<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Дашборд</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h4 class="text-center">Количество участий в мероприятиях студентом</h4>
        <Chart
          v-if="!loaded"
          :chart-data="eventDataToChart"
          :options="options"
          :height="200"
        ></Chart>
      </v-col>

      <v-col>
        <h4 class="text-center">
          Количество участий в командах проектов студентом
        </h4>
        <Chart
          v-if="!loaded"
          :chart-data="teamDataToChart"
          :options="options"
          :height="200"
        ></Chart>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Chart from "@/components/Chart.vue";
import { STATISTICS } from "@/graphql/queries.js";

export default {
  name: "Dashboard",
  data: () => ({
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),
  components: {
    Chart
  },
  apollo: {
    statistics: {
      query: STATISTICS
    }
  },
  computed: {
    loaded() {
      if (!this.$apollo.queries.statistics.loading && this.statistics != null)
        return false;
      else return true;
    },
    eventDataToChart() {
      let dataCollection = {
        labels: [],
        datasets: [
          {
            label: "Dataset",
            backgroundColor: [
              "#AB47BC",
              "#9575CD",
              "#7986CB",
              "#64B5F6",
              "#03A9F4",
              "#4DD0E1",
              "#4DB6AC",
              "#00897B",
              "#00ACC1",
              "#039BE5",
              "#1976D2",
              "#303F9F",
              "#512DA8"
            ],
            data: []
          }
        ]
      };
      if (!this.loaded) {
        for (let index = 0; index < this.statistics.students.length; index++) {
          const student = this.statistics.students[index];
          dataCollection.labels.push(student.fullname);
          dataCollection.datasets[0].data.push(student.eventsCount);
        }
      }
      return dataCollection;
    },
    teamDataToChart() {
      let dataCollection = {
        labels: [],
        datasets: [
          {
            label: "Dataset",
            backgroundColor: [
              "#AB47BC",
              "#9575CD",
              "#7986CB",
              "#64B5F6",
              "#03A9F4",
              "#4DD0E1",
              "#4DB6AC",
              "#00897B",
              "#00ACC1",
              "#039BE5",
              "#1976D2",
              "#303F9F",
              "#512DA8"
            ],
            data: []
          }
        ]
      };
      if (!this.loaded) {
        for (let index = 0; index < this.statistics.students.length; index++) {
          const student = this.statistics.students[index];
          dataCollection.labels.push(student.fullname);
          dataCollection.datasets[0].data.push(student.teamsCount);
        }
      }
      return dataCollection;
    }
  }
};
</script>
<style lang="scss" scoped>
@media (max-width: 365px) {
  div.container.my-container {
    padding: 8px !important;
  }
}
</style>
