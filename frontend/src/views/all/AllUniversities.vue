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
export default {
  name: "AllUniversities",
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
      formDescription: "",
      universities: [
        {
          id: 1,
          fullname: "Московский политехнический университет",
          shortname: "Московский политех",
          location: "Москва",
          description:
            "Московский политехнический университет является крупнейшей образовательной организацией, готовящей квалифицированных специалистов для производства."
        },
        {
          id: 2,
          fullname: "Московский государственный университет",
          shortname: "МГУ",
          location: "Москва",
          description:
            "Моско́вский госуда́рственный университе́т и́мени М. В. Ломоно́сова — один из старейших и крупнейших классических университетов России, один из центров отечественной науки и культуры, расположенный в Москве."
        }
      ]
    };
  },
  components: {},
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.universities.filter(el => {
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
        return this.universities;
      }
    }
  },
  methods: {
    onAdd() {
      let obj = {
        id: 5,
        fullname: this.fullFullname,
        shortname: this.fullShortname,
        location: this.fullLocation,
        description: this.fullDescription
      };
      this.universities.push(obj);
      this.fullLocation = "";
      this.fullDescription = "";
      this.fullFullname = "";
      this.fullShortname = "";
    },
    onDelete(id) {
      let index = this.universities.findIndex(el => {
        return el.id == id;
      });
      this.universities.splice(index, 1);
    },
    onEdit(university) {
      if (this.flag == 0) {
        this.flag = university.id;
        this.formDescription = university.description;
        this.formFullname = university.fullname;
        this.formLocation = university.location;
      } else {
        this.flag = 0;
        let index = this.universities.findIndex(el => {
          return el.id == university.id;
        });
        this.universities[index].description = this.formDescription;
        this.universities[index].location = this.formLocation;
        this.universities[index].fullname = this.formFullname;
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
