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
            <v-btn text color="light-blue" @click="onLink(specialization.id)"> Выбрать </v-btn>
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
  name: "Specializations",
  data() {
    return {
      findString: "",
      specializations: [
        {
          id: 1,
          name: "Информатика и вычислительная техника",
          codeName: "09.03.01",
          faculty: 1
        },
        {
          id: 2,
          name: "Прикладная математика и информатика",
          codeName: "01.03.02",
          faculty: 1
        },
        {
          id: 3,
          name: "Информационная безопасность автоматизированных систем",
          codeName: "10.05.03",
          faculty: 1
        }
      ]
    };
  },
  methods: {
    onLink(id) {
      this.$router.push({ name: "Groups", params: { id: id } });
    }
  },
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.specializations.filter(el => {
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
              el.codeName !== "" &&
              el.faculty == this.$route.params.id)
          );
        });
      } else {
        return this.specializations.filter(el => {
          return el.faculty == this.$route.params.id;
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
