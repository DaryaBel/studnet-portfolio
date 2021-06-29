<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Выберите университет:</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по полному или краткому названию университета"
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
          v-for="university in filterItems"
          :key="university.id"
          elevation="2"
        >
          <v-card-title>{{ university.fullname }}</v-card-title>
          <v-card-subtitle>{{ university.location }}</v-card-subtitle>
          <v-card-text>{{ university.description }}</v-card-text>
          <v-card-actions>
            <v-btn text color="light-blue" @click="onLink(university)">
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
import { UNIVERSITIES } from "@/graphql/queries.js";
export default {
  name: "Universities",
  apollo: {
    allUniversities: {
      query: UNIVERSITIES
    }
  },
  data() {
    return {
      findString: ""
    };
  },
  components: {},
  computed: {
    filterItems() {
      if (this.allUniversities != null || this.allUniversities != undefined) {
        if (this.findString !== "") {
          return this.allUniversities.filter(el => {
            return (
              (el.fullname
                .toLowerCase()
                .split(" ")
                .join("")
                .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
                -1 &&
                el.fullname !== "") ||
              (el.shortname
                .toLowerCase()
                .split(" ")
                .join("")
                .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
                -1 &&
                el.shortname !== "")
            );
          });
        } else {
          return this.allUniversities;
        }
      } else return [];
    }
  },
  methods: {
    onLink(university) {
      this.$router.push({ name: "Faculties", params: { id: university.id } });
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
