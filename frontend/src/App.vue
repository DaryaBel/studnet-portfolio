<template>
  <v-app id="inspire">
    <v-app-bar class="my-header" app color="light-blue"  dark>
      <v-container class="py-0 fill-height">
        <h2 class="mr-8 font-weight-regular">Портфолио</h2>

        <!-- <v-btn
          v-for="link in links"
          :key="link"
          text
        >
          {{ link }}
        </v-btn> -->

        <v-spacer></v-spacer>
        <v-btn text >Войти</v-btn>
      </v-container>
    </v-app-bar>

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
};
</script>

<style lang="scss" scoped>
@media (max-width: 300px) {
  header.my-header {
    height: 84px !important;
    & div div {
      justify-content: center;
      align-items: center;
      & h2 {
        text-align: center;
        width: 100%;
        margin-right: 0 !important;
      }
    }
  }
  main.v-main{
    padding: 84px 0px 0px !important;
    }
}
</style>