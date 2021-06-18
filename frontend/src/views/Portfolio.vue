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
        <v-radio-group v-if="user" v-model="radios1" mandatory>
          <h4 class="light-blue--text mb-2">Проект:</h4>
          <v-radio
            color="light-blue"
            label="Присоединиться к существующему"
            value="radio-1"
            @click="clearProject()"
          ></v-radio>
          <v-radio
            @click="clearProject()"
            color="light-blue"
            label="Добавить новый"
            value="radio-2"
          ></v-radio>
        </v-radio-group>
        <v-text-field
          v-if="user && radios1 == 'radio-2'"
          v-model.trim="$v.form2.project.$model"
          class="mb-3"
          color="light-blue"
          label="Название проекта"
          required
        ></v-text-field>
        <v-select
          v-if="user && radios1 == 'radio-1'"
          class="mb-3"
          :items="allProjects"
          label="Проект"
          dense
          required
          v-model.trim="$v.form2.project.$model"
          color="light-blue"
        ></v-select>
        <v-radio-group
          v-if="user && radios1 == 'radio-1'"
          v-model="radios2"
          mandatory
        >
          <h4 class="light-blue--text mb-2">Команда:</h4>
          <v-radio
            @click="clearTeam()"
            color="light-blue"
            label="Присоединиться к существующей"
            value="radio-3"
          ></v-radio>
          <v-radio
            @click="clearTeam()"
            color="light-blue"
            label="Добавить новую"
            value="radio-4"
          ></v-radio>
        </v-radio-group>
        <v-select
          v-if="user && radios1 == 'radio-1' && radios2 == 'radio-3'"
          :items="allTeams"
          label="Команда"
          dense
          required
          v-model.trim="$v.form2.team.$model"
          color="light-blue"
        ></v-select>
        <v-text-field
          v-if="
            (user && radios1 == 'radio-1' && radios2 == 'radio-4') ||
            (user && radios1 == 'radio-2')
          "
          @input="myFunc()"
          v-model.trim="$v.form2.team.$model"
          class="mb-3"
          color="light-blue"
          label="Название команды"
          required
        ></v-text-field>
        <v-btn
          v-if="user"
          class="mb-5 white--text"
          color="light-blue"
          @click="onAddYouInProject()"
          block="block"
          :dark="!$v.form2.$invalid"
          :disabled="$v.form2.$invalid"
        >
          Добавить участие в проекте
        </v-btn>
        <div v-if="projects.length != 0">
          <Project
            v-for="project in projects"
            :key="project.id"
            v-bind:project="project"
          ></Project>
        </div>
        <div v-if="projects.length == 0">
          <span>Не найдено</span>
        </div>
      </v-col>
      <v-col>
        <h3 class="mb-6">Участие в мероприятиях</h3>
        <v-select
          v-if="user"
          class="mb-3"
          :items="allEvents"
          label="Мероприятие"
          dense
          required
          v-model.trim="$v.form.event.$model"
          color="light-blue"
        ></v-select>
        <v-select
          v-if="user"
          class="mb-3"
          :items="roles"
          label="Ваша роль"
          dense
          required
          color="light-blue"
          v-model.trim="$v.form.role.$model"
        ></v-select>
        <v-btn
          v-if="user"
          class="mb-5 white--text"
          color="light-blue"
          @click="onAddYouInEvent()"
          block="block"
          :dark="!$v.form.$invalid"
          :disabled="$v.form.$invalid"
        >
          Добавить участие в мероприятии
        </v-btn>
        <div v-if="events.length != 0">
          <Event
            v-for="event in events"
            :key="event.id"
            v-bind:event="event"
          ></Event>
        </div>
        <div v-if="events.length == 0">
          <span>Не найдено</span>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { required } from "vuelidate/lib/validators";
import Event from "@/components/Event.vue";
import Project from "@/components/Project.vue";
export default {
  name: "Portfolio",
  components: {
    Event,
    Project
  },
  validations: {
    form: {
      role: {
        required
      },
      event: {
        required
      }
    },
    form2: {
      project: {
        required
      },
      team: {
        required
      }
    }
  },
  data() {
    return {
      form: {
        role: "",
        event: ""
      },
      form2: {
        project: "",
        team: ""
      },
      radios1: "radio-1",
      radios2: "radio-3",
      user: false,
      operator: false,
      admin: false,
      roles: ["Участник", "Волонтер", "Призер", "Победитель"],
      allEvents: [
        "Хакатон 2021",
        "Международный форум молодых ученых «РОЛЬ МОЛОДЫХ УЧЕНЫХ В РАЗВИТИИ НАУКИ, ТЕХНИКИ И ИННОВАЦИЙ» посвященный дню независимости Республики Казахстан",
        "III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ»"
      ],
      allProjects: ["Проект 1", "Проект 2", "Проект 3"],
      allTeams: ["Команда 1", "Команда 2", "Команда 3"],

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
          description: "Студенческая веб-студия",
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
          description: "Студенческая веб-студия",
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
          description: "Студенческая веб-студия",
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
          participant: 2
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
        }
      ].filter(el => {
        return el.participant == this.$route.params.id;
      })
    };
  },
  mounted() {
    if (localStorage.getItem("user")) this.user = true;
    else this.user = false;

    if (localStorage.getItem("operator")) this.operator = true;
    else this.operator = false;

    if (localStorage.getItem("admin")) this.admin = true;
    else this.admin = false;
  },
  methods: {
    myFunc() {
      console.log(this.$v.form2);
    },
    clearProject() {
      this.$v.form2.project.$model = "";
    },
    clearTeam() {
      this.$v.form2.team.$model = "";
    },
    onAddYouInEvent() {
      let obj = {
        id: 5,
        name: this.$v.form.event.$model,
        location: "",
        description: "",
        date: `${new Date("2020-11-20").getDate()}.${
          new Date("2020-11-20").getMonth() + 1
        }.${new Date("2020-11-20").getFullYear()}
         `,
        role: this.$v.form.role.$model,
        student: this.$route.params.id
      };

      this.events.push(obj);
      this.$v.form.event.$model = "";
      this.$v.form.role.$model = "";
    },
    onAddYouInProject() {
      let obj = {
        id: 5,
        name: this.$v.form2.project.$model,
        description: "",
        dateStart: `${new Date("2019-02-18").getDate()}.${
          new Date("2019-02-18").getMonth() + 1
        }.${new Date("2019-02-18").getFullYear()}
         `,
        dateEnd: `${new Date("2022-06-30").getDate()}.${
          new Date("2022-06-30").getMonth() + 1
        }.${new Date("2022-06-30").getFullYear()}
         `,
        links: "",
        team: this.$v.form2.team.$model,
        participant: this.$route.params.id
      };

      this.projects.push(obj);
      this.$v.form2.project.$model = "";
      this.$v.form2.team.$model = "";
      this.radios1 = "radio-1";
      this.radios2 = "radio-3";
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
