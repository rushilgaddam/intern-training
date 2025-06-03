// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify' // this is the file above

const app = createApp(App)
app.use(vuetify)
app.mount('#app')
