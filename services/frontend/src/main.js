import 'bootstrap/dist/css/bootstrap.css';
import masonry from 'vue-next-masonry';

import { createApp } from 'vue';
import axios from 'axios';

import App from './App.vue';
import router from './router';

const app = createApp(App);
app.use(masonry)

axios.defaults.baseURL = 'http://localhost:5000';  // the FastAPI backend

app.use(router);
app.mount("#app");