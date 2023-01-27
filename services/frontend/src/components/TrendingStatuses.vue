<template>
    <div class="container">
        <StatusDisplayCards :posts=posts></StatusDisplayCards>
    </div>
</template>

<script>
import axios from 'axios';
import StatusDisplayCards from './StatusDisplayCards.vue';

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
    components: { StatusDisplayCards }
};
</script>