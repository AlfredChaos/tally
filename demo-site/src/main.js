import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import './style.css'
import App from './App.vue'
import routes from '../router/routes'


createApp(App).use(routes).use(ElementPlus).mount('#app')
