<template>
    <div class="container">
        <h1>Trending Tags</h1>
        <ul class="nav justify-content-center">
            <template v-for="trend in trends" :key="trend.name">
                <li class="nav-item">
                    <a class="nav-link" @click="updateStatuses(trend.name)">{{trend.name}}</a>
                </li>
            </template>
            <div v-if=posts>
                <StatusDisplayCards :posts=posts></StatusDisplayCards>
            </div>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';
import StatusDisplayCards from './StatusDisplayCards.vue';

export default {
    name: "trending-tags",
    data() {
        return {
            trends: "",
            posts: ""
        };
    },
    methods: {
        updateStatuses(tag){
            if(tag){
                axios.get("/public", {params: {tag:tag}})
                .then((res) => {
                    this.posts = res.data
                })
                .catch((error) => {
                    console.error(error);
                });
            }
        },
        getData() {
            axios.get("/trends")
                .then((res) => {
                    this.trends = res.data;
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