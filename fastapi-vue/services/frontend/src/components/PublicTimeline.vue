<template>
  <div class="container">
    <StatusDisplay :posts=postList></StatusDisplay>
  </div>
</template>

<script>
import axios from 'axios';
import StatusDisplay from './StatusDisplay.vue';

export default {
    name: "public-timeline",
    data() {
        return {
            postList: "",
        };
    },
    methods: {
        getData() {
            axios.get("/public")
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
    components: { StatusDisplay }
};
</script>