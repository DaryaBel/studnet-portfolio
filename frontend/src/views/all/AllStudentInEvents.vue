<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">
          Все участия студентов в мероприятиях
        </h2>
      </v-col>
    </v-row>
    <v-row
      v-if="allStudentsInEvents == null || allStudentsInEvents == undefined"
    >
      <v-col>
        <p>Подождите...</p>
      </v-col>
    </v-row>
    <v-row
      v-if="allStudentsInEvents != null && allStudentsInEvents != undefined"
    >
      <v-col>
        <p v-if="allStudentsInEvents.length != 0">
          <span
            v-if="
              allStudentsInEvents.length % 10 == 1 &&
              allStudentsInEvents.length % 100 != 11
            "
            >Найдена {{ allStudentsInEvents.length }} строка</span
          >
          <span
            v-if="
              allStudentsInEvents.length % 10 >= 2 &&
              allStudentsInEvents.length % 10 <= 4 &&
              allStudentsInEvents.length % 100 != 12 &&
              allStudentsInEvents.length % 100 != 13 &&
              allStudentsInEvents.length % 100 != 14
            "
            >Найдено {{ allStudentsInEvents.length }} строки</span
          >
          <span
            v-if="
              (allStudentsInEvents.length % 10 >= 5 &&
                allStudentsInEvents.length % 10 <= 9) ||
              (allStudentsInEvents.length % 100 >= 10 &&
                allStudentsInEvents.length % 100 <= 20) ||
              allStudentsInEvents.length % 10 == 0
            "
            >Найдено {{ allStudentsInEvents.length }} строк</span
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
              >Добавить участие студента в мероприятие
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-select
                :items="allEvents"
                item-text="name"
                item-value="id"
                label="Мероприятие"
                dense
                required
                v-model="fullEvent"
                color="light-blue"
              ></v-select>
              <v-select
                v-model="fullStudent"
                :items="allStudents"
                item-text="fullname"
                item-value="id"
                label="Студент"
                color="light-blue"
                required
              ></v-select>
              <v-select
                :items="roles"
                label="Роль"
                dense
                required
                color="light-blue"
                v-model="fullRole"
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

    <v-row
      v-if="allStudentsInEvents != null && allStudentsInEvents != undefined"
    >
      <v-col v-if="allStudentsInEvents.length != 0">
        <v-card
          class="mb-5"
          v-for="item in allStudentsInEvents"
          :key="item.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != item.id">{{ item.student.fullname }}</span>
            <v-select
              v-if="flag == item.id"
              :items="allEvents"
              item-text="name"
              item-value="id"
              label="Мероприятие"
              dense
              required
              v-model="formEvent"
              color="light-blue"
            ></v-select>
          </v-card-title>
          <v-card-subtitle>
            <span v-if="flag != item.id"
              >{{ item.role }} мероприятия "{{ item.event.name }}"</span
            >
          </v-card-subtitle>
          <v-card-text>
            <v-select
              v-if="flag == item.id"
              v-model="formStudent"
              :items="allStudents"
              item-text="fullname"
              item-value="id"
              label="Студент"
              color="light-blue"
              required
            ></v-select>
            <v-select
              v-if="flag == item.id"
              :items="roles"
              label="Роль"
              dense
              required
              color="light-blue"
              v-model="formRole"
            ></v-select>
          </v-card-text>
          <v-card-actions>
            <v-btn
              v-if="flag != item.id"
              :disabled="flag != 0"
              text
              color="light-blue"
              @click="onEdit(item)"
            >
              Редактировать
            </v-btn>
            <v-btn
              v-if="flag == item.id"
              text
              color="light-blue"
              @click="onEdit(item)"
            >
              Сохранить
            </v-btn>
            <v-btn color="red" class="white--text" @click="onDelete(item.id)">
              Удалить
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col v-if="allStudentsInEvents.length == 0">
        <p class="text-center title">Не найдено</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {
  SHORTEVENTS,
  STUDENTSINEVENTS,
  SHORTSTUDENTS,
  UPDATESTUDENTINEVENT,
  CREATESTUDENTINEVENT,
  DELETESTUDENTINEVENT
} from "@/graphql/queries.js";

export default {
  name: "AllStudentInEvents",
  apollo: {
    allEvents: {
      query: SHORTEVENTS
    },
    allStudentsInEvents: {
      query: STUDENTSINEVENTS
    },
    allStudents: {
      query: SHORTSTUDENTS
    }
  },
  data() {
    return {
      flag: 0,
      fullRole: "",
      fullEvent: "",
      fullStudent: "",

      formRole: "",
      formEvent: "",
      formStudent: "",
      roles: ["Участник", "Волонтер", "Призер", "Победитель"]
    };
  },
  computed: {
    addBtn() {
      if (this.fullRole != "" && this.fullEvent != "" && this.fullStudent != "")
        return true;
      else return false;
    }
  },
  methods: {
    // Исправлено: добавление
    onAdd() {
      this.$apollo
        .mutate({
          mutation: CREATESTUDENTINEVENT,
          variables: {
            student: this.fullStudent,
            event: this.fullEvent,
            role: this.fullRole
          }
        })
        .then(() => {
          this.$apollo.queries.allStudentsInEvents.refresh();
          this.$apollo.queries.allStudentsInEvents.refetch();
          this.fullStudent = "";
          this.fullEvent = "";
          this.fullRole = "";
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
          mutation: DELETESTUDENTINEVENT,
          variables: {
            studentInEventId: id
          }
        })
        .then(() => {
          this.$apollo.queries.allStudentsInEvents.refresh();
          this.$apollo.queries.allStudentsInEvents.refetch();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // Исправлено: обновление
    onEdit(studentInEvent) {
      if (this.flag == 0) {
        this.flag = studentInEvent.id;
        this.formStudent = studentInEvent.student;
        this.formEvent = studentInEvent.event;
        this.formRole = studentInEvent.role;
      } else {
        this.flag = 0;
        let student;
        if (this.formStudent.id == undefined) {
          student = this.formStudent;
        } else student = this.formStudent.id;
        let event;
        if (this.formEvent.id == undefined) {
          event = this.formEvent;
        } else event = this.formEvent.id;
        this.$apollo
          .mutate({
            mutation: UPDATESTUDENTINEVENT,
            variables: {
              event: event,
              role: this.formRole,
              student: student,
              studentInEventId: studentInEvent.id
            }
          })
          .then(() => {
            this.$apollo.queries.allStudentsInEvents.refresh();
            this.$apollo.queries.allStudentsInEvents.refetch();
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
