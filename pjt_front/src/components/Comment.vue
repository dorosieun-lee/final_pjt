<script setup>
import axios from 'axios';

import { userCheckStore } from '@/stores/usercheck'
import { useBoardStore } from '@/stores/board'


const props = defineProps({
    commentInfo: Object,
    boardName: String
})

const userStore = userCheckStore()

const boardStore = useBoardStore()

const emit = defineEmits(['deleteComment'])

const deleteComment = function () {
    axios({
        method: 'delete',
        url: `${userStore.API_URL}/api/v1/boards/${props['boardName']}/comments/${props['commentInfo'].id}`,
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
    .then((res) => {
        console.log('댓글 삭제')
        emit("deleteComment")
    })
    .catch((err) => {
        console.log(err)
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
    <div class="row my-1">
        <div class="d-flex col-8">
            <div v-if="props['boardName'] === 'moneyMGMT'" class="mx-1">{{ commentInfo.nickname ? commentInfo.nickname : "Unknown" }} - </div>
            <div v-if="props['boardName'] === 'local'" class="mx-1">{{ commentInfo.address ? commentInfo.address.split(' ')[0] : "Unknown" }} - </div>
            <div class="mx-1">{{ commentInfo.content }}</div>
        </div>
        <p class="col-2 my-auto">{{ formatDate(commentInfo.created_at) }}</p>
        <button v-if="commentInfo.user.username === userStore.userId" @click="deleteComment" class="btn btn-outline-danger btn-sm col-1">삭제</button>
    </div>
</template>

<style scoped>

</style>

