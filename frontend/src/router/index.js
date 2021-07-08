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

const ifNotAuthenticated = (to, from, next) => {
  let role = localStorage.getItem("role");
  if (!role) {
    next();
    return;
  }
  next("/universities");
};

const ifAuthenticated = (to, from, next) => {
  let role = localStorage.getItem("role");
  if (role) {
    next();
    return;
  }
  next("/");
};

const routes = [
  {
    path: "/dashboard",
    name: "Dashboard",
    beforeEnter: ifAuthenticated,
    component: Dashboard
  },
  {
    path: "/universities",
    name: "Universities",
    beforeEnter: ifAuthenticated,
    component: Universities
  },
  {
    path: "/faculties/:id",
    name: "Faculties",
    beforeEnter: ifAuthenticated,
    component: Faculties
  },
  {
    path: "/specializations/:id",
    name: "Specializations",
    beforeEnter: ifAuthenticated,
    component: Specializations
  },
  {
    path: "/groups/:id",
    name: "Groups",
    beforeEnter: ifAuthenticated,
    component: Groups
  },
  {
    path: "/students/:id",
    name: "Students",
    beforeEnter: ifAuthenticated,
    component: Students
  },
  {
    path: "/portfolio/:id",
    name: "Portfolio",
    beforeEnter: ifAuthenticated,
    component: Portfolio
  },
  {
    path: "/",
    name: "Auth",
    beforeEnter: ifNotAuthenticated,
    component: Auth
  },
  {
    path: "/all-universities",
    name: "AllUniversities",
    beforeEnter: ifAuthenticated,
    component: AllUniversities
  },
  {
    path: "/all-faculties",
    name: "AllFaculties",
    beforeEnter: ifAuthenticated,
    component: AllFaculties
  },
  {
    path: "/all-specialities",
    name: "AllSpecialities",
    beforeEnter: ifAuthenticated,
    component: AllSpecialities
  },
  {
    path: "/all-groups",
    name: "AllGroups",
    beforeEnter: ifAuthenticated,
    component: AllGroups
  },
  {
    path: "/all-events",
    name: "AllEvents",
    beforeEnter: ifAuthenticated,
    component: AllEvents
  },
  {
    path: "/all-students-in-events",
    name: "AllStudentInEvents",
    beforeEnter: ifAuthenticated,
    component: AllStudentInEvents
  },
  {
    path: "/all-projects",
    name: "AllProjects",
    beforeEnter: ifAuthenticated,
    component: AllProjects
  },
  {
    path: "/all-teams",
    name: "AllTeams",
    beforeEnter: ifAuthenticated,
    component: AllTeams
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
