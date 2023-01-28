<template>
    <div class="container">
        <div class="row" data-masonry='{"percentPosition": true }'>
            <StatusDisplayCard v-for="post in posts" :key="post.id" :post="post"></StatusDisplayCard>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import StatusDisplayCard from './cards/StatusDisplayCard.vue';

export default {
    name: "trending-statuses",
    data() {
        return {
            posts: "",
        };
    },
    methods: {
        getData() {
            axios.get("/trending-statuses")
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
    components: { StatusDisplayCard }
};
</script>