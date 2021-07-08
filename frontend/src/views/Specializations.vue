<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Выберите специальность:</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по названию или коду специальности"
          append-icon="mdi-magnify"
          v-model="findString"
        ></v-text-field>
        <p v-if="filterItems.length != 0">
          <span
            v-if="
              filterItems.length % 10 == 1 && filterItems.length % 100 != 11
            "
            >Найдена {{ filterItems.length }} строка</span
          >
          <span
            v-if="
              filterItems.length % 10 >= 2 &&
              filterItems.length % 10 <= 4 &&
              filterItems.length % 100 != 12 &&
              filterItems.length % 100 != 13 &&
              filterItems.length % 100 != 14
            "
            >Найдено {{ filterItems.length }} строки</span
          >
          <span
            v-if="
              (filterItems.length % 10 >= 5 && filterItems.length % 10 <= 9) ||
              (filterItems.length % 100 >= 10 &&
                filterItems.length % 100 <= 20) ||
              filterItems.length % 10 == 0
            "
            >Найдено {{ filterItems.length }} строк</span
          >
          с результатами
        </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-if="filterItems.length != 0">
        <v-card
          class="mb-5"
          v-for="specialization in filterItems"
          :key="specialization.id"
          elevation="2"
        >
          <v-card-title>{{ specialization.name }}</v-card-title>
          <v-card-subtitle>{{ specialization.codeName }}</v-card-subtitle>
          <v-card-actions>
            <v-btn text color="light-blue" @click="onLink(specialization.id)">
              Выбрать
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col v-if="filterItems.length == 0">
        <p class="text-center title">Не найдено</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { SPECIALIZATIONSOFFACULTY } from "@/graphql/queries.js";
export default {
  name: "Specializations",
  apollo: {
    faculty: {
      query: SPECIALIZATIONSOFFACULTY,
      variables() {
        return {
          facultyId: this.$route.params.id
        };
      }
    }
  },
  data() {
    return {
      findString: ""
    };
  },
  methods: {
    onLink(id) {
      this.$router.push({ name: "Groups", params: { id: id } });
    }
  },
  computed: {
    filterItems() {
      if (this.faculty != null || this.faculty != undefined) {
        let specializations = this.faculty.specializationsOfFaculty;
        if (this.findString !== "") {
          return specializations.filter(el => {
            return (
              (el.name
                .toLowerCase()
                .split(" ")
                .join("")
                .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
                -1 &&
                el.name !== "") ||
              (el.codeName
                .toLowerCase()
                .split(" ")
                .join("")
                .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
                -1 &&
                el.codeName !== "")
            );
          });
        } else return specializations;
      } else return [];
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
