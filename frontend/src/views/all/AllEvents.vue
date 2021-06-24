<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Все мероприятия</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по названию мероприятия"
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
              >Добавить мероприятие
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
                label="Место проведения"
                color="light-blue"
                v-model="fullLocation"
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
                    v-model="computedDateFormatted"
                    label="Дата мероприятия"
                    prepend-icon="mdi-calendar"
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="date"
                  no-title
                  @input="menu1 = false"
                ></v-date-picker>
              </v-menu>
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
          v-for="event in filterItems"
          :key="event.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != event.id">{{ event.name }}</span>
            <v-text-field
              v-if="flag == event.id"
              light="light"
              label="Название"
              color="light-blue"
              v-model="formName"
            ></v-text-field>
          </v-card-title>
          <v-card-subtitle>
            <span v-if="flag != event.id"
              >{{ event.location }}. {{ event.date }}</span
            >
            <v-text-field
              v-if="flag == event.id"
              light="light"
              label="Место проведения"
              color="light-blue"
              v-model="formLocation"
            ></v-text-field>
            <v-menu
              v-if="flag == event.id"
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
                  label="Дата мероприятия"
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
          </v-card-subtitle>
          <v-card-text>
            <span v-if="flag != event.id">
              {{ event.description }}
            </span>
            <v-textarea
              v-if="flag == event.id"
              color="light-blue"
              light="light"
              label="Описание"
              v-model="formDescription"
            ></v-textarea>
          </v-card-text>
          <v-card-actions>
            <v-btn
              v-if="flag != event.id"
              :disabled="flag != 0"
              text
              color="light-blue"
              @click="onEdit(event)"
            >
              Редактировать
            </v-btn>
            <v-btn
              v-if="flag == event.id"
              text
              color="light-blue"
              @click="onEdit(event)"
            >
              Сохранить
            </v-btn>
            <v-btn color="red" class="white--text" @click="onDelete(event.id)">
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
  name: "AllEvents",
  data() {
    return {
      flag: 0,
      fullName: "",
      fullLocation: "",
      fullDescription: "",
      fullDate: "",

      findString: "",
      formName: "",
      formLocation: "",
      formDescription: "",
      formDate: "",

      date: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
      menu1: false,
      menu2: false,
      events: [
        {
          id: 1,
          name: "Международный форум молодых ученых «РОЛЬ МОЛОДЫХ УЧЕНЫХ В РАЗВИТИИ НАУКИ, ТЕХНИКИ И ИННОВАЦИЙ» посвященный дню независимости Республики Казахстан",
          location: "Online. Платформа Zoom",
          description:
            "7-8 декабря 2020 года в рамках Международного форума молодых ученых «Роль молодых ученых в развитии науки, техники и инноваций» посвященного дню независимости Республики Казахстан проводился международный конкурс научно практических и научно исследовательских проектов.",
          date: `${new Date("2020-12-07").getDate()}.${
            new Date("2020-12-07").getMonth() + 1
          }.${new Date("2020-12-07").getFullYear()}
         `
        },
        {
          id: 2,
          name: "III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ»",
          location: "Online. Платформа Zoom",
          description:
            "20 ноября завершился III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ», включивший в себя 12 конференций и научно-методических семинаров, круглых столов и экспертных сессий",
          date: `${new Date("2020-11-20").getDate()}.${
            new Date("2020-11-20").getMonth() + 1
          }.${new Date("2020-11-20").getFullYear()}
         `
        },
        {
          id: 3,
          name: "Международный форум молодых ученых «РОЛЬ МОЛОДЫХ УЧЕНЫХ В РАЗВИТИИ НАУКИ, ТЕХНИКИ И ИННОВАЦИЙ» посвященный дню независимости Республики Казахстан",
          location: "Online. Платформа Zoom",
          description:
            "7-8 декабря 2020 года в рамках Международного форума молодых ученых «Роль молодых ученых в развитии науки, техники и инноваций» посвященного дню независимости Республики Казахстан проводился международный конкурс научно практических и научно исследовательских проектов.",
          date: `${new Date("2020-12-07").getDate()}.${
            new Date("2020-12-07").getMonth() + 1
          }.${new Date("2020-12-07").getFullYear()}
         `
        },
        {
          id: 4,
          name: "III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ»",
          location: "Online. Платформа Zoom",
          description:
            "20 ноября завершился III Международный научный Форум профессорско-преподавательского состава и молодых учёных «ЦИФРОВЫЕ ТЕХНОЛОГИИ: НАУКА, ОБРАЗОВАНИЕ, ИННОВАЦИИ», включивший в себя 12 конференций и научно-методических семинаров, круглых столов и экспертных сессий",
          date: `${new Date("2020-11-20").getDate()}.${
            new Date("2020-11-20").getMonth() + 1
          }.${new Date("2020-11-20").getFullYear()}
         `
        }
      ]
    };
  },
  methods: {
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    },
    parseDate(date) {
      if (!date) return null;

      const [month, day, year] = date.split("/");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },
    onAdd() {
      let obj = {
        id: 6,
        name: this.fullName,
        location: this.fullLocation,
        description: this.fullDescription,
        date: this.computedDateFormatted
      };
      this.events.push(obj);
      this.fullLocation = "";
      this.fullDate = "";
      this.fullDescription = "";
      this.fullName = "";
    },

    onDelete(id) {
      let index = this.events.findIndex(el => {
        return el.id == id;
      });
      this.events.splice(index, 1);
    },
    onEdit(event) {
      if (this.flag == 0) {
        this.flag = event.id;
        this.formDescription = event.description;
        this.formLocation = event.location;
        this.formDate = event.date;
        this.formName = event.name;
      } else {
        this.flag = 0;
        let index = this.events.findIndex(el => {
          return el.id == event.id;
        });
        this.events[index].location = this.formLocation;
        this.events[index].date = this.computedDateFormatted2;
        this.events[index].description = this.formDescription;
        this.events[index].name = this.formName;
      }
    }
  },
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.events.filter(el => {
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
        return this.events;
      }
    },
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
    computedDateFormatted2() {
      return this.formatDate(this.date2);
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
