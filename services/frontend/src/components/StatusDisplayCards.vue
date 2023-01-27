<template v-if="posts">
    <div class="row" data-masonry='{"percentPosition": true }'>
        <template v-for="post in posts" :key="post.id">
            <div class="card grid-item">
                <div class="row content-row">
                    <div class="col-4 profile">
                        <img :src=post.profile_photo class="rounded float-left" alt="profile photo"
                            style="width: 80px;">
                    </div>
                    <div class="col-4" style="text-align: top;">
                        {{
                            post.username
                        }}
                    </div>
                    <div class="col-4">
                        {{ timeSince(Date.parse(post.post_time)) }}
                    </div>
                </div>
                <div class="row content-row">
                    <div class="col-12" style="text-align: left;">
                        <div v-html="post.content"></div>
                    </div>
                </div>
                <div class="row content-row">
                    <div class="col-4">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"
                            class="bi bi-reply-fill" viewBox="0 0 24 24">
                            <path
                                d="M5.921 11.9 1.353 8.62a.719.719 0 0 1 0-1.238L5.921 4.1A.716.716 0 0 1 7 4.719V6c1.5 0 6 0 7 8-2.5-4.5-7-4-7-4v1.281c0 .56-.606.898-1.079.62z" />
                        </svg>{{ post.replies_count }}
                    </div>
                    <div class="col-4">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"
                            class="bi bi-arrow-left-right" viewBox="0 0 24 24">
                            <path fill-rule="evenodd"
                                d="M1 11.5a.5.5 0 0 0 .5.5h11.793l-3.147 3.146a.5.5 0 0 0 .708.708l4-4a.5.5 0 0 0 0-.708l-4-4a.5.5 0 0 0-.708.708L13.293 11H1.5a.5.5 0 0 0-.5.5zm14-7a.5.5 0 0 1-.5.5H2.707l3.147 3.146a.5.5 0 1 1-.708.708l-4-4a.5.5 0 0 1 0-.708l4-4a.5.5 0 1 1 .708.708L2.707 4H14.5a.5.5 0 0 1 .5.5z" />
                        </svg>{{ post.reblogs_count }}
                    </div>
                    <div class="col-4">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor"
                            class="bi bi-star" viewBox="0 0 24 24">
                            <path
                                d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z" />
                        </svg>{{ post.favourites_count }}
                    </div>
                </div>
                <div class="row" v-if=post.media>
                    <img :src=post.media class="rounded float-right cover" alt="photo" style="max-height: 400px;">
                </div>
            </div>
        </template>
    </div>
</template>

<script>
export default {

    props: ['posts'],
    created: function () {
        console.log(this.posts)
    },
    methods: {
        timeSince: function (date) {
            var seconds = Math.floor((new Date() - date) / 1000);
            var interval = seconds / 31536000;
            if (interval > 1) {
                return Math.floor(interval) + " years ago";
            }
            interval = seconds / 2592000;
            if (interval > 1) {
                return Math.floor(interval) + " months ago";
            }
            interval = seconds / 86400;
            if (interval > 1) {
                return Math.floor(interval) + " days ago";
            }
            interval = seconds / 3600;
            if (interval > 1) {
                return Math.floor(interval) + " hours ago";
            }
            interval = seconds / 60;
            if (interval > 1) {
                return Math.floor(interval) + " minutes ago";
            }
            return Math.floor(seconds) + " seconds ago";
        }
    }
}
</script>
<style>
.profile {
    text-align: left;
    margin: auto;
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

.content-row {
    padding: 1rem;
}

img {
    border-radius: 10px;
}

.cover {
    object-fit: cover;
}
</style>