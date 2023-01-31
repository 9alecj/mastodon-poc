<template>
    <div>
      <h1 class="display-3">Trending Statuses</h1>
      <div class="row" data-masonry='{"percentPosition": true }'>
            <StatusDisplayCard v-for="post in posts" :key="post.id" :post="post"></StatusDisplayCard>
        </div>
    </div>
  </template>
  
  <script>
import axios from 'axios';
import StatusDisplayCard from '@/components/cards/StatusDisplayCard.vue';
  
  export default {
    name: 'TrendingStatusesView',
    data() {
        return {
            posts: "",
        };
    },
    methods: {
        getData() {
            axios.get("/trending-statuses")
                .then((res) => {
                    res.data.sort(function(a,b){
                        var valA = (a.media === null ? .5 : 2) * a.content.length
                        var valB = (b.media === null ? .5 : 2) * b.content.length
                        return valB - valA;
                    });
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
    components: { StatusDisplayCard }
  }
  </script>
  