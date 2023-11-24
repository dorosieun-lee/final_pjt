<script setup>
import ArticleList from '@/components/ArticleList.vue';
import IndexList from '@/components/IndexList.vue';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { userCheckStore } from '@/stores/usercheck';
import { useBoardStore } from '@/stores/board';
import MMBoardList from '@/components/MMBoardList.vue';
import LBoardList from '@/components/LBoardList.vue';
import Quiz from '@/components/Quiz.vue';
import Carousel from '@/components/Carousel.vue';
import MainProfile from '@/components/MainProfile.vue';
import ExchangeRate from '@/components/ExchangeRate.vue';

const userStore = userCheckStore()
const boardStore = useBoardStore()
const articles = ref(null)
const index = ref(null)
const kospi = ref(null)
const quizAll = ref(null)
const quiz = ref(null)

const loadCrawlingData = function () {
    axios({
        method: 'get',
        url: `${userStore.API_URL}/api/v1/mainpage/`
    })
    .then((res) => {
        // console.log(res.data)
        articles.value = res.data.news_data
        index.value = res.data.index_data
    })
    .catch((err) => {
        console.log(err)
    })
}


const loadKOSPIData = function () {
    axios({
        method: 'get',
        url: `${userStore.API_URL}/api/v1/mainpage/kospi/`
    })
    .then((res) => {
        // console.log(res.data)
        kospi.value = res.data
    })
    .catch((err) => {
        console.log(err)
    })
}

const getRandomQuiz = () => {
    axios({
        method: 'get',
        url: `${userStore.API_URL}/api/v1/quiz/`
    })
    .then((res) => {
        quizAll.value = res.data
        const randomIdx = Math.floor(Math.random() * quizAll.value.length)
        quiz.value = quizAll.value[randomIdx]
    })
    .catch((err) => {
        console.log(err)
        quizAll.value = null
    })
}


onMounted(() => {
    loadCrawlingData()
    loadKOSPIData()
    boardStore.getBoards('moneyMGMT')
    boardStore.getBoards('local')
    getRandomQuiz()
})

</script>

<template>
    <div class="outer">
        <div class="container1 mx-5">
            <div class="row">
                <Carousel class="col-lg-9"/>
                <div class="col-lg-3">
                    <MainProfile class="profile-box" style="height: 40%;"/>
                    <ExchangeRate class="my-2 exchange-rate-main" style="height: 59%;"/>
                </div>
            </div>
        </div>
        <exchangeRate class="exchange-rate-sub"/>
        <div class="container2">
            <div class="row">
                <ArticleList :articles="articles" class="col-lg-4"/>
                <div class="col-lg-3 d-flex flex-column align-content-between">
                    <MMBoardList class="h-50 MMBoard mb-5"/>
                    <LBoardList class="h-50 LBoard"/>
                </div>
                <div class="col-lg-5">
                    <Quiz :quiz="quiz" @change-quiz="getRandomQuiz" class="quiz"/>
                    <IndexList :index="index" :kospi="kospi" class="indexList"/>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>

.container1 {
    /* height: 6rem; */
}

.container2 {
    /* height: 20rem; */
    margin: 3.5rem;
}
.MMBoard {
    background-color: #d7fff6;
    border-radius: 10px;
    padding: 20px;
}

.LBoard {
    background-color: #d5ffee;
    border-radius: 10px;
    padding: 20px;
}

.quiz {
    /* display: grid;
    place-items: center;
    background-color: #00B992;
    color: white;
    border-radius: 10px; */
    height: 35%;
}

.indexList {
    margin-top: 3rem;
    /* height: 59%; */
    border: gray 3px solid;
    border-radius: 10px;
}

.exchange-rate-sub {
        display: none; 
}

@media (max-width: 1700px) {
    .exchange-rate-main {
        display: none;
    }
    .exchange-rate-sub {
        display: block;
        height: 22rem;
        margin: 2rem 4rem;
    }
    .profile-box {
        height: 17rem !important;
    }
}

@media (max-width: 980px) {
    div {
        margin-top: 2rem;
    }

    .exchange-rate-main {
        height: 22rem !important;
    }

    .profile-box {
        height: 15rem !important;
    }
}

</style>
