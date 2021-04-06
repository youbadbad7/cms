<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png">
        <HelloWorld msg="Welcome to Your Vue.js AppQAQ"/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'Home',
        components: {
            HelloWorld
        },
        data() {
            return {}
        },
        created() {
            this.init()
        },
        methods: {
            init() {
                //所有分类
                this.axios.get(`http://127.0.0.1:5000/api`)
                    .then((res) => {
                        console.log(res)
                    })
            },
        }
    }
</script>



