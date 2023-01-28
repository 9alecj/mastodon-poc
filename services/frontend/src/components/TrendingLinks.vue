<template>
    <div class="container">
        <div class="row" data-masonry='{"percentPosition": true }'>
            <LinkDisplayCard v-for="link in links" :key="link.url" :link=link></LinkDisplayCard>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import LinkDisplayCard from './cards/LinkDisplayCard.vue';

export default {
    name: "trending-links",
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
};
</script>