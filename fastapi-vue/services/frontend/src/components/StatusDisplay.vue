<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">Profile Photo</th>
                <th scope="col">User</th>
                <th scope="col">Message</th>
                <th scope="col">Time</th>
            </tr>
        </thead>
        <tbody>
            <template v-if="posts">
                <template v-for="post in posts" :key="post.id">
                    <tr>
                        <td><img :src=post.profile_photo class="rounded float-left" alt="profile photo"
                                style="width: 80px;"></td>
                        <td>{{ post.username }}</td>
                        <td>
                            <div v-html="post.content"></div>
                            <div v-if=post.media>
                                <img :src=post.media class="rounded float-right" alt="photo" style="width: 100px;">
                            </div>
                        </td>
                        <td>{{ timeSince(Date.parse(post.post_time)) }}</td>
                    </tr>
                </template>
            </template>
        </tbody>
    </table>
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