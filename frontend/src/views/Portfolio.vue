<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Портфолио студента</h2>
      </v-col>
    </v-row>
    <v-row
      v-if="
        student == undefined ||
        student == null ||
        allEvents == undefined ||
        allEvents == null ||
        allProjects == undefined ||
        allProjects == null ||
        allTeams == undefined ||
        allTeams == null
      "
    >
      <v-col>
        <h3>Подождите...</h3>
      </v-col>
    </v-row>
    <v-row
      v-if="
        student != undefined &&
        student != null &&
        allEvents != undefined &&
        allEvents != null &&
        allProjects != undefined &&
        allProjects != null &&
        allTeams != undefined &&
        allTeams != null
      "
    >
      <v-col>
        <v-card class="d-print-none mb-2 pb-3" elevation="2">
          <v-card-title>{{ student.fullname }}</v-card-title>
          <v-card-subtitle class="pb-0">{{
            formatDate(student.birthdate)
          }}</v-card-subtitle>
          <p class="ma-4 mt-0 mb-2 light-blue--text text--darken-3">
            E-mail: {{ student.email }}
          </p>
        </v-card>

        <v-card class="mb-2 pb-3 my-print" elevation="0">
          <v-card-title>{{ student.fullname }}</v-card-title>
          <v-card-subtitle class="pb-0">{{
            formatDate(student.birthdate)
          }}</v-card-subtitle>
          <p class="ma-4 mt-0 mb-2">E-mail: {{ student.email }}</p>
        </v-card>
      </v-col>
    </v-row>
    <v-row
      v-if="
        student != undefined &&
        student != null &&
        allEvents != undefined &&
        allEvents != null &&
        allProjects != undefined &&
        allProjects != null &&
        allTeams != undefined &&
        allTeams != null
      "
    >
      <v-col>
        <h3 class="mb-3">Участие в проектах</h3>
        <v-radio-group
          class="d-print-none"
          v-if="user && checkId()"
          v-model="radios1"
          mandatory
        >
          <h4 class="light-blue--text mb-2">Проект:</h4>
          <v-radio
            color="light-blue"
            label="Присоединиться к существующему"
            value="radio-1"
            @click="clearProject()"
          ></v-radio>
          <v-radio
            @click="clearProject()"
            color="light-blue"
            label="Добавить новый"
            value="radio-2"
          ></v-radio>
        </v-radio-group>
        <v-text-field
          v-if="user && radios1 == 'radio-2' && checkId()"
          v-model="projectName"
          color="light-blue"
          label="Название проекта"
          required
          class="d-print-none"
        ></v-text-field>
        <v-textarea
          v-if="user && radios1 == 'radio-2' && checkId()"
          name="input-7-1"
          color="light-blue"
          label="Описание проекта"
          v-model="projectDescription"
          class="mb-3 d-print-none"
        ></v-textarea>
        <v-textarea
          v-if="user && radios1 == 'radio-2' && checkId()"
          name="input-7-1"
          color="light-blue"
          label="Ссылки проекта"
          v-model="projectLinks"
          class="mb-3 d-print-none"
        ></v-textarea>

        <v-menu
          class="d-print-none"
          v-if="user && radios1 == 'radio-2' && checkId()"
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
              label="Дата начала проекта"
              prepend-icon="mdi-calendar"
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            v-model="date"
            no-title
            @input="menu2 = false"
          ></v-date-picker>
        </v-menu>

        <v-menu
          v-if="user && radios1 == 'radio-2' && checkId()"
          v-model="menu2"
          :close-on-content-click="true"
          transition="scale-transition"
          offset-y
          class="d-print-none"
          max-width="290px"
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="computedDateFormatted2"
              label="Дата окончания проекта"
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

        <v-select
          v-if="user && radios1 == 'radio-1' && checkId()"
          class="mb-3 d-print-none"
          :items="allProjects"
          item-text="name"
          item-value="id"
          label="Проект"
          dense
          required
          v-model="projectProject"
          color="light-blue"
        ></v-select>
        <v-radio-group
          v-if="user && radios1 == 'radio-1' && checkId()"
          v-model="radios2"
          mandatory
          class="d-print-none"
        >
          <h4 class="light-blue--text mb-2">Команда:</h4>
          <v-radio
            @click="clearTeam()"
            color="light-blue"
            label="Присоединиться к существующей"
            value="radio-3"
          ></v-radio>
          <v-radio
            @click="clearTeam()"
            color="light-blue"
            label="Добавить новую"
            value="radio-4"
          ></v-radio>
        </v-radio-group>
        <v-select
          v-if="
            user && radios1 == 'radio-1' && radios2 == 'radio-3' && checkId()
          "
          :items="
            allTeams.filter(
              el =>
                el.project.id == projectProject &&
                !student.studentsForTeam.find(elem => elem.id == el.id)
            )
          "
          item-text="name"
          item-value="id"
          label="Команда"
          dense
          required
          class="d-print-none"
          v-model="projectTeam"
          color="light-blue"
        ></v-select>
        <v-text-field
          v-if="
            (user &&
              radios1 == 'radio-1' &&
              radios2 == 'radio-4' &&
              checkId()) ||
            (user && radios1 == 'radio-2' && checkId())
          "
          v-model="projectTeamName"
          class="mb-3 d-print-none"
          color="light-blue"
          label="Название команды"
          required
        ></v-text-field>
        <v-btn
          v-if="user && checkId()"
          class="mb-5 white--text d-print-none"
          color="light-blue"
          @click="onAddYouInProject()"
          block="block"
          :disabled="!projectBtn"
        >
          Добавить участие в проекте
        </v-btn>
        <div v-if="student.studentsForTeam.length != 0">
          <Project
            v-for="project in student.studentsForTeam"
            :key="project.id"
            v-bind:project="project"
          ></Project>
        </div>
        <div v-if="student.studentsForTeam.length == 0">
          <span>Не найдено</span>
        </div>
      </v-col>

      <v-col>
        <h3 class="mb-6">Участие в мероприятиях</h3>
        <v-select
          v-if="user && checkId()"
          class="mb-3 d-print-none"
          :items="allEvents"
          item-text="name"
          item-value="id"
          label="Мероприятие"
          dense
          required
          v-model="eventEvent"
          color="light-blue"
        ></v-select>
        <v-select
          v-if="user && checkId()"
          class="mb-3 d-print-none"
          :items="roles"
          label="Ваша роль"
          dense
          required
          color="light-blue"
          v-model="eventRole"
        ></v-select>
        <v-btn
          v-if="user && checkId()"
          class="mb-5 white--text d-print-none"
          color="light-blue"
          @click="onAddYouInEvent()"
          block="block"
          :disabled="!eventBtn"
        >
          Добавить участие в мероприятии
        </v-btn>
        <div v-if="student.studentsInEvents.length != 0">
          <Event
            v-for="event in student.studentsInEvents"
            :key="event.id"
            v-bind:event="event"
          ></Event>
        </div>
        <div v-if="student.studentsInEvents.length == 0">
          <span>Не найдено</span>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Event from "@/components/Event.vue";
import Project from "@/components/Project.vue";
import {
  PORTFOLIO,
  SHORTEVENTS,
  SHORTPROJECTS,
  SHORTTEAMS,
  CREATEPROJECT,
  ADDTOTEAM,
  CREATETEAMWITHPERSONS,
  CREATESTUDENTINEVENT
} from "@/graphql/queries.js";
export default {
  name: "Portfolio",
  components: {
    Event,
    Project
  },
  apollo: {
    student: {
      query: PORTFOLIO,
      variables() {
        return {
          studentId: this.$route.params.id
        };
      }
    },
    allEvents: {
      query: SHORTEVENTS
    },
    allProjects: {
      query: SHORTPROJECTS
    },
    allTeams: {
      query: SHORTTEAMS
    }
  },

  data() {
    return {
      projectName: "",
      projectDescription: "",
      projectLinks: "",

      projectProject: "",

      projectTeam: "",

      projectTeamName: "",

      eventEvent: "",
      eventRole: "",

      date: new Date().toISOString().substr(0, 10),
      date2: new Date().toISOString().substr(0, 10),

      menu1: false,
      menu2: false,

      radios1: "radio-1",
      radios2: "radio-3",

      roles: ["Участник", "Волонтер", "Призер", "Победитель"]
    };
  },
  computed: {
    eventBtn() {
      if (this.eventEvent != "" && this.eventRole != "") return true;
      else return false;
    },
    projectBtn() {
      if (
        (this.projectName != "" &&
          this.projectDescription != "" &&
          this.projectLinks != "" &&
          this.projectTeamName != "") ||
        (this.projectProject != "" && this.projectTeam != "") ||
        (this.projectProject != "" && this.projectTeamName != "")
      )
        return true;
      else return false;
    },
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
    computedDateFormatted2() {
      return this.formatDate(this.date2);
    },
    user() {
      return this.$store.getters.isUser;
    },
    operator() {
      return this.$store.getters.isOperator;
    },
    admin() {
      return this.$store.getters.isAdmin;
    },
    userObj() {
      let obj = {
        name: localStorage.getItem("name"),
        id: undefined
      };
      if (this.user) {
        obj.id = localStorage.getItem("id");
      }
      return obj;
    }
  },
  methods: {
    checkId() {
      return this.userObj.id == this.$route.params.id;
    },
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      return `${day}.${month}.${year}`;
    },

    clearProject() {
      this.projectName = "";
      this.date = new Date().toISOString().substr(0, 10);
      this.date2 = new Date().toISOString().substr(0, 10);
      this.projectDescription = "";
      this.projectLinks = "";
      this.projectProject = "";
    },
    clearTeam() {
      this.projectTeam = "";
      this.projectTeamName = "";
    },
    onAddYouInEvent() {
      this.$apollo
        .mutate({
          mutation: CREATESTUDENTINEVENT,
          variables: {
            student: this.$route.params.id,
            event: this.eventEvent,
            role: this.eventRole
          }
        })
        .then(() => {
          this.$apollo.queries.student.refresh();
          this.$apollo.queries.student.refetch();
          this.eventRole = "";
          this.eventEvent = "";
        })
        .catch(error => {
          console.error(error);
        });
    },
    findParticipantByTeamID(id) {
      let obj = this.allTeams.find(el => el.id === id);
      let arr = [];
      obj.participants.forEach(element => {
        if (element.id != undefined) arr.push(element.id);
      });
      return arr;
    },

    onAddYouInProject() {
      if (
        this.projectName != "" &&
        this.projectDescription != "" &&
        this.projectLinks != ""
      ) {
        this.$apollo
          .mutate({
            mutation: CREATEPROJECT,
            variables: {
              name: this.projectName,
              dateStart: this.date,
              description: this.projectDescription,
              links: this.projectLinks,
              dateEnd: this.date2
            }
          })
          .then(res => {
            console.log(res);
            this.$apollo
              .mutate({
                mutation: CREATETEAMWITHPERSONS,
                variables: {
                  name: this.projectTeamName,
                  project: res.data.createProject.project.id,
                  participants: [this.$route.params.id]
                }
              })
              .then(() => {
                this.$apollo.queries.student.refresh();
                this.$apollo.queries.student.refetch();
                this.clearProject();
                this.clearTeam();
              })
              .catch(error => {
                console.error(error);
              });
          })
          .catch(error => {
            console.error(error);
          });
      } else {
        if (this.projectTeam != "") {
          let arr = this.findParticipantByTeamID(this.projectTeam);
          arr.push(this.$route.params.id);
          this.$apollo
            .mutate({
              mutation: ADDTOTEAM,
              variables: {
                teamId: this.projectTeam,
                participants: arr
              }
            })
            .then(() => {
              this.$apollo.queries.student.refresh();
              this.$apollo.queries.student.refetch();
              this.clearProject();
              this.clearTeam();
            })
            .catch(error => {
              console.error(error);
            });
        } else {
          this.$apollo
            .mutate({
              mutation: CREATETEAMWITHPERSONS,
              variables: {
                name: this.projectTeamName,
                project: this.projectProject,
                participants: [this.$route.params.id]
              }
            })
            .then(() => {
              this.$apollo.queries.student.refresh();
              this.$apollo.queries.student.refetch();
              this.clearProject();
              this.clearTeam();
            })
            .catch(error => {
              console.error(error);
            });
        }
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
.my-print {
  display: none;
}
@media print {
  .my-print {
    display: block !important;
  }
}
</style>
