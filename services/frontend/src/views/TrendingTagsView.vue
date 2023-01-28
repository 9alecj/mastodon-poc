<template>
    <div>
      <h1 class="display-3">Trending Tags</h1>
      <TrendingTags/>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
import TrendingTags from '../components/TrendingTags.vue';
  
  export default {
    name: 'TrendingTagsView',
    components: {
    TrendingTags
}
  }
  </script>
  