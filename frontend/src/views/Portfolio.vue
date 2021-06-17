<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Портфолио студента</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="mb-2 pb-3" elevation="2">
          <v-card-title>{{ student.fullname }}</v-card-title>
          <v-card-subtitle class="pb-0">{{
            student.birthdate
          }}</v-card-subtitle>
          <p class="ma-4 mt-0 mb-2 light-blue--text text--darken-3">
            E-mail: {{ student.email }}
          </p>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <h3 class="mb-3">Участие в проектах</h3>
        <div v-if="projects.length!=0"> 
        <Project v-for="project in projects"
          :key="project.id" v-bind:project="project"></Project>
        </div>
        <div v-if="projects.length==0">
          <span>Не найдено</span>
        </div>
      </v-col>
      <v-col>
        <h3 class="mb-3">Участие в мероприятиях</h3>
        <div v-if="events.length!=0"> 
        <Event v-for="event in events"
          :key="event.id" v-bind:event="event"></Event>
        </div>
        <div v-if="events.length==0">
          <span>Не найдено</span>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Event from "@/components/Event.vue";
import Project from "@/components/Project.vue";
export default {
  name: "Portfolio",
  components: {
    Event, Project
  },
  data() {
    return {
      student: [
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
      ].find(el => {
        return el.id == this.$route.params.id;
      }),
      events: [
        {
          id: 1,
          name: "Международный форум молодых ученых «РОЛЬ МОЛОДЫХ УЧЕНЫХ В РАЗВИТИИ НАУКИ, ТЕХНИКИ И ИННОВАЦИЙ» посвященный дню независимости Республики Казахстан",
          location: "Online. Платформа Zoom",
          description:
            "7-8 декабря 2020 года в рамках Международного форума молодых ученых «Роль молодых ученых в развитии науки, техники и инноваций» посвященного дню независимости Республики Казахстан проводился международный конкурс научно практических и научно исследовательских проектов.",
          date: `${new Date("2020-12-07").getDate()}.${
            new Date("2020-12-07").getMonth() + 1
          }.${new Date("2020-12-07").getFullYear()}
         `,
          role: "Победитель",
          student: 1
        },
        {
          id: 2,
          name: "III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ»",
          location: "Online. Платформа Zoom",
          description:
            "20 ноября завершился III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ», включивший в себя 12 конференций и научно-методических семинаров, круглых столов и экспертных сессий",
          date: `${new Date("2020-11-20").getDate()}.${
            new Date("2020-11-20").getMonth() + 1
          }.${new Date("2020-11-20").getFullYear()}
         `,
          role: "Призер",
          student: 1
        },
        {
          id: 3,
          name: "Международный форум молодых ученых «РОЛЬ МОЛОДЫХ УЧЕНЫХ В РАЗВИТИИ НАУКИ, ТЕХНИКИ И ИННОВАЦИЙ» посвященный дню независимости Республики Казахстан",
          location: "Online. Платформа Zoom",
          description:
            "7-8 декабря 2020 года в рамках Международного форума молодых ученых «Роль молодых ученых в развитии науки, техники и инноваций» посвященного дню независимости Республики Казахстан проводился международный конкурс научно практических и научно исследовательских проектов.",
          date: `${new Date("2020-12-07").getDate()}.${
            new Date("2020-12-07").getMonth() + 1
          }.${new Date("2020-12-07").getFullYear()}
         `,
          role: "Участник",
          student: 2
        },
        {
          id: 4,
          name: "III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ»",
          location: "Online. Платформа Zoom",
          description:
            "20 ноября завершился III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ», включивший в себя 12 конференций и научно-методических семинаров, круглых столов и экспертных сессий",
          date: `${new Date("2020-11-20").getDate()}.${
            new Date("2020-11-20").getMonth() + 1
          }.${new Date("2020-11-20").getFullYear()}
         `,
          role: "Победитель",
          student: 2
        }
      ].filter(el => {
        return el.student == this.$route.params.id;
      }),
      projects: [
        {
          id: 1,
          name: "Поливеб",
          description:
            "Студенческая веб-студия",
          dateStart: `${new Date("2019-02-18").getDate()}.${
            new Date("2019-02-18").getMonth() + 1
          }.${new Date("2019-02-18").getFullYear()}
         `,
         dateEnd: `${new Date("2022-06-30").getDate()}.${
            new Date("2022-06-30").getMonth() + 1
          }.${new Date("2022-06-30").getFullYear()}
         `,
          links: "Сайт: polyweb.agency",
          team: "Главный сайт",
          participant: 1
        },
        {
          id: 2,
          name: "Поливеб",
          description:
            "Студенческая веб-студия",
          dateStart: `${new Date("2019-02-18").getDate()}.${
            new Date("2019-02-18").getMonth() + 1
          }.${new Date("2019-02-18").getFullYear()}
         `,
         dateEnd: `${new Date("2022-06-30").getDate()}.${
            new Date("2022-06-30").getMonth() + 1
          }.${new Date("2022-06-30").getFullYear()}
         `,
          links: "Сайт: polyweb.agency",
          team: "Игра по интернет-маркетингу",
          participant: 2
        },
        {
          id: 3,
          name: "Поливеб",
          description:
            "Студенческая веб-студия",
          dateStart: `${new Date("2019-02-18").getDate()}.${
            new Date("2019-02-18").getMonth() + 1
          }.${new Date("2019-02-18").getFullYear()}
         `,
         dateEnd: `${new Date("2022-06-30").getDate()}.${
            new Date("2022-06-30").getMonth() + 1
          }.${new Date("2022-06-30").getFullYear()}
         `,
          links: "Сайт: polyweb.agency",
          team: "Главный сайт",
          participant: 2,
        },
        {
          id: 4,
          name: "Catcherry",
          description:
            "Цель проекта -  разработать систему оценки продуктивности сотрудников и анализа данных о рабочих процессах, а также алгоритмов аналитических предсказаний и рекомендаций  с использованием механик геймификации для повышения производительности труда конкретных работников и команд различного размера в целом.",
          dateStart: `${new Date("2020-09-01").getDate()}.${
            new Date("2020-09-01").getMonth() + 1
          }.${new Date("2020-09-01").getFullYear()}
         `,
         dateEnd: `${new Date("2021-01-03").getDate()}.${
            new Date("2021-01-03").getMonth() + 1
          }.${new Date("2021-01-03").getFullYear()}
         `,
          links: "Репозиторий: https://github.com/Glazkoff/catcherry;",
          team: "Команда 1",
          participant: 1
        },
      ].filter(el => {
        return el.participant == this.$route.params.id;
      }),
    };
  },
  methods: {
    // onLink(id) {
    //   this.$router.push({ name: "Groups", params: { id: id } });
    // }
  },
  computed: {}
};
</script>

<style lang="scss" scoped>
@media (max-width: 365px) {
  div.container.my-container {
    padding: 8px !important;
  }
}
</style>
