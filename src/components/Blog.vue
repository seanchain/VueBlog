<template>
  <div id="posts" class="row">
    <table class="col-9 offset-2 table">
      <tbody v-for="ary in json">
        <tr>
          <td><router-link :to="ary['link']">{{ary['title']}}</router-link></td>
          <td>{{ ary['link'].split('/')[2].split('-')[0] }} 年 {{ ary['link'].split('/')[2].split('-')[1] }} 月 {{ ary['link'].split('/')[2].split('-')[2] }} 日</td>
          </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'blog',
  data () {
    return {
      json: null
    }
  },
  created: function () {
    var _this = this
    this.$http.get('static/data.json').then(response => {
      console.log(response.body)
      _this.json = response.body
    }, response => {
      console.log('error here')
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .table {
    font-size: 1.1em;
    text-align: left;
  }

  #posts {
    margin-top: 30px;
  }


</style>
