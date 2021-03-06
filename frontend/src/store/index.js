import Vue from 'vue'
import Vuex from 'vuex'
import { WebApp } from '../api/web-apps'
import {
  ADD_APP,
  REMOVE_APP,
  SET_APPS
} from './mutation-types.js'
Vue.use(Vuex)
// State
const state = {
  webapps: []  // webapp list
}
// Getters
const getters = {
    webapps: state => state.webapps,

}
// Mutations
const mutations = {
  // Add webapp to list
  [ADD_APP] (state, webapp) {
    state.webapps = [webapp, ...state.webapps]
  },
  // Remove webapp
  [REMOVE_APP] (state, { id }) {
    state.webapps = state.webapps.filter(webapp => {
      return webapp.id !== id
    })
  },
  // Set webapps
  [SET_APPS] (state, { webapps, reqs }) {
    state.webapps = webapps
    state.reqs = reqs
  }
}
// Actions
const actions = {
  createWebApp ({ commit }, webAppData) {
    WebApp.create(webAppData).then(webApp => {
      commit(ADD_APP, webApp)
    })
  },
  deleteWebApp ({ commit }, webApp) {
    WebApp.delete(webApp).then(response => {
      commit(REMOVE_APP, webApp)
    })
  },
  getWebApps({ commit }, data) {
    WebApp.list(data).then(function(webapps){
      console.log("LALA: " + commit(SET_APPS, { webapps }))
      commit(SET_APPS, { webapps })
    })
  }
}
export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})