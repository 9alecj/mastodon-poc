<template>
    <div>
      <h1 class="display-3">Trending Links</h1>
      <div class="row" data-masonry='{"percentPosition": true }'>
            <LinkDisplayCard v-for="link in links" :key="link.url" :link=link></LinkDisplayCard>
        </div>
    </div>
  </template>
  
  <script>
import axios from 'axios';
import LinkDisplayCard from '@/components/cards/LinkDisplayCard.vue';

  
  export default {
    name: 'TrendingLinksView',
    data() {
        return {
            links: "",
        };
    },
    methods: {
        getData() {
            axios.get("/trending-links")
                .then((res) => {
                    this.links = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    },
    created() {
        this.getData();
    },
    components: { LinkDisplayCard }
  }
  </script>
  