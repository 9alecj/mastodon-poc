<template>
    <div class="container">
  <div class="row">
    <div class="col-sm">
      {{msg[0]}}
    </div>
    <div class="col-sm">
      One of three columns
    </div>
    <div class="col-sm">
      One of three columns
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'hello-world',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      axios.get('/test')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>