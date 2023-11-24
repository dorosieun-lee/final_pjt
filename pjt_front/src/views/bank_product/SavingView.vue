<script setup>
import { compareBankStore } from '@/stores/compare_bank'
import { onMounted } from 'vue'
import SavingList from '@/components/SavingList.vue'

const store = compareBankStore()

onMounted(() => {
    store.Saving_list()
})

</script>

<template>
    <div>
        <SavingList />
    </div>
</template>

<style scoped></style>
