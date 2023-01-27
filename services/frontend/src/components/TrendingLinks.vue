<template>
    <div class="container">
        <LinkDisplayCards :links=links></LinkDisplayCards>
    </div>
</template>

<script>
import axios from 'axios';
import LinkDisplayCards from './LinkDisplayCards.vue';


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
    components: { LinkDisplayCards }
};
</script>