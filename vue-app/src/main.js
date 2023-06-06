import { createApp } from "vue";
import "./index.css";
import { createPinia } from "pinia";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import { useNewsStore } from "./stores/news";
import { useGalleryStore } from "./stores/gallery";

export const API_ENDPOINT = "https://api.mnx.pw";

const pinia = createPinia();

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("./views/HomeView.vue"),
  },
  {
    path: "/article/:id",
    name: "Article",
    component: () => import("./views/ArticleView.vue"),
  },
  {
    path: "/gallery",
    name: "Gallery",
    component: () => import("./views/GalleryView.vue"),
  },
  {
    path: "/contacts",
    name: "Contacts",
    component: () => import("./views/ContactsView.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("./views/AboutView.vue"),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

const app = createApp(App);
app.use(router);
app.use(pinia);

useNewsStore().fetchNews();
useGalleryStore().fetchGallery()

app.mount("#app");
