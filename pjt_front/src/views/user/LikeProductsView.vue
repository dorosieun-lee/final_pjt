<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios';
import { userCheckStore } from '@/stores/usercheck'
import { useRouter } from 'vue-router'

const router = useRouter()

const goDetailDeposit = function (bank, id) {
  router.push({ name: 'DepositDetailView', params: { fin_prdt_cd: bank, id: id } })
}

const goDetailSaving = function (bank, id) {
  router.push({ name: 'SavingDetailView', params: { fin_prdt_cd: bank, id: id } })
}

const store = userCheckStore()
const products = ref('')

const getLikeBankProducts = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/accounts/like_list/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res.data)
      products.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}
onMounted(() => {
  getLikeBankProducts()
})

</script>

<template>
  <div class="container">

    <div>
      <h2>예금 모아보기</h2>


      <div class="row">
        <!-- Check if deposit list is not empty -->
        <template v-if="products.deposit_list && products.deposit_list.length">
          <div v-for="deposit in products.deposit_list" :key="deposit.id" class="col-lg-3 col-md-4 mb-4">
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">은행명 :</h5>
                <p class="card-text">{{ deposit.kor_co_nm }}</p>

                <h5 class="card-title">상품이름 :</h5>
                <p class="card-text">{{ deposit.fin_prdt_nm }}</p>

                <button @click="goDetailDeposit(deposit.fin_prdt_cd, deposit.id)" class="btn btn-primary">
                  상세정보
                </button>
              </div>
            </div>
          </div>
        </template>
        <!-- Display message if deposit list is empty -->
        <template v-else>
          <div class="col-12 mt-4">
            <p class="text-center"><strong>관심 예금 상품이 없습니다.</strong></p>
          </div>
        </template>
      </div>

      <div>
        <h2>적금 모아보기</h2>
        <div class="row">
          <template v-if="products.saving_list && products.saving_list.length">
            <div v-for="saving in products.saving_list" :key="saving.id" class="col-lg-3 col-md-4 mb-4">
              <div class="card">
                <div class="card-body">
                  <h5 class="card-title">은행명 :</h5>
                  <p class="card-text">{{ saving.kor_co_nm }}</p>

                  <h5 class="card-title">상품이름 :</h5>
                  <p class="card-text">{{ saving.fin_prdt_nm }}</p>

                  <button @click="goDetailSaving(saving.fin_prdt_cd, saving.id)" class="btn btn-primary">
                    상세정보
                  </button>
                </div>
              </div>
            </div>
          </template>
          <template v-else>
            <div class="col-12 mt-4">
              <p class="text-center"><strong>관심 적금 상품이 없습니다.</strong></p>
            </div>
          </template>
        </div>
      </div>
  
    </div>
  </div>
</template>

<style scoped>
.card {
  border: 1px solid;
  display: grid;
  place-items: center;
}
</style>