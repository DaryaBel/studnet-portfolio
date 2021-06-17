import Vue from "vue";
import VueRouter from "vue-router";
import Universities from "../views/Universities.vue";
import Faculties from "../views/Faculties.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Universities",
    component: Universities
  },
  {
    path: "/faculties",
    name: "Faculties",
    component: Faculties
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
