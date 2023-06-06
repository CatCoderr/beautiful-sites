<template>
  <!-- По центру написать большим шрифтом "Контакты" -->
  <!-- Дальш внизу слева будет SVG файл, имя контакта (кликабельный) -->
  <!-- Используй tailwind css -->

  <!-- Надпись "Контакты" -->

  <!-- Отступ сверху и снизу 10px -->
  <h1 class="my-5 text-center text-4xl">Контакты</h1>

  <!-- Google Maps -->
  <div class="flex flex-col items-center">
    <iframe
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2587.15444607312!2d34.56436157613525!3d49.57597554994142!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40d82f64cd0cbd85%3A0x528a08266c1d4938!2z0J3QsNGG0ZbQvtC90LDQu9GM0L3QuNC5INGD0L3RltCy0LXRgNGB0LjRgtC10YIgwqvQn9C-0LvRgtCw0LLRgdGM0LrQsCDQv9C-0LvRltGC0LXRhdC90ZbQutCwINGW0LzQtdC90ZYg0K7RgNGW0Y8g0JrQvtC90LTRgNCw0YLRjtC60LDCuw!5e0!3m2!1sru!2sua!4v1686058278314!5m2!1sru!2sua"
      width="400"
      height="300"
      style="border: 0"
      allowfullscreen=""
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"
    ></iframe>

    <!-- Справа от карты будет контактная информация -->
    <a class="my-2 mt-5 flex items-center rounded-2xl p-2 bg-gray-100 hover:bg-gray-200" href="https://t.me/ext_cat" target="_blank">
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
          d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"
        />
      </svg>
      <span class="text-xl ml-2">Telegram</span>
    </a>
  </div>
</template>

<style scoped></style>
<script setup></script>
