<template>
  <v-container class="pa-5 my-container">
    <v-row>
      <v-col>
        <h2 class="font-weight-regular">Выберите университет:</h2>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          outlined
          label="Поиск по полному или краткому названию университета"
          append-icon="mdi-magnify"
          v-model="findString"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card
          class="mb-5"
          v-for="university in filterItems"
          :key="university.id"
          elevation="2"
        >
          <v-card-title>{{ university.fullname }}</v-card-title>
          <v-card-subtitle>{{ university.location }}</v-card-subtitle>
          <v-card-text>{{ university.description }}</v-card-text>
          <v-card-actions>
            <v-btn text color="light-blue"> Выбрать </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Universities",
  data() {
    return {
      findString: "",
      universities: [
        {
          id: 1,
          fullname: "Московский политехнический университет",
          shortname: "Московский политех",
          location: "Москва",
          description:
            "Московский политехнический университет является крупнейшей образовательной организацией, готовящей квалифицированных специалистов для производства."
        },
        {
          id: 2,
          fullname: "Московский государственный университет",
          shortname: "МГУ",
          location: "Москва",
          description:
            "Моско́вский госуда́рственный университе́т и́мени М. В. Ломоно́сова — один из старейших и крупнейших классических университетов России, один из центров отечественной науки и культуры, расположенный в Москве."
        }
      ]
    };
  },
  computed: {
    filterItems() {
      if (this.findString !== "") {
        return this.universities.filter(el => {
          return (
            (el.fullname.toLowerCase().split(' ').join('').indexOf(this.findString.toLowerCase().split(' ').join('')) !== -1 &&
            el.fullname !== "") || (el.shortname.toLowerCase().split(' ').join('').indexOf(this.findString.toLowerCase().split(' ').join('')) !== -1 &&
            el.shortname !== "")
          );
        });
      } else {
        return this.universities;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
@media (max-width: 300px) {
  div.container.my-container {
    padding: 8px !important;
  }
}
</style>
