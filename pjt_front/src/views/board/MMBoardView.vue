<script setup>
import { ref, onMounted} from 'vue'
import axios from 'axios'


import { userCheckStore } from '@/stores/usercheck'
import { useBoardStore } from '@/stores/board'
import { RouterLink, useRouter } from 'vue-router'

const userStore = userCheckStore()
const boardStore = useBoardStore()
const router = useRouter()

const boardName = 'moneyMGMT'
const keyword = ref('')
const target = ref('')
const boards = ref()
const isSearch = ref(false)

onMounted(() => {
    boardStore.getBoards(boardName)
})


const goDetail = function (pk) {
    router.push({name: 'moneyMGMTDetail', params: {board_pk: pk}})
}

const search = () => {
    isSearch.value = true
    boards.value = boardStore.MMboardAll.filter((item) => {
        if (target.value === 'title') {
            if (item.title.includes(keyword.value)) {
                return item
            }
        }
        if (target.value === 'nickname') {
            if (item.nickname.includes(keyword.value)) {
                return item
            }
        }
    })
}

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
        <h2><img src="/assets/money_marker.png" alt="" style="width: 2.3rem;"> 재테크 정보</h2>
        <p class="my-0">게시판 주제에 맞는 게시글 작성을 부탁드립니다.</p>
        <p>게시글 작성 전, 개인정보 수정에서 닉네임 설정하기!</p>
        <RouterLink :to="{name: 'moneyMGMTCreate'}" class="btn btn-primary my-1">게시글 작성하기</RouterLink>
        <div class="row my-2" style="width: 50%">
            <label for="search" class="col-lg-3 my-auto mx-0">게시글 검색 : </label>
            <input type="text" id="search" v-model="keyword" class="form-control col-lg-4 col-sm-5">
            <select id="target" v-model="target" class="form-select col-lg-2 col-sm-4">
                <option value="title">제목</option>
                <option value="nickname">작성자</option>
            </select>
            <button @click="search" class="btn btn-secondary col-lg-2 col-sm-3">검색</button>
        </div>
        <ul class="list-group list-group-flush text-start" v-if="boardStore.MMboardAll">
            <li v-if="!isSearch" v-for="board in boardStore.MMboardAll" :key="board.id" class="list-group-item">
                <div class="row">
                    <p class="col-5 my-auto">제목: {{ board.title }}</p>
                    <p class="col-3 my-auto">작성일: {{ formatDate(board.created_at) }}</p>
                    <p class="col-2 my-auto">작성자: {{ board.nickname ? board.nickname : "Unknown"}}</p>
                    <button @click="goDetail(board.id)" class="btn btn-outline-secondary col-lg-1 col-sm-2">상세보기</button>
                </div>
            </li>
            <li v-else v-for="board in boards" :key="board.id" class="list-group-item">
                <div class="row">
                    <p class="col-5 my-auto">제목: {{ board.title }}</p>
                    <p class="col-3 my-auto">작성일: {{ formatDate(board.created_at) }}</p>
                    <p class="col-2 my-auto">작성자: {{ board.nickname ? board.nickname : "Unknown"}}</p>
                    <button @click="goDetail(board.id)" class="btn btn-outline-secondary col-lg-1 col-sm-2">상세보기</button>
                </div>
            </li>
        </ul>
        <div v-else>
            <p>게시글이 없습니다. 게시글을 작성해주세요.</p>
        </div>
    </div>
</template>

<style scoped>

</style>
