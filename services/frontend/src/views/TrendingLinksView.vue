<template>
    <div class="container">
        <h1 class="display-3">Trending Links</h1>
        <masonry   :cols="{default: 3, 1400: 2, 1000: 1}"
                   :gutter="{default: '30px'}">
            <LinkDisplayCard v-for="link in links" :key="link.url" :link=link></LinkDisplayCard>
        </masonry>
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
