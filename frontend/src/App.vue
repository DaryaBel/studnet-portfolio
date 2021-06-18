<template>
  <v-app id="inspire">
    <v-app-bar class="my-header" app color="light-blue" dark>
      <v-container class="py-0 fill-height">
        <v-app-bar-nav-icon
          v-if="user || operator || admin"
          @click="drawer = true"
        ></v-app-bar-nav-icon>
        <h2 class="mr-8 font-weight-regular pointer" @click="onLinkUniversities()">
          Портфолио
        </h2>

        <v-spacer></v-spacer>
        <div v-if="user || operator || admin" class="flexxx">
          <span>Беляева Дарья</span>
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

    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="light-blue--text text--accent-4"
        >
          <v-list-item v-if="user">
            <v-list-item-title  @click="onLinkPortfolio(1)">Профиль</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="user">
            <v-list-item-title >Проекты</v-list-item-title>
          </v-list-item>
          <v-list-item v-if="user">
            <v-list-item-title >Мероприятия</v-list-item-title>
          </v-list-item>
          <v-list-item @click="logOut()" >
            <v-list-item-title v-if="user || operator || admin"  class="danger--text">Выйти</v-list-item-title>
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
      group: null,
      user: false,
      operator: false,
      admin: false
    };
  },
  mounted() {
    if (localStorage.getItem("user")) this.user = true;
    else this.user = false;

    if (localStorage.getItem("operator")) this.operator = true;
    else this.operator = false;
    
    if (localStorage.getItem("admin")) this.admin = true;
    else this.admin = false;
  },
  methods: {
    onLinkUniversities() {
      this.$router.push({ name: "Universities" });
    },
    onLinkAuth() {
      this.$router.push({ name: "Auth" });
    },
    onLinkPortfolio(id) {
      this.$router.push({ name: "Portfolio", params: { id: id } });
    },
    logOut() {
      localStorage.removeItem("user");
      localStorage.removeItem("operator");
      localStorage.removeItem("admin");
      this.user = false;
      this.operator = false;
      this.admin = false;
      if (this.$router.currentRoute.name != "Auth") {
        this.$router.push({ name: "Auth" });
      } 
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
</style>
