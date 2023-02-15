import { createRouter, createWebHistory } from 'vue-router'
import PublicTimelineView from '../views/PublicPostsView.vue'
import TrendingPostsView from '../views/TrendingPostsView.vue'
import TrendingLinksView from '../views/TrendingLinksView.vue'
import TrendingTagsView from '../views/TrendingTagsView.vue'


const routes = [
  {
    path: '/',
    name: 'public',
    component: PublicTimelineView
  },
  {
    path: '/trending-posts',
    name: 'trending-posts',
    component: TrendingPostsView
  },
  {
    path: '/trending-links',
    name: 'trending-links',
    component: TrendingLinksView
  },
  {
    path: '/trending-tags',
    name: 'trending-tags',
    component: TrendingTagsView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
