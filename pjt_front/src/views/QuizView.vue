<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { userCheckStore } from '@/stores/usercheck'
import Quiz from '@/components/Quiz.vue'

const userStore = userCheckStore()
const quizAll = ref(null)
const question = ref(null)
const answer = ref(null)

const getQuiz = () => {
    axios({
        method: 'get',
        url: `${userStore.API_URL}/api/v1/quiz/`
    })
    .then((res) => {
        quizAll.value = res.data
    })
    .catch((err) => {
        console.log(err)
        quizAll.value = null
    })
}

const createQuiz = () => {
    axios({
        method: 'post',
        url: `${userStore.API_URL}/api/v1/quiz/`,
        data: {
            question: question.value, 
            answer: answer.value
        }
    })
    .then((res) => {
        // console.log(res.data)
        getQuiz()
        question.value = null
        answer.value = null
    })
    .catch((err) => {
        console.log(err)
    })
}

onMounted(() => {
    getQuiz()
})
</script>

<template>
    <div class="container">
        <div>
            <h3>퀴즈 만들기</h3>
            <a href="https://sgsg.hankyung.com/sgplus/quiz">퀴즈 만들기 참고 사이트</a>
            <div>
                <label for="question">질문: </label>
                <input type="text" id="question" v-model="question" class="form-control">
                <label for="answer">정답: </label>
                <input type="text" id="answer" v-model="answer" class="form-control">
                <button @click="createQuiz" class="btn btn-primary my-2">퀴즈 생성</button>
            </div>
        </div>
        <div class="row">
            <Quiz v-for="quiz in quizAll" :quiz="quiz" @get-quiz="getQuiz()"/>
        </div>
    </div>
</template>

<style scoped>

</style>
