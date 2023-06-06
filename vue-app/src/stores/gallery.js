import { defineStore } from "pinia";
import { API_ENDPOINT } from "../main";

export const useGalleryStore = defineStore("gallery", {
  state: () => {
    return {
      gallery: [],
    };
  },
  actions: {
    async fetchGallery() {
      const response = await fetch(`${API_ENDPOINT}/gallery/`);
      this.gallery = await response.json();

      console.log(this.gallery)
    },
  },
});
