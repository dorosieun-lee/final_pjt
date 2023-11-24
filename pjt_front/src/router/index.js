import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '@/views/MainPageView.vue'
import DepositView from '@/views/bank_product/DepositView.vue'
import SavingView from '@/views/bank_product/SavingView.vue'
import DepositDetailView from '@/views/bank_product/DepositDetailView.vue'
import SavingDetailView from '@/views/bank_product/SavingDetailView.vue'
import SearchBankView from '@/views/SearchBankView.vue'
import SignUpView from '@/views/user/SignUpView.vue'
import LoginView from '@/views/user/LoginView.vue'
import MMBoardView from '@/views/board/MMBoardView.vue'
import MMBoardCreateView from '@/views/board/MMBoardCreateView.vue'
import MMBoardDetailView from '@/views/board/MMBoardDetailView.vue'
import LocalBoardView from '@/views/board/LocalBoardView.vue'
import LocalBoardCreateView from '@/views/board/LocalBoardCreateView.vue'
import LocalBoardDetailView from '@/views/board/LocalBoardDetailView.vue'
import UserDetailView from '@/views/user/UserDetailView.vue'
import QuizView from '@/views/QuizView.vue'
import UserCommunityLogView from '@/views/user/UserCommunityLogView.vue'
import LikeProductsView from '@/views/user/LikeProductsView.vue'
import RecommendProductView from '@/views/user/RecommendProductView.vue'
import ChangePassView from '@/views/user/ChangePassView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { 
      path: '/',
      name: 'home',
      component: MainPageView
    },
    { 
      path: '/deposit/',
      name: 'deposit',
      component: DepositView
    },
    {
      path: '/saving/',
      name: 'saving',
      component: SavingView
    },
    {
      path: '/deposit/:fin_prdt_cd/:id/',
      name: 'DepositDetailView',
      component: DepositDetailView
    },
    {
      path: '/saving/:fin_prdt_cd/:id/',
      name: 'SavingDetailView',
      component: SavingDetailView
    },
    { 
      path: '/bank/',
      name: 'bank',
      component: SearchBankView
    },
    {
      path: '/signup/',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/changepassword/',
      name: 'changepassword',
      component: ChangePassView
    },
    {
      path: '/moneyMGMT/',
      name: 'moneyMGMT',
      component: MMBoardView
    },
    {
      path: '/moneyMGMT/create/',
      name: 'moneyMGMTCreate',
      component: MMBoardCreateView
    },
    {
      path: '/moneyMGMT/:board_pk/',
      name: 'moneyMGMTDetail',
      component: MMBoardDetailView
    },
    {
      path: '/moneyMGMT/:board_pk/update/',
      name: 'moneyMGMTUpdate',
      component: MMBoardCreateView
    },
    {
      path: '/local/',
      name: 'local',
      component: LocalBoardView
    },
    {
      path: '/local/create/',
      name: 'localCreate',
      component: LocalBoardCreateView
    },
    {
      path: '/local/:board_pk/',
      name: 'localDetail',
      component: LocalBoardDetailView
    },
    {
      path: '/local/:board_pk/update/',
      name: 'localUpdate',
      component: LocalBoardCreateView
    },
    {
      path: '/userdetail/',
      name: 'userdetail',
      component: UserDetailView
    },
    {
      path: '/quiz/',
      name: 'quiz',
      component: QuizView
    },
    {
      path: '/user-community-log/',
      name: 'userCommunityLog',
      component: UserCommunityLogView
    },
    {
      path: '/like-products/',
      name: 'likeProducts',
      component: LikeProductsView
    },
    {
      path: '/product-recommend/',
      name: 'productRecommend',
      component: RecommendProductView
    },
  ]
})

import { userCheckStore } from '@/stores/usercheck'

router.beforeEach((to, from) => {
  const store = userCheckStore()
  if (to.name === 'MainPageView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView'}
  }
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)){
    window.alert('이미 로그인 했습니다.')
    return { name: 'MainPageView' }
  }
})

export default router
