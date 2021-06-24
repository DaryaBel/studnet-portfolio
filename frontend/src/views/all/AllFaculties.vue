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
          Найдено {{ filterItems.length }}
          <span
            v-if="
              filterItems.length % 10 == 1 && filterItems.length % 100 != 11
            "
            >строка</span
          >
          <span
            v-if="
              filterItems.length % 10 >= 2 &&
              filterItems.length % 10 <= 4 &&
              filterItems.length % 100 != 12 &&
              filterItems.length % 100 != 13 &&
              filterItems.length % 100 != 14
            "
            >строки</span
          >
          <span
            v-if="
              filterItems.length % 10 >= 5 &&
              filterItems.length % 10 <= 9 &&
              filterItems.length % 10 == 0 &&
              filterItems.length % 100 >= 10 &&
              filterItems.length % 100 <= 20
            "
            >строк</span
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
                :items="arrayUniversity()"
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
              Университет: {{ findUniversity(faculty.university) }}</span
            >
            <v-select
              v-if="flag == faculty.id"
              :items="arrayUniversity()"
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
export default {
  name: "AllFaculties",
  data() {
    return {
      flag: 0,
      fullName: "",
      fullUniversity: "",
      fullDescription: "",

      findString: "",
      formName: "",
      formUniversity: "",
      formDescription: "",
      allUniversities: [
        { id: 1, fullname: "Московский политехнический университет" },
        { id: 2, fullname: "Московский государственный университет" }
      ],
      faculties: [
        {
          id: 1,
          name: "Факультет информационных технологий",
          description:
            "Образовательные программы созданы совместно с профессионалами из Ассоциации Интернет Разработчиков, 1С, Autodesk, Mail.ru, Лаборатории Касперского, Яндекса и других ведущих ИТ-компаний, поэтому студенты получают самые актуальные знания и легко находят работу уже во время учебы на старших курсах. Мы оперативно реагируем на изменения ИТ-рынка и каждый год вносим изменения в учебные планы, а 30% наших преподавателей – руководители и сотрудники ведущих IT-компаний.",
          university: 1
        },
        {
          id: 2,
          name: "Транспортный факультет",
          description:
            "Основой образовательного процесса является дисциплина «Проектная деятельность». Во время обучения студенты проходят несколько этапов - от новой идеи, дизайна и проектирования, до производства и дальнейшей эксплуатации. Наши студенты сами делают гоночные болиды, которые участвуют и побеждают в соревнованиях, и мотоциклы – два года подряд сделанный ребятами электробайк устанавливает рекорд скорости на фестивале «Байкальская миля». Если в 2019 году скорость составила 145 км/час, то в 2020 году мы побили собственный рекорд в два раза – 210,5 км/час.",
          university: 1
        },
        {
          id: 3,
          name: "Факультет философии",
          description: "Много думаем",
          university: 2
        }
      ]
    };
  },
  methods: {
    onAdd() {
      let obj = {
        id: 6,
        name: this.fullName,
        university: this.findUniversityByName(this.fullUniversity),
        description: this.fullDescription
      };
      this.faculties.push(obj);
      this.fullUniversity = "";
      this.fullDescription = "";
      this.fullName = "";
    },
    arrayUniversity() {
      let arr = [];
      this.allUniversities.forEach(el => {
        arr.push(el.fullname);
      });
      return arr;
    },
    onDelete(id) {
      let index = this.faculties.findIndex(el => {
        return el.id == id;
      });
      this.faculties.splice(index, 1);
    },
    onEdit(faculty) {
      if (this.flag == 0) {
        this.flag = faculty.id;
        this.formDescription = faculty.description;
        this.formUniversity = this.findUniversity(faculty.university);
        this.formName = faculty.name;
      } else {
        this.flag = 0;
        let index = this.faculties.findIndex(el => {
          return el.id == faculty.id;
        });
        this.faculties[index].university = this.findUniversityByName(
          this.formUniversity
        );
        this.faculties[index].description = this.formDescription;
        this.faculties[index].name = this.formName;
      }
    },
    findUniversity(id) {
      let obj = this.allUniversities.find(el => {
        return el.id == id;
      });

      return obj.fullname;
    },
    findUniversityByName(fullname) {
      let obj = this.allUniversities.find(el => {
        return el.fullname == fullname;
      });
      return obj.id;
    }
  },
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.faculties.filter(el => {
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
        return this.faculties;
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
