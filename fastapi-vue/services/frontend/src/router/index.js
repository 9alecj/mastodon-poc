import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PublicTimelineView from '../views/PublicTimelineView.vue'
import TrendingStatusesView from '../views/TrendingStatusesView.vue'


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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
