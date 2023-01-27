import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PublicTimelineView from '../views/PublicTimelineView.vue'
import TrendingStatusesView from '../views/TrendingStatusesView.vue'
import TrendingLinksView from '../views/TrendingLinksView.vue'
import TrendingTagsView from '../views/TrendingTagsView.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/public',
    name: 'public',
    component:PublicTimelineView
  },
  {
    path: '/trending-statuses',
    name: 'trending-statuses',
    component:TrendingStatusesView
  },
  {
    path: '/trending-links',
    name: 'trending-links',
    component:TrendingLinksView
  },
  {
    path: '/trends',
    name: 'trending-tags',
    component:TrendingTagsView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
