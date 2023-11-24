<script setup>
import axios from 'axios';
import { ref, watch } from 'vue'

import { userCheckStore } from '@/stores/usercheck'
import { useBoardStore } from '@/stores/board'


const comment = ref(null)
const userStore = userCheckStore()

const boardStore = useBoardStore()

const props = defineProps({
    boardName: String
})

const emit = defineEmits(['createComment'])

const createComment = function () {
    if (props['boardName'] === 'moneyMGMT') {
        var boardPk = boardStore.MMboardDetail.id
    } else if (props['boardName'] === 'local') {
        var boardPk = boardStore.LboardDetail.id
    } 
    
    axios({
        method: 'post',
        url: `${userStore.API_URL}/api/v1/boards/${props['boardName']}/${boardPk}/comments/`,
        data: {
            content: comment.value
        },
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
    .then((res) => {
        console.log('댓글 생성')
        emit('createComment')
        comment.value = ''
    })
    .catch((err) => {
        console.log(err)
    })
}

watch(comment, () => {
    if (comment.value.length > 200) {
        window.alert('댓글은 200자 이내로 작성해야 합니다')
        comment.value = comment.value.slice(0, 200)
    }
})
</script>

<template>
    <div>
        <form @submit.prevent="createComment" class="row mx-1">
            <input type="text" id="comment" v-model="comment" class="form-control col-md-8" placeholder="욕설/비방 댓글은 삭제될 수 있습니다. 댓글은 200자 이내로 남겨주세요.">
            <button type="submit" class="btn btn-secondary col-lg-1 col-md-2 col-sm-3">댓글 남기기</button>
        </form>
    </div>
</template>

<style scoped>
</style>
