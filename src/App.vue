<template>
  <div id="app">
    <div class="row">
      <div class="col-2 offset-2"><h2 class="my_h2">/dev/random</h2></div>
      <div class="col-4"></div>
      <div class="col-4">
        <div class="my_header">
        <ul>
          <li><router-link to="/">博客</router-link></li>
          <li><router-link to="/about">关于</router-link></li>
        </ul>
        </div>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script src="/node_modules/shoelace-css/dist/shoelace.js"></script>
<script src="/node_modules/vue-resource/dist/vue-resource.min"></script>
<script>
export default {
  name: 'app',
  data () {
    return {
      json: null
    }
  },
  created: function () {
    var _this = this
    this.$http.get('http://localhost:3000/').then(response => {
      console.log(response.body)
      _this.json = response.body
    }, response => {
      console.log('error here')
    })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 40px;
}


h2.my_h2 {
  font-size: 2em;
}

div.my_header>ul {
  list-style-type: none;
  padding: 0;
}

div.my_header>ul>li {
  font-size: 1.2em;
  display: inline-block;
  margin: 0 10px;
}

</style>
