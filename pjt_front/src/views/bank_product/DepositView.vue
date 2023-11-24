<script setup>
import { compareBankStore } from '@/stores/compare_bank'
import { onMounted } from 'vue'
import DepositList from '@/components/DepositList.vue'

const store = compareBankStore()

onMounted(() => {
    store.Deposit_list()
})


</script>

<template>
    <div>
        <DepositList />
    </div>
</template>

<style scoped></style>
