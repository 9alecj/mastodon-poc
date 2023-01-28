<template>
    <div>
      <h1 class="display-3">Trending Statuses</h1>
      <TrendingStatuses/>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
import TrendingStatuses from '@/components/TrendingStatuses.vue';
  
  export default {
    name: 'TrendingStatusesView',
    components: {
    TrendingStatuses
}
  }
  </script>
  