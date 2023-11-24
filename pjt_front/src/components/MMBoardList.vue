<script setup>
import { useBoardStore } from '@/stores/board'
import { useRouter } from 'vue-router';

const boardStore = useBoardStore()
const router = useRouter()

const goBoard = () => {
    router.push({name: 'moneyMGMT'})
}

const goDetail = function (pk) {
    router.push({name: 'moneyMGMTDetail', params: {board_pk: pk}})
}
</script>

<template>
    <div>
        <div class="d-flex justify-content-between mb-4">
            <h2 class="fw-bold">제태크 정보</h2>
            <button class="btn" @click="goBoard">더보기</button>
        </div>
        <ul v-if="boardStore.MMboardAll" class="p-0">
            <li v-for="board in boardStore.MMboardAll.slice(0, Math.min(boardStore.MMboardAll.length, 6))" style="list-style: none;">
                <div class="d-flex" @click="goDetail(board.id)">
                    <img style="height: 27px; margin: auto 0;" src="/assets/money_marker.png" alt="">
                    <p class="fs-5 mx-2 my-auto">{{ board.title }}</p>
                </div>
                <hr>
            </li>
        </ul>
        <ul v-else>
            <h5>게시글이 없습니다.</h5>
        </ul>
    </div>
</template>

<style scoped>

</style>