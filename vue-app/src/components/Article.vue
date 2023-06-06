<template>
  <!-- Слева по центру изображение новости, справа текст на уровне изображения -->

  <div class="my-5 flex flex-col md:flex-row">
    <div class="md:w-1/2">
      <img :src="article.image_url" :alt="article.title" class="w-full" />
    </div>
    <div class="md:w-1/2 md:pl-4">
      <h2 class="text-2xl font-bold">{{ article.title }}</h2>
      <p class="mt-4">{{ article.content }}</p>
      <br />
      <span
        class="inline-flex items-center rounded-full bg-indigo-100 px-3 py-0.5 text-sm font-medium text-indigo-800"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="h-6 w-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z"
          />
        </svg>

        <span class="ml-1">{{ article.author }}</span>
      </span>
    </div>
  </div>
</template>

<script>
import { useNewsStore } from "../stores/news";

export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
  },

  setup(props) {
    const store = useNewsStore();
    return {
      article: store.getArticleById(props.id),
    };
  },
};
</script>
