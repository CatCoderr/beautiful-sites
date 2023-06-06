<script setup>
import { useNewsStore } from "../stores/news";

const store = useNewsStore();
</script>

<template>
  <div class="grid grid-cols-1 gap-4 py-5 sm:grid-cols-2 lg:grid-cols-3">
    <div
      v-for="item in store.news"
      :key="item.id"
      class="relative flex transform flex-col overflow-hidden rounded-lg shadow-lg transition duration-500 ease-in-out hover:-translate-y-1 hover:scale-105 hover:shadow-xl"
    >
      <div class="flex flex-1 flex-col justify-between bg-white p-6">
        <div class="flex-1">
          <router-link
            class="mt-2 block text-xl font-semibold text-gray-900 hover:text-gray-600 dark:text-gray-100 dark:hover:text-gray-300"
            :to="{ name: 'Article', params: { id: item.id } }"
          >
            <div class="flex-shrink-0">
              <img
                class="h-50 w-full object-cover rounded-lg"
                :src="item.image_url"
                alt="News image"
              />
            </div>

            <p class="text-xl font-semibold text-gray-900 mt-2">
              {{ item.title }}
            </p>
            <p class="mt-3 text-base text-gray-500">
              {{ item.content.substring(0, 100) }}...
            </p>
            <div
              class="inline-flex items-center rounded-full bg-indigo-100 px-3 py-0.5 text-sm font-medium text-indigo-800 mt-5"
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

              <span class="ml-1">{{ item.author }}
              </span>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
