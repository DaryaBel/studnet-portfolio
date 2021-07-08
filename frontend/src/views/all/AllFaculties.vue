<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Все факультеты</h2>
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
              >Добавить факультет
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-text-field
                light="light"
                label="Название"
                color="light-blue"
                v-model="fullName"
              ></v-text-field>
              <v-select
                :items="allUniversities"
                item-text="fullname"
                item-value="id"
                label="Университет"
                dense
                required
                v-model="fullUniversity"
                color="light-blue"
              ></v-select>
              <v-textarea
                color="light-blue"
                light="light"
                label="Описание"
                v-model="fullDescription"
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
          v-for="faculty in filterItems"
          :key="faculty.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != faculty.id">{{ faculty.name }}</span>
            <v-text-field
              v-if="flag == faculty.id"
              light="light"
              label="Название"
              color="light-blue"
              v-model="formName"
            ></v-text-field>
          </v-card-title>
          <v-card-text>
            <span v-if="flag != faculty.id">
              {{ faculty.description }}
            </span>
            <v-textarea
              v-if="flag == faculty.id"
              color="light-blue"
              light="light"
              label="Описание"
              v-model="formDescription"
            ></v-textarea>
            <br v-if="flag != faculty.id" />
            <span class="light-blue--text" v-if="flag != faculty.id">
              Университет: {{ faculty.university.fullname }}</span
            >
            <v-select
              v-if="flag == faculty.id"
              :items="allUniversities"
              item-text="fullname"
              item-value="id"
              label="Университет"
              dense
              required
              v-model="formUniversity"
              color="light-blue"
            ></v-select>
          </v-card-text>
          <v-card-actions>
            <v-btn
              v-if="flag != faculty.id"
              :disabled="flag != 0"
              text
              color="light-blue"
              @click="onEdit(faculty)"
            >
              Редактировать
            </v-btn>
            <v-btn
              v-if="flag == faculty.id"
              text
              color="light-blue"
              @click="onEdit(faculty)"
            >
              Сохранить
            </v-btn>
            <v-btn
              color="red"
              class="white--text"
              @click="onDelete(faculty.id)"
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
  FACULTIES,
  SHORTUNIVERSITIES,
  DELETEFACULTY,
  CREATEFACULTY,
  UPDATEFACULTY
} from "@/graphql/queries.js";

export default {
  name: "AllFaculties",
  apollo: {
    allFaculties: {
      query: FACULTIES
    },
    allUniversities: {
      query: SHORTUNIVERSITIES
    }
  },
  data() {
    return {
      flag: 0,
      fullName: "",
      fullUniversity: "",
      fullDescription: "",

      findString: "",
      formName: "",
      formUniversity: "",
      formDescription: ""
    };
  },
  methods: {
    // Исправлено: добавление
    onAdd() {
      this.$apollo
        .mutate({
          mutation: CREATEFACULTY,
          variables: {
            name: this.fullName,
            university: this.fullUniversity,
            description: this.fullDescription
          }
        })
        .then(() => {
          this.$apollo.queries.allFaculties.refresh();
          this.$apollo.queries.allFaculties.refetch();
          this.fullUniversity = "";
          this.fullDescription = "";
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
          mutation: DELETEFACULTY,
          variables: {
            facultyId: id
          }
        })
        .then(() => {
          this.$apollo.queries.allFaculties.refresh();
          this.$apollo.queries.allFaculties.refetch();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Исправлено: обновление
    onEdit(faculty) {
      if (this.flag == 0) {
        this.flag = faculty.id;
        this.formDescription = faculty.description;
        this.formUniversity = faculty.university;
        this.formName = faculty.name;
      } else {
        this.flag = 0;
        let university;
        if (this.formUniversity.id == undefined) {
          university = this.formUniversity;
        } else university = this.formUniversity.id;
        this.$apollo
          .mutate({
            mutation: UPDATEFACULTY,
            variables: {
              description: this.formDescription,
              name: this.formName,
              university: university,
              facultyId: faculty.id
            }
          })
          .then(() => {
            this.$apollo.queries.allFaculties.refresh();
            this.$apollo.queries.allFaculties.refetch();
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  },
  computed: {
    addBtn() {
      if (
        this.fullName != "" &&
        this.fullUniversity != "" &&
        this.fullDescription != ""
      )
        return true;
      else return false;
    },
    filterItems() {
      if (this.allFaculties != null || this.allFaculties != undefined) {
        if (this.findString !== "") {
          return this.allFaculties.filter(el => {
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
          return this.allFaculties;
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
