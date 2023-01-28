<template>
    <div>
      <h1 class="display-3">Trending Links</h1>
      <TrendingLinks/>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
import TrendingLinks from '@/components/TrendingLinks.vue';
  
  export default {
    name: 'TrendingLinksView',
    components: {
    TrendingLinks
}
  }
  </script>
  