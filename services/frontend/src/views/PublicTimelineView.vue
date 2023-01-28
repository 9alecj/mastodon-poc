<template>
  <div>
    <h1 class="display-3">Latest Public Statuses</h1>
    <PublicTimeline/>
  </div>
</template>

<script>
// @ is an alias to /src
import PublicTimeline from '@/components/PublicTimeline.vue';

export default {
  name: 'PublicTimelineView',
  components: {
    PublicTimeline
}
}
</script>
