<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Все группы</h2>
      </v-col>
    </v-row>
    <v-row v-if="!(chip1 && chip2 && chip3)">
      <v-col>
        <span>Выберите фильтры: </span>
        <span
          v-if="!chip1"
          @click="chip1 = true"
          class="ma-2 light-blue--text pointer"
          >Бакалавриат</span
        >
        <span
          v-if="!chip2"
          @click="chip2 = true"
          class="ma-2 light-blue--text pointer"
          >Магистратура</span
        >
        <span
          v-if="!chip3"
          @click="chip3 = true"
          class="ma-2 light-blue--text pointer"
          >Аспирантура</span
        >
      </v-col>
    </v-row>
    <v-row v-if="chip1 || chip2 || chip3">
      <v-col>
        <span>Используются следующие фильтры: </span>
        <v-chip
          v-if="chip1"
          class="ma-2"
          close
          color="light-blue"
          outlined
          @click:close="chip1 = false"
        >
          Бакалавриат
        </v-chip>
        <v-chip
          v-if="chip2"
          class="ma-2"
          close
          color="light-blue"
          outlined
          @click:close="chip2 = false"
        >
          Магистратура
        </v-chip>
        <v-chip
          v-if="chip3"
          class="ma-2"
          close
          color="light-blue"
          outlined
          @click:close="chip3 = false"
        >
          Аспирантура
        </v-chip>
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
              >Добавить группу
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-text-field
                light="light"
                label="Кодовое название"
                color="light-blue"
                v-model="fullCodename"
              ></v-text-field>
              <v-select
                :items="degrees"
                label="Степень обучения"
                dense
                chips
                required
                v-model="fullDegree"
                color="light-blue"
              ></v-select>
              <v-text-field
                light="light"
                label="Курс"
                color="light-blue"
                v-model="fullCourse"
              ></v-text-field>

              <v-select
                :items="formsEducation"
                label="Форма обучения"
                dense
                required
                v-model="fullForms"
                color="light-blue"
              ></v-select>
              <v-select
                :items="allSpecializations"
                item-text="name"
                item-value="id"
                label="Специальность"
                dense
                required
                v-model="fullSpecialities"
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
          v-for="group in filterItems"
          :key="group.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != group.id">{{ group.codeName }}</span>
            <v-text-field
              v-if="flag == group.id"
              light="light"
              label="Номер группы"
              color="light-blue"
              v-model="formCodename"
            ></v-text-field>
          </v-card-title>
          <v-card-subtitle class="pb-0">
            <v-chip
              v-if="flag != group.id"
              color="light-blue"
              text-color="white"
              class="mr-1"
              >{{ group.studyDegree }}</v-chip
            >

            <v-select
              v-if="flag == group.id"
              :items="degrees"
              label="Степень обучения"
              dense
              chips
              required
              v-model="formDegree"
              color="light-blue"
            ></v-select>
            <span v-if="flag != group.id">
              {{ group.course }} курс. {{ group.formEducation }} форма обучения
            </span>

            <v-text-field
              v-if="flag == group.id"
              light="light"
              label="Курс"
              color="light-blue"
              v-model="formCourse"
            ></v-text-field>

            <v-select
              v-if="flag == group.id"
              :items="formsEducation"
              label="Форма обучения"
              dense
              required
              v-model="formForms"
              color="light-blue"
            ></v-select>
          </v-card-subtitle>
          <v-card-text>
            <br v-if="flag != group.id" />
            <span class="light-blue--text" v-if="flag != group.id">
              Специальность:
              {{ group.specialization.name }}</span
            >
            <v-select
              v-if="flag == group.id"
              :items="allSpecializations"
              item-text="name"
              item-value="id"
              label="Специальность"
              dense
              required
              v-model="formSpecialization"
              color="light-blue"
            ></v-select>
          </v-card-text>
          <v-card-actions>
            <v-btn
              v-if="flag != group.id"
              :disabled="flag != 0"
              text
              color="light-blue"
              @click="onEdit(group)"
            >
              Редактировать
            </v-btn>
            <v-btn
              v-if="flag == group.id"
              text
              color="light-blue"
              @click="onEdit(group)"
            >
              Сохранить
            </v-btn>
            <v-btn color="red" class="white--text" @click="onDelete(group.id)">
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
  SHORTSPECIALIZATIONS,
  GROUPS,
  CREATEGROUP,
  UPDATEGROUP,
  DELETEGROUP
} from "@/graphql/queries.js";

export default {
  name: "AllGroups",
  apollo: {
    allGroups: {
      query: GROUPS
    },
    allSpecializations: {
      query: SHORTSPECIALIZATIONS
    }
  },
  data() {
    return {
      fullCourse: "",
      fullForms: "",
      fullCodename: "",
      fullDegree: "",
      fullSpecialities: "",

      chip1: true,
      chip2: true,
      chip3: true,
      flag: 0,
      findString: "",
      formCourse: "",
      formDegree: "",
      formSpecialization: "",
      formForms: "",
      formCodename: "",
      formsEducation: ["Очная", "Заочная", "Очно-заочная"],
      degrees: ["Бакалавриат", "Магистратура", "Аспирантура"]
    };
  },
  methods: {
    // Исправлено: добавление
    onAdd() {
      this.$apollo
        .mutate({
          mutation: CREATEGROUP,
          variables: {
            course: this.fullCourse,
            codeName: this.fullCodename,
            specialization: this.fullSpecialities,
            formEducation: this.fullForms,
            studyDegree: this.fullDegree
          }
        })
        .then(() => {
          this.$apollo.queries.allGroups.refresh();
          this.$apollo.queries.allGroups.refetch();
          this.fullCodename = "";
          this.fullSpecialities = "";
          this.fullForms = "";
          this.fullDegree = "";
          this.fullCourse = "";
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
          mutation: DELETEGROUP,
          variables: {
            groupId: id
          }
        })
        .then(() => {
          this.$apollo.queries.allGroups.refresh();
          this.$apollo.queries.allGroups.refetch();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Исправлено: обновление
    onEdit(group) {
      if (this.flag == 0) {
        this.flag = group.id;
        this.formCodename = group.codeName;
        this.formSpecialization = group.specialization;
        this.formCourse = group.course;
        this.formForms = group.formEducation;
        this.formDegree = group.studyDegree;
      } else {
        this.flag = 0;
        let specialization;
        if (this.formSpecialization.id == undefined) {
          specialization = this.formSpecialization;
        } else specialization = this.formSpecialization.id;
        this.$apollo
          .mutate({
            mutation: UPDATEGROUP,
            variables: {
              codeName: this.formCodename,
              course: this.formCourse,
              formEducation: this.formForms,
              groupId: group.id,
              specialization: specialization,
              studyDegree: this.formDegree
            }
          })
          .then(() => {
            this.$apollo.queries.allGroups.refresh();
            this.$apollo.queries.allGroups.refetch();
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
        this.fullSpecialities != "" &&
        this.fullForms != "" &&
        this.fullDegree != "" &&
        this.fullCourse != "" &&
        this.fullCodename != ""
      )
        return true;
      else return false;
    },
    filterItems() {
      if (this.allGroups != null || this.allGroups != undefined) {
        let array = [];
        let bachelor = this.allGroups.filter(el => {
          return (
            el.studyDegree.toLowerCase().split(" ").join("") == "бакалавриат"
          );
        });
        let master = this.allGroups.filter(el => {
          return (
            el.studyDegree.toLowerCase().split(" ").join("") == "магистратура"
          );
        });
        let phd = this.allGroups.filter(el => {
          return (
            el.studyDegree.toLowerCase().split(" ").join("") == "аспирантура"
          );
        });
        if (this.chip1) array = array.concat(bachelor);
        if (this.chip2) array = array.concat(master);
        if (this.chip3) array = array.concat(phd);
        return array;
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
.pointer {
  cursor: pointer;
}
</style>
