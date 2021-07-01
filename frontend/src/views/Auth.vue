<template>
  <v-layout align-center="align-center" justify-center="justify-center">
    <div class="col col-sm-8 col-md-6 col-lg-6 col-xl-6">
      <v-flex class="auth-form text-center">
        <h1 class="mt-8 mb-12 light-blue--text">Авторизация</h1>
        <v-card flat light="light">
          <v-card-text>
            <v-form>
              <v-text-field
                light="light"
                label="Логин"
                type="text"
                color="light-blue"
                required
                v-model="login"
              ></v-text-field>
              <v-text-field
                light="light"
                label="Пароль"
                :type="passShow ? 'text' : 'password'"
                color="light-blue"
                :append-icon="passShow ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="passShow = !passShow"
                required
                v-model="password"
              ></v-text-field>
              <v-btn
                class="mt-8 white--text"
                color="light-blue"
                @click="onLogin"
                block="block"
                :disabled="!addBtn"
              >
                Войти
              </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-flex>
    </div>
  </v-layout>
</template>

<script>
import { AUTH } from "@/graphql/queries.js";
export default {
  name: "Auth",

  data() {
    return {
      passShow: false,

      login: "",
      password: ""
    };
  },

  computed: {
    addBtn() {
      if (this.login != "" && this.password != "") return true;
      else return false;
    }
  },

  methods: {
    onLogin() {
      this.$apollo
        .mutate({
          mutation: AUTH,
          variables: {
            login: this.login,
            password: this.password
          }
        })
        .then(res => {
          this.login = "";
          this.password = "";
          if (res.data.auth.isOk) {
            if (res.data.auth.userGroup.name == "Операторы") {
              localStorage.setItem("role", "operator");
              localStorage.setItem("name", res.data.auth.user.firstName);
              this.$store.commit("SET_ROLE", "operator");
            }
            if (res.data.auth.userGroup.name == "Администраторы") {
              localStorage.setItem("role", "admin");
              localStorage.setItem("name", res.data.auth.user.firstName);
              this.$store.commit("SET_ROLE", "admin");
            }
            if (res.data.auth.userGroup.name == "Пользователи") {
              localStorage.setItem("name", res.data.auth.user.firstName);
              localStorage.setItem("id", res.data.auth.employee.student.id);
              localStorage.setItem("role", "user");
              this.$store.commit("SET_ROLE", "user");
            }
            this.$router.push({ name: "Universities" });
          }
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped></style>
