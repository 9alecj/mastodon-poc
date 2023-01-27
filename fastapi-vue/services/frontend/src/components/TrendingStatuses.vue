<template>
    <div class="container">
        <StatusDisplayCards :posts=postList></StatusDisplayCards>
    </div>
</template>

<script>
import axios from 'axios';
import StatusDisplayCards from './StatusDisplayCards.vue';

export default {
    name: "trending-statuses",
    data() {
        return {
            postList: "",
        };
    },
    methods: {
        getData() {
            axios.get("/trending-statuses")
                .then((res) => {
                    this.postList = res.data;
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