import { defineStore } from "pinia";
import { API_ENDPOINT } from "../main";

export const useNewsStore = defineStore("news", {
  state: () => {
    return {
      news: [],
    };
  },
  actions: {
    async fetchNews() {
      const response = await fetch(`${API_ENDPOINT}/news/`);
      this.news = await response.json();
    },

    getArticleById(id) {
      return this.news.find((article) => article.id === id);
    },
  },
});
