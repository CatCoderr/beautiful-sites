<script setup>
import { useGalleryStore } from "../stores/gallery";

const store = useGalleryStore();
</script>

<template>
  <div class="grid grid-cols-1 gap-4 md:grid-cols-1 lg:grid-cols-4">
    <!-- Iterate over each gallery item -->
    <div
      v-for="item in store.gallery"
      :key="item.id"
      class="animate-fadeIn rounded bg-white p-4 shadow"
    >
      <!-- Display multiple images if available -->
      <template v-if="item.images.length > 1">
        <div class="grid grid-cols-2 gap-2">
          <!-- Iterate over each image in the item -->
          <img
            v-for="(image, index) in item.images"
            :key="index"
            :src="image"
            alt="Gallery Image"
            class="h-auto w-full animate-pulse rounded"
          />
        </div>
      </template>

      <!-- Display a single image if no multiple images are available -->
      <template v-else>
        <!-- Rounded image with hover effect -->
        <img
          :src="item.images[0]"
          alt="Gallery Image"
          class="h-auto w-full transform rounded transition duration-300 hover:scale-105"
        />
      </template>

      <div class="mt-4">
        <h3 class="text-xl font-bold">{{ item.name }}</h3>
        <p class="text-gray-500">{{ item.place }}</p>
        <p class="text-gray-500">{{ item.address }}</p>
        <!-- Description can contain \n, handle it propertly -->
        <p class="mt-2">{{ item.description }}</p>
      </div>
      <!-- Кнопка, которая перекидывает на страницу источника -->
      <!-- Кнопка фиолетовая, заокругленная -->
      <a :href="item.source" target="_blank" class="mt-4 inline-flex items-center rounded-full bg-indigo-100 px-3 py-0.5 text-sm font-medium text-indigo-800 hover:bg-indigo-200">
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
            d="M13.5 6H5.25A2.25 2.25 0 003 8.25v10.5A2.25 2.25 0 005.25 21h10.5A2.25 2.25 0 0018 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25"
          />
        </svg>
        <span class="ml-1">Джерело</span>

      </a>
    </div>
  </div>
</template>
