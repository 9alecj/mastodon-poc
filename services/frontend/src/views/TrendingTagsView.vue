<template>
    <div class="container">
        <h1 class="display-3">Trending Tags</h1>
        <div class="d-grid gap-2 d-md-flex justify-content-center">
            <template v-for="tag in tags" :key="tag.name">
                <button class="btn btn-secondary" @click="updateStatuses(tag.name)" type="button">#{{
                    tag.name
                }}</button>
            </template>
        </div>
        <div v-if=posts>
            <h1 class="display-6">#{{ tag }}</h1>
            <masonry :cols="{ default: 3, 1400: 2, 1000: 1 }" :gutter="{ default: '30px' }">
                <StatusDisplayCard v-for="post in posts" :key="post.id" :post="post"></StatusDisplayCard>
            </masonry>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import StatusDisplayCard from '@/components/cards/StatusDisplayCard.vue';

export default {
    name: 'TrendingTagsView',
    data() {
        return {
            tag: "",
            tags: "",
            posts: ""
        };
    },
    methods: {
        getData() {
            axios.get("/trends")
                .then((res) => {
                    this.tags = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        updateStatuses(tag) {
            if (tag) {
                axios.get("/timelines/tag", { params: { tag: tag } })
                    .then((res) => {
                        this.tag = tag;
                        res.data.sort(function (a, b) {
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
    },
    created() {
        this.getData();
    },
    components: { StatusDisplayCard }
}
</script>
