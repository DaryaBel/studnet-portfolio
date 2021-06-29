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
      if (this.login == "operator") {
        localStorage.setItem("operator", true);
        this.password = "";
        this.login = "";
        this.$router.push({ name: "Universities" });
      } else {
        if (this.login == "admin") {
          localStorage.setItem("admin", true);
          this.password = "";
          this.login = "";
          this.$router.push({ name: "Universities" });
        } else {
          localStorage.setItem("user", true);
          this.password = "";
          this.login = "";
          this.$router.push({ name: "Universities" });
        }
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>
