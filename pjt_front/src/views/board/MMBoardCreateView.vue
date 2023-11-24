<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { userCheckStore } from '@/stores/usercheck'
import { useBoardStore } from '@/stores/board'

const userStore = userCheckStore()
const boardStore = useBoardStore()

const isCreate = ref(true)
const router = useRouter()
const route = useRoute()

const title = ref(null)
const content = ref(null)

const createBoard = function () {
    axios({
        method: 'post',
        url: `${userStore.API_URL}/api/v1/boards/moneyMGMT/`,
        data: {
            title: title.value,
            content: content.value,
        },
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
    .then((res) => {
        console.log('게시글 생성 완료')
        router.push({name: 'moneyMGMTDetail', params: {board_pk: res.data.id}})
    })
    .catch((err) => {
        console.log(err)
    })

}


const updateBoard = function () {
    axios({
        method: 'put',
        url: `${userStore.API_URL}/api/v1/boards/moneyMGMT/${route.params.board_pk}/`,
        data: {
            title: title.value,
            content: content.value,
        },
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
    .then((res) => {
        console.log('게시글 수정 완료')
        router.push({name: 'moneyMGMTDetail', params: {board_pk: res.data.id}})
    })
    .catch((err) => {
        console.log(err)
    })
}


const handleSubmit = function () {
    // console.log(isCreate.value)
    if (isCreate.value) {
        createBoard()
    } else {
        updateBoard()
    }
}


if (route.name === 'moneyMGMTUpdate') {
    isCreate.value = false
    title.value = boardStore.MMboardDetail.title
    content.value = boardStore.MMboardDetail.content
} 
</script>

<template>
    <div class="container">
        <h2><img src="/assets/money_marker.png" alt="" style="width: 2.3rem;"> 재테크 정보</h2>
        <h3>게시글 생성</h3>
        <form @submit.prevent="handleSubmit">
            <div class="mx-1 my-2">
                <label for="title" class="fs-5">제목 : </label>
                <input type="text" id="title" v-model="title" class="form-control" placeholder="제목은 50자 이내로 간단히!">
            </div>
            <div class="mx-1 my-2">
                <label for="content" class="fs-5">내용 : </label>
                <textarea v-model="content" name="content" id="content" cols="30" rows="10" class="form-control" placeholder="내용은 게시판 주제에 맞게 부탁드려요~"></textarea>
            </div>
            <div class="d-flex justify-content-center">
                <button v-if="isCreate" type="submit" class="btn btn-primary my-2 px-4">생성</button>
                <button v-else class="btn btn-outline-primary my-2 px-4">수정</button>
            </div>
        </form>
    </div>
</template>

<style scoped>
.btn {
    display: inline-block;
    margin: auto;
}
</style>
