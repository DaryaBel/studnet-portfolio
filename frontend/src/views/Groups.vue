<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Выберите группу:</h2>
      </v-col>
    </v-row>
    <v-row v-if="!(chip1 && chip2 && chip3)">
      <v-col>
        <span>Выберите фильтры: </span>
        <span
          v-if="!chip1"
          @click="chip1 = true"
          class="ma-2 light-blue--text pointer"
          >Бакалавриат</span
        >
        <span
          v-if="!chip2"
          @click="chip2 = true"
          class="ma-2 light-blue--text pointer"
          >Магистратура</span
        >
        <span
          v-if="!chip3"
          @click="chip3 = true"
          class="ma-2 light-blue--text pointer"
          >Аспирантура</span
        >
      </v-col>
    </v-row>
    <v-row v-if="chip1 || chip2 || chip3">
      <v-col>
        <span>Используются следующие фильтры: </span>
        <v-chip
          v-if="chip1"
          class="ma-2"
          close
          color="light-blue"
          outlined
          @click:close="chip1 = false"
        >
          Бакалавриат
        </v-chip>
        <v-chip
          v-if="chip2"
          class="ma-2"
          close
          color="light-blue"
          outlined
          @click:close="chip2 = false"
        >
          Магистратура
        </v-chip>
        <v-chip
          v-if="chip3"
          class="ma-2"
          close
          color="light-blue"
          outlined
          @click:close="chip3 = false"
        >
          Аспирантура
        </v-chip>
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
          v-for="group in filterItems"
          :key="group.id"
          elevation="2"
        >
          <v-card-title class="mb-2">{{ group.codeName }}</v-card-title>
          <v-card-subtitle> <v-chip color="light-blue" text-color="white" class="mr-1">{{ group.studyDegree }}</v-chip> {{group.course}} курс. {{ group.formEducation }} форма обучения</v-card-subtitle>
          
          <v-card-actions>
            <v-btn text color="light-blue" @click="onLink(group.id)"> Выбрать </v-btn>
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
  name: "Groups",
  data() {
    return {
      chip1: true,
      chip2: true,
      chip3: true,
      findString: "",
      groups: [
        {
          id: 1,
          course: 3,
          codeName: "181-321",
          formEducation: "Очная",
          studyDegree: "Бакалавриат",
          specialization: 1
        },
        {
          id: 2,
          course: 3,
          codeName: "181-322",
          formEducation: "Очная",
          studyDegree: "Бакалавриат",
          specialization: 1
        },
        {
          id: 3,
          course: 1,
          codeName: "202-321",
          formEducation: "Заочная",
          studyDegree: "Магистратура",
          specialization: 1
        }
      ]
    };
  },
methods: {
    onLink(id) {
      this.$router.push({ name: "Students", params: { id: id } });
    }
  },
  computed: {
    filterItems() {
      let array = [];
      let bachelor = this.groups.filter(el => {
        return (
          el.studyDegree.toLowerCase().split(" ").join("") == "бакалавриат"
        );
      });
      let master = this.groups.filter(el => {
        return (
          el.studyDegree.toLowerCase().split(" ").join("") == "магистратура"
        );
      });
      let phd = this.groups.filter(el => {
        return (
          el.studyDegree.toLowerCase().split(" ").join("") == "аспирантура"
        );
      });
      if (this.chip1) array = array.concat(bachelor);
      if (this.chip2) array = array.concat(master);
      if (this.chip3) array = array.concat(phd);
      return array;
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
.pointer {
  cursor: pointer;
}
</style>
