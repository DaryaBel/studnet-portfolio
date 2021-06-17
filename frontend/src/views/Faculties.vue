<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Выберите факультет:</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по названию факультета"
          append-icon="mdi-magnify"
          v-model="findString"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-if="filterItems.length != 0">
        <v-card
          class="mb-5"
          v-for="faculty in filterItems"
          :key="faculty.id"
          elevation="2"
        >
          <v-card-title>{{ faculty.name }}</v-card-title>
          <v-card-text>{{ faculty.description }}</v-card-text>
          <v-card-actions>
            <v-btn text color="light-blue" @click="onLink(faculty.id)">
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
export default {
  name: "Faculties",
  data() {
    return {
      findString: "",
      faculties: [
        {
          id: 1,
          name: "Факультет информационных технологий",
          description:
            "Образовательные программы созданы совместно с профессионалами из Ассоциации Интернет Разработчиков, 1С, Autodesk, Mail.ru, Лаборатории Касперского, Яндекса и других ведущих ИТ-компаний, поэтому студенты получают самые актуальные знания и легко находят работу уже во время учебы на старших курсах. Мы оперативно реагируем на изменения ИТ-рынка и каждый год вносим изменения в учебные планы, а 30% наших преподавателей – руководители и сотрудники ведущих IT-компаний.",
          university: 1
        },
        {
          id: 2,
          name: "Транспортный факультет",
          description:
            "Основой образовательного процесса является дисциплина «Проектная деятельность». Во время обучения студенты проходят несколько этапов - от новой идеи, дизайна и проектирования, до производства и дальнейшей эксплуатации. Наши студенты сами делают гоночные болиды, которые участвуют и побеждают в соревнованиях, и мотоциклы – два года подряд сделанный ребятами электробайк устанавливает рекорд скорости на фестивале «Байкальская миля». Если в 2019 году скорость составила 145 км/час, то в 2020 году мы побили собственный рекорд в два раза – 210,5 км/час.",
          university: 1
        },
        {
          id: 3,
          name: "Факультет философии",
          description: "Много думаем",
          university: 2
        }
      ]
    };
  },
  methods: {
    onLink(id) {
      this.$router.push({ name: "Specializations", params: { id: id } });
    }
  },
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.faculties.filter(el => {
          return (
            el.name
              .toLowerCase()
              .split(" ")
              .join("")
              .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
              -1 &&
            el.name !== "" &&
            el.university == this.$route.params.id
          );
        });
      } else {
        return this.faculties.filter(el => {
          return el.university == this.$route.params.id;
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
