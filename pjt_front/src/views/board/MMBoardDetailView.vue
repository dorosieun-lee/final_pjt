<script setup>
import { useRoute, useRouter, RouterLink } from 'vue-router'
import { ref, computed, watch, onMounted } from 'vue'
import axios from 'axios';


import { userCheckStore } from '@/stores/usercheck'
import { useBoardStore } from '@/stores/board'

import CreateComment from '@/components/CreateComment.vue';
import Comment from '@/components/Comment.vue';

const route = useRoute()
const router = useRouter()

const userStore = userCheckStore()
const boardStore = useBoardStore()

const board = ref(null)
const comments = ref(null)
const boardName = 'moneyMGMT'
const boardPk = route.params.board_pk

const getBoardDetail = function (boardName, boardPk) {
    if (userStore.userId == null) {
        router.push({name: 'login'})
    }
    axios({
        method: 'get',
        url: `${userStore.API_URL}/api/v1/boards/${boardName}/${boardPk}`,
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
    .then((res) => {
        console.log('상세 게시글 불러오기')
        board.value = res.data
        comments.value = res.data.mm_comment
        boardStore.MMboardDetail = res.data
    })
    .catch((err) => {
        console.log(err)
    })
}

onMounted(() => {
    getBoardDetail(boardName, boardPk)
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

const updateBoard = function () {
    router.push({name: 'moneyMGMTUpdate', params: {board_pk: boardPk}})
}

const deleteBoard = function () {
    axios({
        method: 'delete',
        url: `${userStore.API_URL}/api/v1/boards/moneyMGMT/${boardPk}/`,
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
    .then((res) => {
        console.log('게시글 삭제')
        router.push({name: 'moneyMGMT'})
    })
    .catch((err) => {
        console.log(err)
    })
}

</script>

<template>
    <div class="container">
        <h2><img src="/assets/money_marker.png" alt="" style="width: 2.3rem;"> 재테크 정보</h2>
        <div v-if="board" class="my-4">
            <!-- <p>{{ board.id }}번 게시글</p> -->
            <h3>제목 : {{ board.title }}</h3>
            <p class="fs-5">내용: </p>
            <p class="fs-5">{{ board.content }}</p>
            <p>작성자: {{ board.nickname ? board.nickname : "Unknown"}}</p>
            <p>작성일: {{ formatDate(board.created_at) }}</p>
            <p>최근 수정일: {{ formatDate(board.updated_at) }}</p>
        </div>
        <div v-if="board && (board.user.username === userStore.userId)">
            <button @click="updateBoard" class="mx-2 btn btn-outline-primary">수정</button>
            <button @click="deleteBoard" class="mx-2 btn btn-outline-danger">삭제</button>
        </div>
        <hr>
        <RouterLink :to="{name: 'moneyMGMT'}" style="text-decoration: none;">전체 게시글 보기</RouterLink>
        <hr>
        <CreateComment board-name="moneyMGMT" @create-comment="getBoardDetail(boardName, boardPk)"/>
        <ul class="list-group list-group-flush w-75">
            <li class="list-group-item">
                <Comment v-for="comment in comments" :key="comment ? comment.id : null" :comment-info="comment" :board-name="boardName" @delete-comment="getBoardDetail(boardName, boardPk)"/>
            </li>
        </ul>
    </div>
</template>

<style scoped>

</style>
