<template>
  <v-app id="inspire">
    <v-app-bar class="my-header d-print-none" app color="light-blue" dark>
      <v-container class="py-0 fill-height">
        <v-app-bar-nav-icon
          v-if="user || operator || admin"
          @click="drawer = true"
        ></v-app-bar-nav-icon>
        <h2
          class="mr-8 font-weight-regular pointer"
          @click="onLinkUniversities()"
        >
          Портфолио
        </h2>

        <v-spacer></v-spacer>
        <div v-if="user || operator || admin" class="flexxx">
          <span>{{ userObj.name }}</span>
          <span v-if="operator"> Оператор</span>
          <span v-if="admin"> Администратор</span>
        </div>
        <v-btn
          v-if="!user && !operator && !admin"
          class="ml-4"
          text
          @click="onLinkAuth()"
          >Войти</v-btn
        >
      </v-container>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" fixed temporary>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="light-blue--text text--accent-4"
        >
          <v-list-item v-if="admin" @click="onLinkDashboard()">
            <v-list-item-title>Дашборд</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="user" @click="onLinkPortfolio(userObj.id)">
            <v-list-item-title>Профиль</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="admin" @click="onLinkAllUniversities()">
            <v-list-item-title>Университеты</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="admin" @click="onLinkAllFaculties()">
            <v-list-item-title>Факультеты</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="admin" @click="onLinkAllSpecialities()">
            <v-list-item-title>Специальности</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="admin" @click="onLinkAllGroups()">
            <v-list-item-title>Группы</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="operator || admin" @click="onLinkAllEvents()">
            <v-list-item-title>Мероприятия</v-list-item-title>
          </v-list-item>
          <v-list-item
            v-if="operator || admin"
            @click="onLinkAllStudentInEvents()"
          >
            <v-list-item-title>Студенты в мероприятиях</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="operator || admin" @click="onLinkAllProjects()">
            <v-list-item-title>Проекты</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="operator || admin" @click="onLinkAllTeams()">
            <v-list-item-title>Команды</v-list-item-title>
          </v-list-item>
          <v-list-item @click="logOut()">
            <v-list-item-title
              v-if="user || operator || admin"
              class="danger--text"
              >Выйти</v-list-item-title
            >
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col>
            <v-sheet min-height="70vh" rounded="lg">
              <router-view></router-view>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      drawer: false,
      group: null
    };
  },
  computed: {
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
    onLinkDashboard() {
      this.$router.push({ name: "Dashboard" });
    },
    onLinkUniversities() {
      this.$router.push({ name: "Universities" });
    },
    onLinkAllUniversities() {
      this.$router.push({ name: "AllUniversities" });
    },
    onLinkAllFaculties() {
      this.$router.push({ name: "AllFaculties" });
    },
    onLinkAllSpecialities() {
      this.$router.push({ name: "AllSpecialities" });
    },
    onLinkAllGroups() {
      this.$router.push({ name: "AllGroups" });
    },
    onLinkAllEvents() {
      this.$router.push({ name: "AllEvents" });
    },
    onLinkAllStudentInEvents() {
      this.$router.push({ name: "AllStudentInEvents" });
    },
    onLinkAllProjects() {
      this.$router.push({ name: "AllProjects" });
    },
    onLinkAllTeams() {
      this.$router.push({ name: "AllTeams" });
    },

    onLinkAuth() {
      this.$router.push({ name: "Auth" });
    },

    onLinkPortfolio(id) {
      this.$router.push({ name: "Portfolio", params: { id: id } });
    },
    logOut() {
      localStorage.removeItem("role");
      localStorage.removeItem("id");
      localStorage.removeItem("name");
      this.$store.commit("CLEAR_ROLE");
      this.$router.push({ name: "Auth" });
    }
  }
};
</script>

<style lang="scss" scoped>
.flexxx {
  display: flex;
  flex-direction: column;
  & * {
    text-align: right;
  }
}

.pointer {
  cursor: pointer !important;
}

@media (max-width: 365px) {
  header.my-header {
    height: 136px !important;
    & button.v-btn {
      margin-left: 0 !important;
    }
    & div {
      justify-content: center;
      align-items: center;
      & h2 {
        text-align: center;
        width: 100%;
        margin-right: 0 !important;
      }
    }
  }
  main.v-main {
    padding: 136px 0px 0px !important;
  }
}

@media print {
  main.v-main {
    padding: 0 0px 0px !important;
  }
}
</style>
