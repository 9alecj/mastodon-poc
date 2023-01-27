<template v-if="links">
    <div class="row" data-masonry='{"percentPosition": true }'>
        <template v-for="link in links" :key="link.url">
            <div class="card grid-item" @click="openInNewTab(link.url)">
                <div class="row media" v-if=link.image>
                    <img :src=link.image class="cover" alt="photo" style="max-height: 400px;">
                </div>
                <div class="row card-text">
                    <div class="col-12">
                        <h4 style="color: dimgray;">{{ link.provider_name }}</h4>
                    </div>
                </div>
                <div class="row card-text">
                    <div class="col-12" style="text-align: left;">
                        <h3>{{ link.title }}</h3>
                    </div>
                </div>
                <div class="row card-text">
                    <div class="col-12" style="text-align: left;">
                        <div v-html="link.description"></div>
                    </div>
                </div>
                <div class="row card-text">
                    <div class="col-12 float-end">
                        <p style="color: gray; display: table-cell;vertical-align: bottom;">{{ link.author_name }}</p>
                    </div>
                </div>
            </div>
        </template>
    </div>
</template>

<script>
export default {

    props: ['links'],
    created: function () {
        console.log(this.links)
    },
    methods: {
        openInNewTab(url) {
            window.open(url, '_blank', 'noreferrer');
    },
    }
}
</script>
<style>
.card-text {
    padding-left: 1rem;
    padding-right: 1rem;
}

.card {
    overflow: hidden;
    padding-left: 0px !important;
    padding-right: 0px !important;
    text-align: top;
    width: 400px;
    background: #fff;
    border-radius: 10px;
    display: inline-block;
    margin: 1rem;
    position: relative;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
    transition: all 0.3s cubic-bezier(.25, .8, .25, 1);
}

.card:hover {
    cursor: pointer;
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
}

img {
    border-radius: 10px;
}

.cover {
    object-fit: cover;
}
</style>