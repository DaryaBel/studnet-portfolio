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
          Найдено {{ filterItems.length }}
          <span
            v-if="
              filterItems.length % 10 == 1 && filterItems.length % 100 != 11
            "
            >строка</span
          >
          <span
            v-if="
              filterItems.length % 10 >= 2 &&
              filterItems.length % 10 <= 4 &&
              filterItems.length % 100 != 12 &&
              filterItems.length % 100 != 13 &&
              filterItems.length % 100 != 14
            "
            >строки</span
          >
          <span
            v-if="
              filterItems.length % 10 >= 5 &&
              filterItems.length % 10 <= 9 &&
              filterItems.length % 10 == 0 &&
              filterItems.length % 100 >= 10 &&
              filterItems.length % 100 <= 20
            "
            >строк</span
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
export default {
  name: "Students",
  data() {
    return {
      findString: "",
      students: [
        {
          id: 1,
          fullname: "Беляева Дарья Владиславовна",
          birthdate: `${new Date("2000-11-24").getDate()}.${
            new Date("2000-11-24").getMonth() + 1
          }.${new Date("2000-11-24").getFullYear()}
         `,
          group: 1,
          email: "d.belyaeva1@gmail.com",
          budgetary: true
        },
        {
          id: 2,
          fullname: "Глазков Никита Олегович",
          birthdate: `${new Date("2000-10-31").getDate()}.${
            new Date("2000-10-31").getMonth() + 1
          }.${new Date("2000-10-31").getFullYear()}
         `,
          group: 1,
          email: "zitrnik@gmail.com",
          budgetary: true
        },
        {
          id: 3,
          fullname: "Колезнева Надежда Валентиновна",
          birthdate: `${new Date("2000-09-20").getDate()}.${
            new Date("2000-09-20").getMonth() + 1
          }.${new Date("2000-09-20").getFullYear()}
         `,
          group: 2,
          email: "nkolezneva@gmail.com",
          budgetary: false
        }
      ]
    };
  },
  methods: {
    onLink(id) {
      this.$router.push({ name: "Portfolio", params: { id: id } });
    }
  },
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.students.filter(el => {
          return (
            el.fullname
              .toLowerCase()
              .split(" ")
              .join("")
              .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
              -1 &&
            el.fullname !== "" &&
            el.group == this.$route.params.id
          );
        });
      } else {
        return this.students.filter(el => {
          return el.group == this.$route.params.id;
        });
      }
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
