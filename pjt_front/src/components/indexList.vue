<script setup>
import { ref, computed, watch } from 'vue'
const props = defineProps({
    index: Object,
    kospi: Object
})

const check = (item) => {
    const number = item.fluctuation.percent.trim()
    if (number[0] === '+') {
        return true
    } else {
        return false
    }
}
</script>

<template>
    <div class="p-4 container">
        <h2 class="fw-bold my-2">경제 지수</h2>
        <p class="d-flex justify-content-between"><span>환율과 유가, 금 시세는 당일 지수를, 코스피는 실시간 지수를 나타냅니다.</span><span>(출처: 네이버 증권)</span></p>
        <div class="row" v-if="index">
            <div v-for="idx in index" class='col-6 card'>
                <div class="card-body">
                    <strong class="card-title h5 fw-bold">{{ idx.name }}</strong>
                    <p class="card-subtitle fs-5 fw-bold">{{ idx.value }}</p>
                    <p class="card-text fs-5"><span :class="{up: check(idx), down: !check(idx)}">{{ idx.fluctuation.value }}</span> // {{ idx.fluctuation.percent }}% </p>
                </div>
            </div>
            <div v-if="kospi" class="col-12 card">
                <div class="card-body">
                    <strong class="card-title fs-4">{{ kospi.name }}</strong>
                    <p class="card-subtitle fs-5 fw-bold">{{ kospi.value }}</p>
                    <p class="card-text fs-5"><span :class="{up: check(kospi), down: !check(kospi)}">{{ kospi.fluctuation.value }}</span> // {{ kospi.fluctuation.percent }}% </p>
                </div>
            </div>
            <div v-else class="col-12 card">
                <div class="card-body">
                    <strong class="card-title fs-4">코스피</strong>
                    <p class="card-text">코스피 정보를 받아오는 중입니다.</p>
                </div>
            </div>
        </div>
        
        
    </div>
</template>

<style scoped>
.up {
    color: red;
}

.down {
    color: blue;
}

.card {
    height: 7.5rem;
}
</style>