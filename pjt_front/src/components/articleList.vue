<script setup>

const props = defineProps({
    articles: Object
})

const moveToArticle = function (link) {
    window.open(link)
}

const goNewMain = function () {
    window.open("https://m.stock.naver.com/investment/news/mainnews")
}
</script>

<template>
    <div class="container">
        <div class="d-flex justify-content-between">
            <h2 class="fw-bold">경제 뉴스</h2>
            <button class="btn" @click="goNewMain">더보기</button>
        </div>
        <p>뉴스 클릭 시, 새 탭으로 뉴스가 뜹니다</p>
        <ul v-if="articles">
            <li v-for="article in articles.slice(0, 5)" @click="moveToArticle(article.link)" class="row me-1">
                <img class="col-3 my-auto" :src="article.img_link" style="height: 100%;" alt="news_thumbnail">
                <div class="col-9">
                    <strong>{{ article.title }}</strong>
                    <p>{{ article.content.slice(0, 50) }}...</p>
                    <div class="d-flex justify-content-between"><p>{{ article.time }}</p><p>[{{ article.cite }}]</p></div>
                </div>
                <hr style="width: 95%;">
            </li>
        </ul>

        
    </div>
</template>

<style scoped>
.container {
    background-color: #F0EFEF;
    border-radius: 10px;
    padding: 10px;
}
</style>