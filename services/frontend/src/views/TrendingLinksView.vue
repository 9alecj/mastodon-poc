<template>
    <div>
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
  