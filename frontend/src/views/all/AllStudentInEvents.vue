<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">
          Все участия студентов в мероприятиях
        </h2>
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
                :items="arrayEvents()"
                label="Мероприятие"
                dense
                required
                v-model="fullEvent"
                color="light-blue"
              ></v-select>
              <v-select
                v-model="fullStudent"
                :items="arrayStudents()"
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
              <v-btn color="light-blue" class="white--text" @click="onAdd()">
                Добавить
              </v-btn>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>

    <v-row>
      <v-col v-if="studentInEvents.length != 0">
        <v-card
          class="mb-5"
          v-for="item in studentInEvents"
          :key="item.id"
          elevation="2"
        >
          <v-card-title
            ><span v-if="flag != item.id"
              >{{ findStudent(item.student) }}. {{ item.role }} мероприятия "{{
                findEvent(item.event)
              }}"</span
            >
            <v-select
              v-if="flag == item.id"
              :items="arrayEvents()"
              label="Мероприятие"
              dense
              required
              v-model="formEvent"
              color="light-blue"
            ></v-select>
            <v-select
              v-if="flag == item.id"
              v-model="formStudent"
              :items="arrayStudents()"
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
          </v-card-title>
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
      <v-col v-if="studentInEvents.length == 0">
        <p class="text-center title">Не найдено</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "AllStudentInEvents",
  data() {
    return {
      flag: 0,
      fullRole: "",
      fullEvent: "",
      fullStudent: "",

      formRole: "",
      formEvent: "",
      formStudent: "",
      roles: ["Участник", "Волонтер", "Призер", "Победитель"],
      allEvents: [
        { id: 1, name: "Мероприятие 1" },
        { id: 2, name: "Мероприятие 2" },
        { id: 3, name: "Мероприятие 3" }
      ],
      allStudents: [
        { id: 1, fullname: "Иванова Екатерина Петровна" },
        { id: 2, fullname: "Емельянов Тихон Ярославович" },
        { id: 3, fullname: "Терентьев Эрик Михаилович" },
        { id: 4, fullname: "Лихачёва Злата Михаиловна" },
        { id: 5, fullname: "Попова Малика Авксентьевна" },
        { id: 6, fullname: "Васильева Нонна Ивановна" },
        { id: 7, fullname: "Кузнецова Наталья Геннадьевна" },
        { id: 8, fullname: "Фомичёва Эдита Мэлоровна" },
        { id: 9, fullname: "Рыбакова Кармелитта Михайловна" }
      ],
      studentInEvents: [
        {
          id: 1,
          student: 1,
          event: 1,
          role: "Победитель"
        },
        {
          id: 2,
          student: 2,
          event: 2,
          role: "Участник"
        }
      ]
    };
  },
  methods: {
    onAdd() {
      let obj = {
        id: 6,
        student: this.findStudentByName(this.fullStudent),
        event: this.findEventByName(this.fullEvent),
        role: this.fullRole
      };
      this.studentInEvents.push(obj);
      this.fullStudent = "";
      this.fullEvent = "";
      this.fullRole = "";
    },

    onDelete(id) {
      let index = this.studentInEvents.findIndex(el => {
        return el.id == id;
      });
      this.studentInEvents.splice(index, 1);
    },
    arrayEvents() {
      let arr = [];
      this.allEvents.forEach(el => {
        arr.push(el.name);
      });
      return arr;
    },
    arrayStudents() {
      let arr = [];
      this.allStudents.forEach(el => {
        arr.push(el.fullname);
      });
      return arr;
    },
    onEdit(studentInEvent) {
      if (this.flag == 0) {
        this.flag = studentInEvent.id;
        this.formStudent = this.findStudent(studentInEvent.student);
        this.formEvent = this.findEvent(studentInEvent.event);
        this.formRole = studentInEvent.role;
      } else {
        this.flag = 0;
        let index = this.studentInEvents.findIndex(el => {
          return el.id == studentInEvent.id;
        });
        this.studentInEvents[index].event = this.findEventByName(
          this.formEvent
        );
        this.studentInEvents[index].student = this.findStudentByName(
          this.formStudent
        );
        this.studentInEvents[index].role = this.formRole;
      }
    },
    findEvent(id) {
      let obj = this.allEvents.find(el => {
        return el.id == id;
      });
      return obj.name;
    },
    findEventByName(name) {
      let obj = this.allEvents.find(el => {
        return el.name == name;
      });
      return obj.id;
    },
    findStudent(id) {
      let obj = this.allStudents.find(el => {
        return el.id == id;
      });
      return obj.fullname;
    },
    findStudentByName(name) {
      let obj = this.allStudents.find(el => {
        return el.fullname == name;
      });
      return obj.id;
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
