<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Все университеты</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по полному или краткому названию университета"
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
              >Добавить университет
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-text-field
                light="light"
                label="Полное название"
                color="light-blue"
                v-model="fullFullname"
              ></v-text-field>
              <v-text-field
                light="light"
                label="Краткое название"
                color="light-blue"
                v-model="fullShortname"
              ></v-text-field>
              <v-text-field
                light="light"
                label="Город"
                color="light-blue"
                v-model="fullLocation"
              ></v-text-field>
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
          v-for="university in filterItems"
          :key="university.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != university.id">{{ university.fullname }}</span>
            <v-text-field
              v-if="flag == university.id"
              light="light"
              label="Полное название"
              color="light-blue"
              v-model="formFullname"
            ></v-text-field>
          </v-card-title>
          <v-card-subtitle>
            <span v-if="flag != university.id"> {{ university.location }}</span>
            <v-text-field
              v-if="flag == university.id"
              light="light"
              label="Город"
              color="light-blue"
              v-model="formLocation"
            ></v-text-field>
          </v-card-subtitle>
          <v-card-text>
            <span v-if="flag != university.id">
              {{ university.description }}
            </span>
            <v-textarea
              v-if="flag == university.id"
              color="light-blue"
              light="light"
              label="Описание"
              v-model="formDescription"
            ></v-textarea>
          </v-card-text>
          <v-card-actions>
            <v-btn
              v-if="flag != university.id"
              :disabled="flag != 0"
              text
              color="light-blue"
              @click="onEdit(university)"
            >
              Редактировать
            </v-btn>
            <v-btn
              v-if="flag == university.id"
              text
              color="light-blue"
              @click="onEdit(university)"
            >
              Сохранить
            </v-btn>
            <v-btn
              color="red"
              class="white--text"
              @click="onDelete(university.id)"
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
  UNIVERSITIES,
  DELETEUNIVERSITY,
  CREATEUNIVERSITY,
  UPDATEUNIVERSITY
} from "@/graphql/queries.js";
export default {
  name: "AllUniversities",
  apollo: {
    allUniversities: {
      query: UNIVERSITIES
    }
  },
  data() {
    return {
      flag: 0,
      fullFullname: "",
      fullShortname: "",
      fullDescription: "",
      fullLocation: "",

      findString: "",
      formFullname: "",
      formLocation: "",
      formDescription: ""
    };
  },
  components: {},
  computed: {
    addBtn() {
      if (
        this.fullFullname != "" &&
        this.fullShortname != "" &&
        this.fullDescription != "" &&
        this.fullLocation != ""
      )
        return true;
      else return false;
    },
    filterItems() {
      if (this.allUniversities != null || this.allUniversities != undefined) {
        if (this.findString !== "") {
          return this.allUniversities.filter(el => {
            return (
              (el.fullname
                .toLowerCase()
                .split(" ")
                .join("")
                .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
                -1 &&
                el.fullname !== "") ||
              (el.shortname
                .toLowerCase()
                .split(" ")
                .join("")
                .indexOf(this.findString.toLowerCase().split(" ").join("")) !==
                -1 &&
                el.shortname !== "")
            );
          });
        } else {
          return this.allUniversities;
        }
      } else return [];
    }
  },
  methods: {
    // Исправлено: добавление
    onAdd() {
      this.$apollo
        .mutate({
          mutation: CREATEUNIVERSITY,
          variables: {
            fullname: this.fullFullname,
            shortname: this.fullShortname,
            location: this.fullLocation,
            description: this.fullDescription
          }
        })
        .then(() => {
          this.$apollo.queries.allUniversities.refresh();
          this.$apollo.queries.allUniversities.refetch();
          this.fullLocation = "";
          this.fullDescription = "";
          this.fullFullname = "";
          this.fullShortname = "";
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
          mutation: DELETEUNIVERSITY,
          variables: {
            universityId: id
          }
        })
        .then(() => {
          this.$apollo.queries.allUniversities.refresh();
          this.$apollo.queries.allUniversities.refetch();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Исправлено: обновление
    onEdit(university) {
      if (this.flag == 0) {
        this.flag = university.id;
        this.formDescription = university.description;
        this.formFullname = university.fullname;
        this.formLocation = university.location;
      } else {
        this.flag = 0;
        this.$apollo
          .mutate({
            mutation: UPDATEUNIVERSITY,
            variables: {
              description: this.formDescription,
              fullname: this.formFullname,
              location: this.formLocation,
              universityId: university.id
            }
          })
          .then(() => {
            this.$apollo.queries.allUniversities.refresh();
            this.$apollo.queries.allUniversities.refetch();
          })
          .catch(error => {
            console.error(error);
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
