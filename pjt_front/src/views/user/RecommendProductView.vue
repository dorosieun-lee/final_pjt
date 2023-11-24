<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import axios from 'axios';
import { userCheckStore } from '@/stores/usercheck'
import { compareBankStore } from '@/stores/compare_bank'
import { RouterLink, useRouter } from 'vue-router'

const router = useRouter()
const store = userCheckStore()
const bank_store = compareBankStore()

const recommend_products = ref('')

const goDetailDeposit = function (bank, id) {
    router.push({ name: 'DepositDetailView', params: { fin_prdt_cd: bank, id: id } })
}

const goDetailSaving = function (bank, id) {
    router.push({ name: 'SavingDetailView', params: { fin_prdt_cd: bank, id: id } })
}

const warning = ref('')
const isChart = ref(false)

const deposit_bank = ref([])
const saving_bank = ref([])


const saving_name = ref([])
const saving_rate = ref([])



const getRecommendation = () => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/bank-products/recommend/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
        })
        .then((res) => {
            recommend_products.value = res.data
            deposit_bank.value = res.data.deposit_products
            saving_bank.value = res.data.saving_products
            makeChart()
        })
        .catch((err) => {
            if (err.message === "Request failed with status code 500") {
                warning.value = "개인정보 수정 페이지에서 상세 정보를 작성해야 추천 상품을 받아볼 수 있습니다."
            }
        })
}
onMounted(() => {
    getRecommendation()
})



import { Bar } from 'vue-chartjs'
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale
} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)
ChartJS.defaults.font.size = 15
ChartJS.defaultFontFamily = 'Helvetica Neue'

const dpChartData = ref()
const dpChartOptions = ref()
const svChartData = ref()
const svChartOptions = ref()

const makeChart = function () {
    var depositName = []
    var depositIntr = []

    for (const data of deposit_bank.value) {
        depositName.push(data.fin_prdt_nm)
        const intrList = []
        for (const option of data.deposit_options) {
            intrList.push(option.intr_rate2)
        }
        depositIntr.push(Math.max(...intrList))
    }
    console.log(depositName)
    console.log(depositIntr)

    var savingName = []
    var savingIntr = []

    for (const data of saving_bank.value) {
        savingName.push(data.fin_prdt_nm)
        const intrList = []
        for (const option of data.saving_options) {
            intrList.push(option.intr_rate2)
        }
        savingIntr.push(Math.max(...intrList))
    }
    console.log(savingName)
    console.log(savingIntr)

    dpChartData.value = {
        labels: depositName,
        datasets: [
            {
                label: '최고우대금리',
                backgroundColor: '#24C3A1',
                data: depositIntr
            }
        ],
    }
    
    dpChartOptions.value = {
        type: 'bar',
        data: dpChartData.value,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        },
    }
    svChartData.value = {
        labels: savingName,
        datasets: [
            {
                label: '최고우대금리',
                backgroundColor: '#91E1D0',
                data: savingIntr
            }
        ],
    }
    
    svChartOptions.value = {
        type: 'bar',
        data: svChartData.value,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
        },
    }

    isChart.value = true
}

</script>

<template>
    <div class="container">
        <h2 class="my-auto"><img src="/assets/recommend.png" style="width: 50px;" alt=""> 예적금 상품 추천</h2>
        <div v-if="warning">
            <h4 style="color: red;" class="my-5">{{ warning }}</h4>
            <RouterLink :to="{ name: 'userdetail' }" class="btn btn-outline-primary">개인 정보 수정 페이지로 가기</RouterLink>
        </div>
        <div v-else class="my-5">
            <div v-if="recommend_products.filter === 'age_only'">
                <p class="fw-bold">{{ store.userId }}님과 나이대가 유사한 회원이 관심을 표시한 상품 목록입니다.</p>
                <p>추천 알고리즘에서 참고한 회원의
                    <span><strong>평균 자산</strong> : {{
                        Number(recommend_products.average_asset.toFixed(0)).toLocaleString('ko-KR') }} 원, </span>
                    <span><strong>평균 연봉</strong> : {{
                        Number(recommend_products.average_salary.toFixed(0)).toLocaleString('ko-KR') }} 원</span>
                </p>
            </div>
            <div v-if="recommend_products.filter === 'all'" class="my-3">
                <p class="fw-bold">{{ store.userId }}님과 나이대, 자산, 연봉, 주거래 은행, 저축 목표가 유사한 회원이 관심을 표시한 상품 목록입니다.</p>
                <p>추천 알고리즘에서 참고한 회원의
                    <span><strong>평균 자산</strong> : {{
                        Number(recommend_products.average_asset.toFixed(0)).toLocaleString('ko-KR') }} 원, </span>
                    <span><strong>평균 연봉</strong> : {{
                        Number(recommend_products.average_salary.toFixed(0)).toLocaleString('ko-KR') }} 원</span>
                </p>
            </div>

            <div class="mx-3 my-3">
                <h3>추천 예금 상품</h3>
                <div class="list-group">
                    <div v-for="deposit in recommend_products.deposit_products" :key="deposit.id"
                        class="list-group-item d-flex justify-content-between">
                        <div>[{{ deposit.kor_co_nm }}] {{ deposit.fin_prdt_nm }}</div>
                        <button @click="goDetailDeposit(deposit.fin_prdt_cd, deposit.id)"
                            class="btn btn-outline-primary btn-sm">상세 정보 보기</button>
                    </div>
                </div>
            </div>

        <div class="row" v-if="isChart">
            <div class="chart my-2">
                <Bar :data="dpChartData" :options="dpChartOptions" />
            </div>
        </div>

            <div class="mx-3 my-5">
                <h3>추천 적금 상품</h3>
                <div class="list-group">
                    <div v-for="saving in recommend_products.saving_products" :key="saving.id"
                        class="list-group-item d-flex justify-content-between">
                        <div>[{{ saving.kor_co_nm }}] {{ saving.fin_prdt_nm }}</div>
                        <button @click="goDetailSaving(saving.fin_prdt_cd, saving.id)"
                            class="btn btn-outline-primary btn-sm">상세 정보 보기</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="row" v-if="isChart">
            <div class="chart my-2">
                <Bar :data="svChartData" :options="svChartOptions" />
            </div>
        </div>
    </div>


</template>

<style scoped>
.container {
    padding: 50px;
    border-radius: 10px;
}

.chart {
    display: flex;
    justify-content: center;
    height: 25rem;
}
</style>
