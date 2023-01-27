<template>
    <div>
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
  