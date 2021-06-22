<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Все проекты</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по названию проекта"
          append-icon="mdi-magnify"
          v-model="findString"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header
              >Добавить проект
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-text-field
                light="light"
                label="Название"
                color="light-blue"
                v-model="fullName"
              ></v-text-field>
              <v-menu
                v-model="menu1"
                :close-on-content-click="true"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="computedDateFormatted1"
                    label="Дата начала"
                    prepend-icon="mdi-calendar"
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="date1"
                  no-title
                  @input="menu1 = false"
                ></v-date-picker>
              </v-menu>
              <v-menu
                v-model="menu2"
                :close-on-content-click="true"
                transition="scale-transition"
                offset-y
                max-width="290px"
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="computedDateFormatted2"
                    label="Дата окончания"
                    prepend-icon="mdi-calendar"
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="date2"
                  no-title
                  @input="menu2 = false"
                ></v-date-picker>
              </v-menu>
              <v-textarea
                color="light-blue"
                light="light"
                label="Описание"
                v-model="fullDescription"
              ></v-textarea>
              <v-textarea
                color="light-blue"
                light="light"
                label="Ссылки"
                v-model="fullLinks"
              ></v-textarea>
              <v-btn color="light-blue" class="white--text" @click="onAdd()">
                Добавить
              </v-btn>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>

    <v-row>
      <v-col v-if="filterItems.length != 0">
        <v-card
          class="mb-5"
          v-for="project in filterItems"
          :key="project.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != project.id">{{ project.name }}</span>
            <v-text-field
              v-if="flag == project.id"
              light="light"
              label="Название"
              color="light-blue"
              v-model="formName"
            ></v-text-field>
          </v-card-title>
          <v-card-subtitle>
            <span v-if="flag != project.id"
              >{{ project.dateStart }} - {{ project.dateEnd }}</span
            >
            <v-menu
              v-if="flag == project.id"
              v-model="menu3"
              :close-on-content-click="true"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="computedDateFormatted3"
                  label="Дата начала"
                  prepend-icon="mdi-calendar"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="date3"
                no-title
                @input="menu3 = false"
              ></v-date-picker>
            </v-menu>
            <v-menu
              v-if="flag == project.id"
              v-model="menu4"
              :close-on-content-click="true"
              transition="scale-transition"
              offset-y
              max-width="290px"
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="computedDateFormatted4"
                  label="Дата окончания"
                  prepend-icon="mdi-calendar"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="date4"
                no-title
                @input="menu4 = false"
              ></v-date-picker>
            </v-menu>
          </v-card-subtitle>
          <v-card-text>
            <span v-if="flag != project.id">
              {{ project.description }}
            </span>
            <v-textarea
              v-if="flag == project.id"
              color="light-blue"
              light="light"
              label="Описание"
              v-model="formDescription"
            ></v-textarea>
          </v-card-text>
           <v-card-text>
            <span v-if="flag != project.id">
              {{ project.links }}
            </span>
            <v-textarea
              v-if="flag == project.id"
              color="light-blue"
              light="light"
              label="Ссылки"
              v-model="formLinks"
            ></v-textarea>
          </v-card-text>
          <v-card-actions>
            <v-btn
              v-if="flag != project.id"
              :disabled="flag != 0"
              text
              color="light-blue"
              @click="onEdit(project)"
            >
              Редактировать
            </v-btn>
            <v-btn
              v-if="flag == project.id"
              text
              color="light-blue"
              @click="onEdit(project)"
            >
              Сохранить
            </v-btn>
            <v-btn color="red" class="white--text" @click="onDelete(project.id)">
              Удалить
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
  name: "AllProjects",
  data() {
    return {
      flag: 0,
      fullName: "",
      fullDateStart: "",
      fullDescription: "",
      fullDateEnd: "",
      fullLinks: "",

      findString: "",
      formName: "",
      formDateStart: "",
      formDescription: "",
      formDateEnd: "",
      formLinks: "",

      date1: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
      date3: new Date().toISOString().substr(0, 10),
      date4: new Date().toISOString().substr(0, 10),

      menu1: false,
      menu2: false,
      menu3: false,
      menu4: false,
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
          links: "Сайт: polyweb.agency"
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
          links: "Репозиторий: https://github.com/Glazkoff/catcherry;"
        }
      ]
    };
  },
  methods: {
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },
    onAdd() {
      let obj = {
        id: 6,
        name: this.fullName,
        dateStart: this.computedDateFormatted1,
        description: this.fullDescription,
        links: this.fullLinks,
        dateEnd: this.computedDateFormatted2
      };
      this.projects.push(obj);
      this.fullLinks = "";
      this.fullDateStart = "";
      this.fullDateEnd = "";
      this.fullDescription = "";
      this.fullName = "";
    },

    onDelete(id) {
      let index = this.projects.findIndex(el => {
        return el.id == id;
      });
      this.projects.splice(index, 1);
    },
    onEdit(project) {
      if (this.flag == 0) {
        this.flag = project.id;
        this.formDescription = project.description;
        this.formLinks = project.links;
        this.formDateStart = project.dateStart;
        this.formDateEnd = project.dateEnd;
        this.formName = project.name;
      } else {
        this.flag = 0;
        let index = this.projects.findIndex(el => {
          return el.id == project.id;
        });
        this.projects[index].links = this.formLocation;
        this.projects[index].dateStart = this.computedDateFormatted3;
        this.projects[index].dateEnd = this.computedDateFormatted4;
        this.projects[index].description = this.formDescription;
        this.projects[index].name = this.formName;
      }
    }
  },
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.projects.filter(el => {
          return (
            el.name
              .toLowerCase()
              .split(" ")
              .join("")
              .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
              -1 && el.name !== ""
          );
        });
      } else {
        return this.projects;
      }
    },
    computedDateFormatted1() {
      return this.formatDate(this.date1);
    },
    computedDateFormatted2() {
      return this.formatDate(this.date2);
    },
    computedDateFormatted3() {
      return this.formatDate(this.date3);
    },
    computedDateFormatted4() {
      return this.formatDate(this.date4);
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
