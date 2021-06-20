<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Все специальности</h2>
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
      <v-col>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header
              >Добавить cпециальность
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-text-field
                light="light"
                label="Название"
                color="light-blue"
                v-model="fullName"
              ></v-text-field>
              <v-text-field
                light="light"
                label="Кодовое название"
                color="light-blue"
                v-model="fullCodename"
              ></v-text-field>
              <v-select
                :items="arrayFaculties()"
                label="Факультет"
                dense
                required
                v-model="fullFaculties"
                color="light-blue"
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
          v-for="specialization in filterItems"
          :key="specialization.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != specialization.id">{{
              specialization.name
            }}</span>
            <v-text-field
              v-if="flag == specialization.id"
              light="light"
              label="Название"
              color="light-blue"
              v-model="formName"
            ></v-text-field>
          </v-card-title>
          <v-card-subtitle>
            <span v-if="flag != specialization.id">
              {{ specialization.codeName }}</span
            >
            <v-text-field
              v-if="flag == specialization.id"
              light="light"
              label="Кодовое название"
              color="light-blue"
              v-model="formCodename"
            ></v-text-field>
          </v-card-subtitle>
          <v-card-actions>
            <v-btn
              v-if="flag != specialization.id"
              :disabled="flag != 0"
              text
              color="light-blue"
              @click="onEdit(specialization)"
            >
              Редактировать
            </v-btn>
            <v-btn
              v-if="flag == specialization.id"
              text
              color="light-blue"
              @click="onEdit(specialization)"
            >
              Сохранить
            </v-btn>
            <v-btn
              color="red"
              class="white--text"
              @click="onDelete(specialization.id)"
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
export default {
  name: "AllSpecialities",
  data() {
    return {
      flag: 0,
      fullName: "",
      fullFaculties: "",
      fullCodename: "",

      findString: "",
      formName: "",
      formFaculty: "",
      formCodename: "",
      allFaculties: [
        { id: 1, name: "Факультет философии" },
        { id: 2, name: "Факультет информационных технологий" }
      ],
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
          faculty: 2
        }
      ]
    };
  },
  methods: {
    onAdd() {
      let obj = {
        id: 6,
        name: this.fullName,
        faculty: this.findFacultyByName(this.fullFaculties),
        codeName: this.fullCodename
      };
      this.specializations.push(obj);
      this.fullCodename = "";
      this.fullFaculties = "";
      this.fullName = "";
    },
    arrayFaculties() {
      let arr = [];
      this.allFaculties.forEach(el => {
        arr.push(el.name);
      });
      return arr;
    },
    onDelete(id) {
      let index = this.specializations.findIndex(el => {
        return el.id == id;
      });
      this.specializations.splice(index, 1);
    },
    onEdit(specialization) {
      if (this.flag == 0) {
        this.flag = specialization.id;
        this.formCodename = specialization.codeName;
        this.formFaculty = this.findFaculty(specialization.faculty);
        this.formName = specialization.name;
      } else {
        this.flag = 0;
        let index = this.specializations.findIndex(el => {
          return el.id == specialization.id;
        });
        this.specializations[index].faculty = this.findFacultyByName(
          this.formFaculty
        );
        this.specializations[index].codeName = this.formCodename;
        this.specializations[index].name = this.formName;
      }
    },
    findFaculty(id) {
      let obj = this.allFaculties.find(el => {
        return el.id == id;
      });
      return obj.name;
    },
    findFacultyByName(name) {
      let obj = this.allFaculties.find(el => {
        return el.name == name;
      });
      return obj.id;
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
              el.codeName !== "")
          );
        });
      } else {
        return this.specializations;
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
