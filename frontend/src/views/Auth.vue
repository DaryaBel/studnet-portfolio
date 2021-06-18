<template>
  <v-layout align-center="align-center" justify-center="justify-center">
    <div class="col col-sm-8 col-md-6 col-lg-6 col-xl-6">
      <v-flex class="auth-form text-center">
        <h1 class="mt-8 mb-12 light-blue--text">Авторизация</h1>
        <v-card flat light="light">
          <v-card-text>
            <v-form>
              <v-text-field
                :disabled="formLoading"
                light="light"
                label="Логин"
                type="text"
                color="light-blue"
                required
                :error-messages="loginErrors"
                v-model.trim="$v.form.login.$model"
                @input="
                  $v.form.login.$touch();
                  requestErrors = [];
                "
                @blur="
                  $v.form.login.$touch();
                  requestErrors = [];
                "
              ></v-text-field>
              <v-text-field
                :disabled="formLoading"
                light="light"
                label="Пароль"
                :type="passShow ? 'text' : 'password'"
                color="light-blue"
                :append-icon="passShow ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="passShow = !passShow"
                required
                :error-messages="passwordErrors"
                v-model.trim="$v.form.password.$model"
                @input="
                  $v.form.password.$touch();
                  requestErrors = [];
                "
                @blur="
                  $v.form.password.$touch();
                  requestErrors = [];
                "
              ></v-text-field>
              <v-btn
                class="mt-8 white--text"
                color="light-blue"
                :dark="!$v.form.$invalid && !formLoading"
                @click="onLogin"
                block="block"
                :disabled="$v.form.$invalid || formLoading"
                :loading="formLoading"
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
import { required } from "vuelidate/lib/validators";
export default {
  name: "Auth",
  data() {
    return {
      passShow: false,
      formLoading: false,
      form: {
        login: "",
        password: ""
      },
      requestErrors: []
    };
  },
  validations: {
    form: {
      login: {
        required
      },
      password: {
        required
      }
    }
  },
  computed: {
    loginErrors() {
      const errors = [];
      if (!this.$v.form.login.$dirty) return errors;
      !this.$v.form.login.required && errors.push("Данное поле обязательное!");
      this.requestErrors.length > 0 &&
        this.requestErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    },
    passwordErrors() {
      const errors = [];
      if (!this.$v.form.password.$dirty) return errors;
      !this.$v.form.password.required &&
        errors.push("Данное поле обязательное!");
      this.requestErrors.length > 0 &&
        this.requestErrors.forEach(element => {
          errors.push(element);
        });
      return errors;
    }
  },
  
  methods: {
    onLogin() {
      if (this.form.login == "operator") {
        localStorage.setItem("operator", true);
        this.form.password = "";
        this.form.login = "";
        this.$router.push({ name: "Universities" });
      } else {
        if (this.form.login == "admin") {
          localStorage.setItem("admin", true);
          this.form.password = "";
          this.form.login = "";
          this.$router.push({ name: "Universities" });
        } else {
          localStorage.setItem("user", true);
          this.form.password = "";
          this.form.login = "";
          this.$router.push({ name: "Universities" });
        }
      }

      //   let sendObj = { ...this.form };
      //   this.formLoading = true;
      //   this.$store.dispatch("LOG_IN", sendObj).then(
      //     () => {
      //       this.formLoading = false;
      //       this.$router.push("/");
      //     },
      //     errors => {
      //       this.formLoading = false;
      //       if (errors.non_field_errors) {
      //         for (
      //           let index = 0;
      //           index < errors.non_field_errors.length;
      //           index++
      //         ) {
      //           this.requestErrors.push(errors.non_field_errors[index]);
      //         }
      //       }
      //     }
      //   );
    }
  }
};
</script>

<style lang="scss" scoped></style>
