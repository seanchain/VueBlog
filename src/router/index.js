import Vue from 'vue'
import Router from 'vue-router'
import Blog from '@/components/Blog'
import About from '@/components/About'
import Post from '@/components/Post'

Vue.use(Router)

export default new Router({
  routes: [
    {path: '/', name: 'Hello', component: Blog},
    {path: '/about', name: 'About', component: About},
    {path: '/post/:name', name: 'Post', component: Post}
  ]
})
