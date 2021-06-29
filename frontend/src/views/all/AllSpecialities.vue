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
                :items="allFaculties"
                item-text="name"
                item-value="id"
                label="Факультет"
                dense
                required
                v-model="fullFaculties"
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
            <br v-if="flag != specialization.id" />
            <span class="light-blue--text" v-if="flag != specialization.id">
              Факультет: {{ specialization.faculty.name }}</span
            >
            <v-select
              v-if="flag == specialization.id"
              :items="allFaculties"
              item-text="name"
              item-value="id"
              label="Факультет"
              dense
              required
              v-model="formFaculty"
              color="light-blue"
            ></v-select>
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
import {
  SHORTFACULTIES,
  SPECIALIZATIONS,
  CREATESPECIALIZATION,
  UPDATESPECIALIZATION,
  DELETESPECIALIZATION
} from "@/graphql/queries.js";
export default {
  name: "AllSpecialities",
  apollo: {
    allFaculties: {
      query: SHORTFACULTIES
    },
    allSpecializations: {
      query: SPECIALIZATIONS
    }
  },
  data() {
    return {
      flag: 0,
      fullName: "",
      fullFaculties: "",
      fullCodename: "",

      findString: "",
      formName: "",
      formFaculty: "",
      formCodename: ""
    };
  },
  methods: {
    // Исправлено: добавление
    onAdd() {
      this.$apollo
        .mutate({
          mutation: CREATESPECIALIZATION,
          variables: {
            name: this.fullName,
            faculty: this.fullFaculties,
            codeName: this.fullCodename
          }
        })
        .then(() => {
          this.$apollo.queries.allSpecializations.refresh();
          this.$apollo.queries.allSpecializations.refetch();
          this.fullCodename = "";
          this.fullFaculties = "";
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
          mutation: DELETESPECIALIZATION,
          variables: {
            specializationId: id
          }
        })
        .then(() => {
          this.$apollo.queries.allSpecializations.refresh();
          this.$apollo.queries.allSpecializations.refetch();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Исправлено: обновление
    onEdit(specialization) {
      if (this.flag == 0) {
        this.flag = specialization.id;
        this.formCodename = specialization.codeName;
        this.formFaculty = specialization.faculty;
        this.formName = specialization.name;
      } else {
        this.flag = 0;
        let faculty;
        if (this.formFaculty.id == undefined) {
          faculty = this.formFaculty;
        } else faculty = this.formFaculty.id;
        this.$apollo
          .mutate({
            mutation: UPDATESPECIALIZATION,
            variables: {
              codeName: this.formCodename,
              name: this.formName,
              faculty: faculty,
              specializationId: specialization.id
            }
          })
          .then(() => {
            this.$apollo.queries.allSpecializations.refresh();
            this.$apollo.queries.allSpecializations.refetch();
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
        this.fullFaculties != "" &&
        this.fullCodename != ""
      )
        return true;
      else return false;
    },
    filterItems() {
      if (
        this.allSpecializations != null ||
        this.allSpecializations != undefined
      ) {
        if (this.findString !== "") {
          return this.allSpecializations.filter(el => {
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
          return this.allSpecializations;
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
