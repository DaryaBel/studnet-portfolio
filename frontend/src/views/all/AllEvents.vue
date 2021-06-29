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
              >{{ event.location }}. {{ formatDate(event.date) }}</span
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
import {
  EVENTS,
  DELETEEVENT,
  CREATEEVENT,
  UPDATEEVENT
} from "@/graphql/queries.js";

export default {
  name: "AllEvents",
  apollo: {
    allEvents: {
      query: EVENTS
    }
  },
  data() {
    return {
      flag: 0,
      fullName: "",
      fullLocation: "",
      fullDescription: "",

      findString: "",
      formName: "",
      formLocation: "",
      formDescription: "",

      date: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),
      menu1: false,
      menu2: false
    };
  },
  methods: {
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    },
    // Исправлено: добавление
    onAdd() {
      this.$apollo
        .mutate({
          mutation: CREATEEVENT,
          variables: {
            name: this.fullName,
            location: this.fullLocation,
            description: this.fullDescription,
            date: this.date
          }
        })
        .then(() => {
          this.$apollo.queries.allEvents.refresh();
          this.$apollo.queries.allEvents.refetch();
          this.fullLocation = "";
          this.date = new Date().toISOString().substr(0, 10);
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
          mutation: DELETEEVENT,
          variables: {
            eventId: id
          }
        })
        .then(() => {
          this.$apollo.queries.allEvents.refresh();
          this.$apollo.queries.allEvents.refetch();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Исправлено: обновление
    onEdit(event) {
      if (this.flag == 0) {
        this.flag = event.id;
        this.formDescription = event.description;
        this.formLocation = event.location;
        this.formName = event.name;
        this.date2 = new Date(event.date).toISOString().substr(0, 10);
      } else {
        this.flag = 0;
        this.$apollo
          .mutate({
            mutation: UPDATEEVENT,
            variables: {
              eventId: event.id,
              name: this.formName,
              description: this.formDescription,
              date: this.date2,
              location: this.formLocation
            }
          })
          .then(() => {
            this.$apollo.queries.allEvents.refresh();
            this.$apollo.queries.allEvents.refetch();
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
        this.fullLocation != "" &&
        this.fullDescription != ""
      )
        return true;
      else return false;
    },
    filterItems() {
      if (this.allEvents != null || this.allEvents != undefined) {
        if (this.findString !== "") {
          return this.allEvents.filter(el => {
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
          return this.allEvents;
        }
      } else return [];
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
