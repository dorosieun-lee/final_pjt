<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-4">
        <h1 class="mb-4">비밀번호 변경</h1>
        <form @submit.prevent="changePassword">
          <div class="mb-3">
            <label for="old_password" class="form-label">현재 비밀번호 : </label>
            <input type="password" class="form-control" v-model.trim="old_password">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">새 비밀번호 :</label>
            <input type="password" class="form-control" v-model.trim="new_password1">
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">새 비밀번호 확인 :</label>
            <input type="password" class="form-control" v-model.trim="new_password2">
            <div v-if="new_password1 !== new_password2 && new_password2 !== null" class="text-danger">
              {{ warning }}
            </div>
          </div>
          <div class="text-center">
            <button type="submit" class="btn btn-primary">변경</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { userCheckStore } from '@/stores/usercheck'
const store = userCheckStore()

const new_password1 = ref(null)
const new_password2 = ref(null)
const old_password = ref(null)
const warning = ref('비밀번호가 일치하지 않습니다.')

const changePassword = function () {
  const payload = {
    new_password1: new_password1.value,
    new_password2: new_password2.value,
    old_password: old_password.value,
  }
  store.changePassword(payload)
}

</script>

<style></style>