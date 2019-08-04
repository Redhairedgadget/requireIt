import Result from './components/Result'
import Question from './components/Question'
import Home from './components/Home'

import VueRouter from "vue-router";

const routes = [
    {path: '/', component: Home},
    {path: '/result', name: 'result', component: Result, props: true},
    {path: '/questionnaire', component: Question}
]

export default new VueRouter({
    mode: 'history',
    routes
})