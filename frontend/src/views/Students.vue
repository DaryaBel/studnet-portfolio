<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Выберите студента:</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по ФИО"
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
          v-for="student in filterItems"
          :key="student.id"
          elevation="2"
        >
          <v-card-title>{{ student.fullname }}</v-card-title>
          <v-card-subtitle class="pb-0">{{
            student.birthdate
          }}</v-card-subtitle>
          <span class="ma-4 light-blue--text text--darken-3"
            >E-mail: {{ student.email }}</span
          >
          <v-card-actions>
            <v-btn text color="light-blue" @click="onLink(student.id)">
              Посмотреть портфолио
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
import { STUDENTSOFGROUP } from "@/graphql/queries.js";
export default {
  name: "Students",
  apollo: {
    group: {
      query: STUDENTSOFGROUP,
      variables() {
        return {
          groupId: this.$route.params.id
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
      this.$router.push({ name: "Portfolio", params: { id: id } });
    }
  },
  computed: {
    filterItems() {
      if (this.group != null || this.group != undefined) {
        let students = this.group.studentsOfGroup;
        if (this.findString !== "") {
          return students.filter(el => {
            return (
              el.fullname
                .toLowerCase()
                .split(" ")
                .join("")
                .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
                -1 && el.fullname !== ""
            );
          });
        } else return students;
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
