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
                :items="arrayProject()"
                label="Проект"
                dense
                required
                v-model="fullProject"
                color="light-blue"
              ></v-select>
              <v-select
                v-model="fullStudents"
                :items="arrayStudents()"
                :menu-props="{ maxHeight: '400' }"
                label="Студенты"
                multiple
                color="light-blue"
                required
              ></v-select>
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
              {{ findProject(team.project) }}</span
            >
            <v-select
              v-if="flag == team.id"
              :items="arrayProject()"
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
export default {
  name: "AllTeams",
  data() {
    return {
      flag: 0,
      fullName: "",
      fullProject: "",
      fullStudents: "",
      // студенты!

      findString: "",
      formName: "",
      formProject: "",
      allProjects: [
        { id: 1, name: "Проект 1" },
        { id: 2, name: "Проект 2" },
        { id: 3, name: "Проект 3" }
      ],
      allStudents: [
        { id: 1, fullname: "Иванова Екатерина Петровна" },
        { id: 2, fullname: "Емельянов Тихон Ярославович" },
        { id: 3, fullname: "Терентьев Эрик Михаилович" },
        { id: 4, fullname: "Лихачёва Злата Михаиловна" },
        { id: 5, fullname: "Попова Малика Авксентьевна" },
        { id: 6, fullname: "Васильева Нонна Ивановна" },
        { id: 7, fullname: "Кузнецова Наталья Геннадьевна" },
        { id: 8, fullname: "Фомичёва Эдита Мэлоровна" },
        { id: 9, fullname: "Рыбакова Кармелитта Михайловна" }
      ],
      teams: [
        { id: 1, name: "Команда 1", project: 1 },
        { id: 2, name: "Команда 2", project: 1 },
        { id: 3, name: "Команда 3", project: 1 }
      ]
    };
  },
  methods: {
    onAdd() {
      let obj = {
        id: 6,
        name: this.fullName,
        project: this.findProjectByName(this.fullProject)
      };
      this.fullStudents.forEach(el => {
        let obj2 = {
          id: 10,
          student: this.findStudentByName(el),
          team: 6
        };
        console.log(obj2);
      });
      this.teams.push(obj);
      this.fullStudents = "";
      this.fullProject = "";
      this.fullName = "";
    },

    onDelete(id) {
      let index = this.teams.findIndex(el => {
        return el.id == id;
      });
      this.teams.splice(index, 1);
    },
    arrayProject() {
      let arr = [];
      this.allProjects.forEach(el => {
        arr.push(el.name);
      });
      return arr;
    },
    arrayStudents() {
      let arr = [];
      this.allStudents.forEach(el => {
        arr.push(el.fullname);
      });
      return arr;
    },
    onEdit(team) {
      if (this.flag == 0) {
        this.flag = team.id;
        this.formProject = this.findProject(team.project);
        this.formName = team.name;
      } else {
        this.flag = 0;
        let index = this.teams.findIndex(el => {
          return el.id == team.id;
        });
        this.teams[index].project = this.findProjectByName(this.formProject);
        this.teams[index].name = this.formName;
      }
    },
    findProject(id) {
      let obj = this.allProjects.find(el => {
        return el.id == id;
      });
      return obj.name;
    },
    findProjectByName(name) {
      let obj = this.allProjects.find(el => {
        return el.name == name;
      });
      return obj.id;
    },
    findStudentByName(name) {
      let obj = this.allStudents.find(el => {
        return el.fullname == name;
      });
      return obj.id;
    }
  },
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.teams.filter(el => {
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
        return this.teams;
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
