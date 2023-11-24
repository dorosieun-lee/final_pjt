import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import { userCheckStore } from '@/stores/usercheck'
import axios from 'axios'

export const useBoardStore = defineStore('board', () => {
  const userStore = userCheckStore()
  const MMboardAll = ref()
  const MMboardDetail = ref(null)
  const LboardAll = ref(null)
  const LboardDetail = ref(null)
  
  
  const getBoards =  function(boardName) {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/api/v1/boards/${boardName}/`,
      // 전체 게시글 조회는 비로그인 사용자도 가능 (메인페이지 표출도 가능)
      // headers: {
      //     Authorization: `Token ${userStore.token}`
      // }
  })
  .then((res) => {
      // console.log('전체 게시글 불러오기')
      if (boardName === 'moneyMGMT') {
        MMboardAll.value = res.data
      } else if (boardName === 'local') {
        LboardAll.value = res.data
      }
  })
  .catch((err) => {
      console.log(err)
      if (boardName === 'moneyMGMT') {
        MMboardAll.value = ''
      } else if (boardName === 'local') {
        LboardAll.value = ''
      }
  })
  }


  return { MMboardAll, MMboardDetail, LboardAll, LboardDetail, getBoards}
}, { persist: true })