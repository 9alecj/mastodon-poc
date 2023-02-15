<template>
  <div class="container">
    <h1 class="display-3">Latest Public Posts</h1>
    <masonry :cols="{ default: 3, 1400: 2, 1000: 1 }" :gutter="{ default: '30px' }">
      <PostDisplayCard v-for="post in posts" :key="post.id" :post="post"></PostDisplayCard>
    </masonry>
  </div>
</template>

<script>
import axios from 'axios';
import PostDisplayCard from '@/components/cards/PostDisplayCard.vue';

export default {
  name: 'PublicTimelineView',
  data() {
    return {
      posts: "",
    };
  },
  methods: {
    getData() {
      axios.get("/posts")
        .then((res) => {
          this.posts = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getData();
  },
  components: {
    PostDisplayCard
  }
}
</script>
