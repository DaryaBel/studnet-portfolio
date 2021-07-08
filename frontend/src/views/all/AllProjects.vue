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
              <v-btn
                :disabled="!addBtn"
                color="light-blue"
                class="white--text"
                @click="onAdd()"
              >
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
              >{{ formatDate(project.dateStart) }} -
              {{ formatDate(project.dateEnd) }}</span
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
            <v-btn
              color="red"
              class="white--text"
              @click="onDelete(project.id)"
            >
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
import {
  PROJECTS,
  CREATEPROJECT,
  UPDATEPROJECT,
  DELETEPROJECT
} from "@/graphql/queries.js";

export default {
  name: "AllProjects",
  apollo: {
    allProjects: {
      query: PROJECTS
    }
  },
  data() {
    return {
      flag: 0,
      fullName: "",
      fullDescription: "",
      fullLinks: "",

      findString: "",
      formName: "",
      formDescription: "",
      formLinks: "",

      date1: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
      date3: new Date().toISOString().substr(0, 10),
      date4: new Date().toISOString().substr(0, 10),

      menu1: false,
      menu2: false,
      menu3: false,
      menu4: false
    };
  },
  methods: {
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    },
    // Исправлено: добавление
    onAdd() {
      this.$apollo
        .mutate({
          mutation: CREATEPROJECT,
          variables: {
            name: this.fullName,
            dateStart: this.date1,
            description: this.fullDescription,
            links: this.fullLinks,
            dateEnd: this.date2
          }
        })
        .then(() => {
          this.$apollo.queries.allProjects.refresh();
          this.$apollo.queries.allProjects.refetch();
          this.fullLinks = "";
          this.fullDescription = "";
          this.date1 = new Date().toISOString().substr(0, 10);
          this.date2 = new Date().toISOString().substr(0, 10);

          this.fullName = "";
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Исправлено: удаление
    onDelete(id) {
      this.flag = 0;
      this.$apollo
        .mutate({
          mutation: DELETEPROJECT,
          variables: {
            projectId: id
          }
        })
        .then(() => {
          this.$apollo.queries.allProjects.refresh();
          this.$apollo.queries.allProjects.refetch();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Исправлено: обновление
    onEdit(project) {
      if (this.flag == 0) {
        this.flag = project.id;
        this.formDescription = project.description;
        this.formLinks = project.links;
        this.date3 = new Date(project.dateStart).toISOString().substr(0, 10);
        this.date4 = new Date(project.dateEnd).toISOString().substr(0, 10);
        this.formName = project.name;
      } else {
        this.flag = 0;
        this.$apollo
          .mutate({
            mutation: UPDATEPROJECT,
            variables: {
              dateEnd: this.date4,
              dateStart: this.date3,
              description: this.formDescription,
              links: this.formLinks,
              name: this.formName,
              projectId: project.id
            }
          })
          .then(() => {
            this.$apollo.queries.allProjects.refresh();
            this.$apollo.queries.allProjects.refetch();
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  },
  computed: {
    addBtn() {
      if (this.fullName != "" && this.fullName != "" && this.fullLinks != "")
        return true;
      else return false;
    },
    filterItems() {
      if (this.allProjects != null || this.allProjects != undefined) {
        if (this.findString !== "") {
          return this.allProjects.filter(el => {
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
          return this.allProjects;
        }
      } else return [];
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
