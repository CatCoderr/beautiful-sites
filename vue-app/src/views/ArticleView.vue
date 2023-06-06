
<template>
  <div>
    <Navbar />
    <Article :id="id" />
    <Footer />
  </div>
</template>

<style scoped></style>


<script setup>
import Navbar from "../components/Navbar.vue";
import Article from "../components/Article.vue";
import Footer from "../components/Footer.vue";

import { useRoute } from "vue-router";

const route = useRoute();
const id = Number(route.params.id);

</script>
