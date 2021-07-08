<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Все команды</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по названию команды"
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
              >Добавить команду
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-text-field
                light="light"
                label="Название"
                color="light-blue"
                v-model="fullName"
              ></v-text-field>
              <v-select
                :items="allProjects"
                item-text="name"
                item-value="id"
                label="Проект"
                dense
                required
                v-model="fullProject"
                color="light-blue"
              ></v-select>
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
          v-for="team in filterItems"
          :key="team.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != team.id">{{ team.name }}</span>
            <v-text-field
              v-if="flag == team.id"
              light="light"
              label="Название"
              color="light-blue"
              v-model="formName"
            ></v-text-field>
          </v-card-title>
          <v-card-subtitle>
            <span class="light-blue--text" v-if="flag != team.id">
              Проект:
              {{ team.project.name }}</span
            >
            <v-select
              v-if="flag == team.id"
              :items="allProjects"
              item-text="name"
              item-value="id"
              label="Проект"
              dense
              required
              v-model="formProject"
              color="light-blue"
            ></v-select>
          </v-card-subtitle>
          <v-card-actions>
            <v-btn
              v-if="flag != team.id"
              :disabled="flag != 0"
              text
              color="light-blue"
              @click="onEdit(team)"
            >
              Редактировать
            </v-btn>
            <v-btn
              v-if="flag == team.id"
              text
              color="light-blue"
              @click="onEdit(team)"
            >
              Сохранить
            </v-btn>
            <v-btn color="red" class="white--text" @click="onDelete(team.id)">
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
  TEAMS,
  SHORTPROJECTS,
  CREATETEAM,
  UPDATETEAM,
  DELETETEAM
} from "@/graphql/queries.js";

export default {
  name: "AllTeams",
  apollo: {
    allTeams: {
      query: TEAMS
    },
    allProjects: {
      query: SHORTPROJECTS
    }
  },
  data() {
    return {
      flag: 0,
      fullName: "",
      fullProject: "",

      findString: "",
      formName: "",
      formProject: ""
    };
  },
  methods: {
    // Исправлено: добавление
    onAdd() {
      this.$apollo
        .mutate({
          mutation: CREATETEAM,
          variables: {
            name: this.fullName,
            project: this.fullProject
          }
        })
        .then(() => {
          this.$apollo.queries.allTeams.refresh();
          this.$apollo.queries.allTeams.refetch();
          this.fullCodename = "";
          this.fullProject = "";
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
          mutation: DELETETEAM,
          variables: {
            teamId: id
          }
        })
        .then(() => {
          this.$apollo.queries.allTeams.refresh();
          this.$apollo.queries.allTeams.refetch();
        })
        .catch(error => {
          console.error(error);
        });
    },

    // Исправлено: обновление
    onEdit(team) {
      if (this.flag == 0) {
        this.flag = team.id;
        this.formProject = team.project;
        this.formName = team.name;
      } else {
        this.flag = 0;
        let project;
        if (this.formProject.id == undefined) {
          project = this.formProject;
        } else project = this.formProject.id;
        this.$apollo
          .mutate({
            mutation: UPDATETEAM,
            variables: {
              teamId: team.id,
              name: this.formName,
              project: project
            }
          })
          .then(() => {
            this.$apollo.queries.allTeams.refresh();
            this.$apollo.queries.allTeams.refetch();
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  },
  computed: {
    addBtn() {
      if (this.fullName != "" && this.fullProject != "") return true;
      else return false;
    },
    filterItems() {
      if (this.allTeams != null || this.allTeams != undefined) {
        if (this.findString !== "") {
          return this.allTeams.filter(el => {
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
          return this.allTeams;
        }
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
