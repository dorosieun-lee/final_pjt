<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios';
import { userCheckStore } from '@/stores/usercheck'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()

const goDetailMM = function (pk) {
    router.push({name: 'moneyMGMTDetail', params: {board_pk: pk}})
}

const goDetailLocal = function (pk) {
    router.push({name: 'localDetail', params: {board_pk: pk}})
}

const store = userCheckStore()
const articles = ref('')

const getLog = () => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/boards/user_log/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
        .then((res) => {
            // console.log(res.data)
            articles.value = res.data
        })
        .catch((err) => {
            console.log(err)
        })
}
onMounted(() => {
  getLog()
})

const formatDate = function (dateString) {
    const date = new Date(dateString)
    const year = date.getFullYear()
    const month = ('0' + (date.getMonth() + 1)).slice(-2)
    const day = ('0' + date.getDate()).slice(-2);
    const hours = ('0' + date.getHours()).slice(-2);
    const minutes = ('0' + date.getMinutes()).slice(-2);

    // Form the desired date string
    const formattedDate = year + '-' + month + '-' + day + ' ' + hours + ':' + minutes
    return formattedDate
}

</script>

<template>
  <div class="container">
    <h2>{{ store.userId }}님이 게시판에 작성한 글</h2>
    <div class="container my-3 mx-5">
      <h3 class="mt-4">제태크 정보 게시판에 작성한 글</h3>
      <div class="list-group">
        <div v-for="article in articles.mm_boards" :key="article.id" @click="goDetailMM(article.id)" class="list-group-item list-group-item-action d-flex justify-content-between">
          <p class="my-auto"><strong>제목 : </strong>{{ article.title }}</p>
          <p class="my-auto"><strong>작성일 : </strong>{{ formatDate(article.created_at) }}</p>
        </div>
      </div>
      <h3 class="mt-4">지역 커뮤니티 게시판에 작성한 글</h3>
      <div class="list-group">
        <div v-for="article in articles.l_boards" :key="article.id" @click="goDetailLocal(article.id)" class="list-group-item list-group-item-action d-flex justify-content-between">
          <p class="my-auto"><strong>제목 : </strong>{{ article.title }}</p>
          <p class="my-auto"><strong>작성일 : </strong>{{ formatDate(article.created_at) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
