<template>
    <div class="container">
        <div class="d-grid gap-2 d-md-flex justify-content-center">
            <template v-for="trend in trends" :key="trend.name">
                <button class="btn btn-secondary" @click="updateStatuses(trend.name)" type="button">{{
                    trend.name
                }}</button>
            </template>
        </div>
        <div v-if=posts>
            <StatusDisplayCards :posts=posts></StatusDisplayCards>
        </div>
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
        updateStatuses(tag) {
            if (tag) {
                axios.get("/public", { params: { tag: tag } })
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

<style>

</style>