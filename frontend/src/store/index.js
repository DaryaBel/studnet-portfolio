import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    role: localStorage.getItem("role")
  },
  getters: {
    isUser: state => {
      return state.role == "user";
    },
    isOperator: state => {
      return state.role == "operator";
    },
    isAdmin: state => {
      return state.role == "admin";
    }
  },
  mutations: {
    SET_ROLE(state, role) {
      state.role = role;
    },
    CLEAR_ROLE(state) {
      state.role = "";
    }
  },
  actions: {},
  modules: {}
});
