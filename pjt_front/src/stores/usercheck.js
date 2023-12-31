import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'
import axios from 'axios'

export const userCheckStore = defineStore('usercheck', () => {
  // const API_URL = 'http://127.0.0.1:8000'
  const API_URL = 'http://3.144.139.49'
  const token = ref('')

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    }
    else {
      return true
    }
  })

  const userId = ref(null)
  const router = useRouter()
  const isSuperuser = ref(null)

  const signUp = function (payload) {
    // 구조 분해할당
    const { username, password1, password2, email } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, email
      }
    })
      .then((res) => {
        console.log('회원가입 완료')
        logIn({ username: username, password: password1 })
        router.push({name: 'home'})
        window.alert('FINDY의 회원가입을 환영합니다. \n 개인정보 수정에서 상세 내용을 수정하고 추천 상품을 받아보세요.')
      })
      .catch((err) => {
        console.log(err)
        window.alert("비밀번호가 너무 짧거나, 숫자로만 구성되어 있습니다. 비밀번호는 8글자 이상이며, 영문과 숫자가 섞여야 합니다.")
      })
  }

  const checkSuperUser = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/accounts/check_superuser/`,
      headers: {
          Authorization: `Token ${token.value}`
      }
    })
    .then((res) => {
      isSuperuser.value = res.data.is_superuser == 1 ? true : false
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 완료')
        token.value = res.data.key
        userId.value = username
        // console.log(res)
        checkSuperUser()
        router.push({name: 'home'})
        // router.go(-1)
      })
      .catch((err) => {
        console.log(err)
        window.alert('아이디 또는 비밀번호가 틀렸습니다.')
      })
  }


  const withdraw = function () {
    const answer = window.confirm("회원탈퇴 하시겠습니까?")
    if (answer) {
      const re_answer = window.confirm("정말 회원탈퇴 하시겠습니까?")
      if (re_answer) {
        const re_re_answer = window.confirm("정말 정말 떠나시겠습니까? 모든 정보는 지워집니다.")
        if (re_re_answer) {
          axios({
            method: 'delete',
            url: `${API_URL}/api/v1/accounts/withdraw/`,
            headers: {
                Authorization: `Token ${token.value}`
            }
          })
          .then((res) => {
            token.value = null
            userId.value = null
            window.alert("회원탈퇴 되었습니다. 안녕히 가십시요.")
          })
          .catch((err) => {
            console.log(err)
          })
        }
      }
    }
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`
    })
      .then((res) => {
        console.log('로그아웃 완료')
        token.value = null
        userId.value = null
        router.push({ name: 'home'})
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const changePassword = function (payload) {
    const { new_password1, new_password2, old_password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/password/change/`,
      data: {
        new_password1, new_password2, old_password
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        window.alert('비밀번호가 변경되었습니다.')
        router.go(-1)
      })
      .catch((err) => {
        console.log(err)
        // console.log(JSON.parse(err.request.response)['new_password2'])
        window.alert("비밀번호가 너무 짧거나, 숫자로만 구성되어 있습니다. 비밀번호는 8글자 이상이며, 영문과 숫자가 섞여야 합니다.")
        // if (err.data) {request.response}
        // {"new_password2":["This password is too short. It must contain at least 8 characters.","This password is too common.","This password is entirely numeric."]}
      })
  }

  return { API_URL, signUp, logIn, token, isLogin, logOut, 
    userId, withdraw, isSuperuser, changePassword }
}, { persist: true })