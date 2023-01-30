<template>
    <div class="container">
        <div class="d-grid gap-2 d-md-flex justify-content-center">
            <template v-for="trend in trends" :key="trend.name">
                <button class="btn btn-secondary" @click="updateStatuses(trend.name)" type="button">#{{
                    trend.name
                }}</button>
            </template>
        </div>
        <div v-if=posts>
            <h1 class="display-6">#{{trendName}}</h1>
            <div class="row" data-masonry='{"percentPosition": true }'>
                <StatusDisplayCard v-for="post in posts" :key="post.id" :post="post"></StatusDisplayCard>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import StatusDisplayCard from './cards/StatusDisplayCard.vue';

export default {
    name: "trending-tags",
    data() {
        return {
            trendName:"",
            trends: "",
            posts: ""
        };
    },
    methods: {
        updateStatuses(tag) {
            if (tag) {
                axios.get("/timelines/tag", { params: { tag: tag } })
                    .then((res) => {
                        this.trendName = tag;
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
    components: { StatusDisplayCard }
};
</script>

<style>

</style>