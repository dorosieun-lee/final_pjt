<script setup>
import { ref } from 'vue'
import { userCheckStore } from '@/stores/usercheck'
import { useRoute } from 'vue-router';
import axios from 'axios'

const userAnswer = ref()
const userStore = userCheckStore()
const route = useRoute()
const emit = defineEmits(['getQuiz', 'changeQuiz'])
const props = defineProps({
    quiz: Object
})

const isMainPage = route.name === 'home' ? true : false
const isSubmit = ref(false)
const isRight = ref(false)

const deleteQuiz = function () {
    axios({
        method: 'delete',
        url: `${userStore.API_URL}/api/v1/quiz/${props['quiz'].id}/`,
    })
    .then((res) => {
        // console.log(res)
        emit('getQuiz')
    })
    .catch((err) => {
        console.log(err)
    })
}

const checkAnswer = () => {
    isSubmit.value = true
    if (userAnswer.value == props['quiz'].answer) {
        // window.alert('정답입니다')
        isRight.value = true
        userAnswer.value = null
        // 카드가 뒤집어지면서 정답 표출
    } else {
        // window.alert(`오답입니다. 정답은 ${props['quiz'].answer}입니다.`)
        isRight.value = false
        userAnswer.value = null
        // 카드가 뒤집어지면서 정답 표출
    }
}

const changeQuiz = () => {
    isSubmit.value = false
    emit('changeQuiz')
}

</script>

<template>
    <div v-if="isMainPage" :class="{quizBox: !isSubmit, answerRight: isSubmit && isRight, answerWrong: isSubmit && !isRight}">
        <div v-if="quiz" class="card">
            <div class="front" v-if="!isSubmit">
                <div class="text-center my-2">
                    <h2 class="fw-bold my-3">경제 퀴즈</h2>
                    <h4 class="mx-4 text-center">Q. {{ quiz.question }}</h4>
                    <div class="row">
                        <label for="userAnswer" class="fs-4 col-3 ms-2">정답 :</label>
                        <input type="text" id="userAnswer" v-model="userAnswer" class="form-control col-4">
                        <span class="fs-4 col-2">({{ quiz.answer.length }}자)</span>
                        <button @click="checkAnswer" class="btn btn-check-answer fw-bold col-2">정답 확인</button>
                    </div>
                    <button @click="changeQuiz" class="btn fw-bold fs-5 btn-change-quiz">퀴즈 바꾸기</button>
                </div>
            </div>
            <div class="back" v-else>
                <div class="right" v-if="isRight">
                    <h2 class="fw-bold my-3 text-center">경제 퀴즈</h2>
                    <h4 class="mx-4 text-center">{{ quiz.answer }}</h4>
                    <h4 class="mx-4 text-center">정답입니다.</h4>
                    <button @click="changeQuiz" class="btn fw-bold fs-5 btn-change-quiz">퀴즈 바꾸기</button>
                </div>
                <div class="wrong" v-else>
                    <h2 class="fw-bold my-3 text-center">경제 퀴즈</h2>
                    <h4 class="mx-4 text-center">오답입니다.</h4>
                    <h4 class="mx-4 text-center">정답은 {{ quiz.answer }} 입니다.</h4>
                    <button @click="changeQuiz" class="btn fw-bold fs-5 btn-change-quiz">퀴즈 바꾸기</button>
                </div>
            </div>    
        </div>
    </div>
    <div v-else style="border: 1px solid gray" class="card card-for-admin col-5">
        <div class="card-body">
            <h4 class="card-title">질문: {{ quiz.question }}</h4>
            <p class="card-content">정답: {{ quiz.answer }}</p>
            <button @click="deleteQuiz" class="btn btn-danger">삭제</button>
        </div>
    </div>
</template>

<style scoped>
.quizBox {
    display: grid;
    place-items: center;
    background-color: #00B992;
    border-radius: 10px;
    margin: 0;
}

.answerRight {
    display: grid;
    place-items: center;
    background-color: rgb(75, 201, 2);
    border-radius: 10px;
    margin: 0;
}

.answerWrong {
    display: grid;
    place-items: center;
    background-color: rgb(255, 37, 37);
    border-radius: 10px;
    margin: 0;
}

.card {
    border: none;
    display: grid;
    place-items: center;
    background-color: rgba(255, 255, 255, 0);
    color: white;
}

.btn-change-quiz {
    display: block;
    margin: 1rem auto;
}

.btn-check-answer {
    background-color:#00271f;
    color:white;
}

.card-for-admin {
    border: 1px gray solid;
    margin: 2rem;
    color: black;
}

.btn-danger {
    color: white;
}
</style>
