<template>
  <div>
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
