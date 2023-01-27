<template v-if="posts">
    <div class="row" id="masonry">
        <template v-for="post in posts" :key="post.id">
            <div class="col-4">
                <div class="card grid-item">
                    <div class="container-fluid">
                        <div class="row content-row">
                            <div class="col-2 profile">
                                <img :src=post.profile_photo class="rounded float-left" alt="profile photo"
                                    style="width: 80px;">
                            </div>
                            <div class="col-6" style="text-align: top;">
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
                        <div class="row media" v-if=post.media>
                            <img :src=post.media class="rounded float-right cover" alt="photo"
                                style="max-height: 400px;">
                        </div>
                        <div class="row content-row">
                            <div class="col-4">
                                Replies Count: {{ post.replies_count }}
                            </div>
                            <div class="col-4">
                                Reblogs Count: {{ post.reblogs_count }}
                            </div>
                            <div class="col-4">
                                Favorites: {{ post.favourites_count }}
                            </div>
                        </div>
                    </div>
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

.card:hover {
    box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
}

img {
    border-radius: 10px;
}

.cover {
    object-fit: cover;
}
</style>