import { createApp } from 'vue'
import App from './App.vue'
import Vue3TouchEvents from "vue3-touch-events";
import axios from 'axios'
import VueAxios from 'vue-axios'

let app = createApp(App)
app.use(Vue3TouchEvents, {dragFrequency: 15})
app.use(VueAxios, axios).mount('#app')
