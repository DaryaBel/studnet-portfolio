import Vue from "vue";
import VueRouter from "vue-router";
import Universities from "../views/Universities.vue";
import Faculties from "../views/Faculties.vue";
import Specializations from "../views/Specializations.vue";
import Groups from "../views/Groups.vue";
import Students from "../views/Students.vue";
import Portfolio from "../views/Portfolio.vue";
import Auth from "../views/Auth.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/universities",
    name: "Universities",
    component: Universities
  },
  {
    path: "/faculties/:id",
    name: "Faculties",
    component: Faculties
  },
  {
    path: "/specializations/:id",
    name: "Specializations",
    component: Specializations
  },
  {
    path: "/groups/:id",
    name: "Groups",
    component: Groups
  },
  {
    path: "/students/:id",
    name: "Students",
    component: Students
  },
  {
    path: "/portfolio/:id",
    name: "Portfolio",
    component: Portfolio
  },
  {
    path: "/",
    name: "Auth",
    component: Auth
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
