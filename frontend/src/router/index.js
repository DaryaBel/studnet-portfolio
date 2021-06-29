import Vue from "vue";
import VueRouter from "vue-router";
import Universities from "../views/Universities.vue";
import Faculties from "../views/Faculties.vue";
import Specializations from "../views/Specializations.vue";
import Groups from "../views/Groups.vue";
import Students from "../views/Students.vue";
import Portfolio from "../views/Portfolio.vue";
import Auth from "../views/Auth.vue";
import Dashboard from "../views/Dashboard.vue";

import AllUniversities from "../views/all/AllUniversities.vue";
import AllFaculties from "../views/all/AllFaculties.vue";
import AllSpecialities from "../views/all/AllSpecialities.vue";
import AllGroups from "../views/all/AllGroups.vue";
import AllEvents from "../views/all/AllEvents.vue";
import AllStudentInEvents from "../views/all/AllStudentInEvents.vue";
import AllProjects from "../views/all/AllProjects.vue";
import AllTeams from "../views/all/AllTeams.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard
  },
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
  },
  {
    path: "/all-universities",
    name: "AllUniversities",
    component: AllUniversities
  },
  {
    path: "/all-faculties",
    name: "AllFaculties",
    component: AllFaculties
  },
  {
    path: "/all-specialities",
    name: "AllSpecialities",
    component: AllSpecialities
  },
  {
    path: "/all-groups",
    name: "AllGroups",
    component: AllGroups
  },
  {
    path: "/all-events",
    name: "AllEvents",
    component: AllEvents
  },
  {
    path: "/all-students-in-events",
    name: "AllStudentInEvents",
    component: AllStudentInEvents
  },
  {
    path: "/all-projects",
    name: "AllProjects",
    component: AllProjects
  },
  {
    path: "/all-teams",
    name: "AllTeams",
    component: AllTeams
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
