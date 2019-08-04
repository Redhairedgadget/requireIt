<template>
  <!--TODO: fix mobile view-->
  <v-container fluid fill-height jusitfy-center align-content-center>
    <v-layout wrap>

      <v-flex xs12 md6 m-5>
        <!--All available webapps-->
        <h2>Available web app types: </h2>
        <v-tabs color="black" center-active show-arrows v-model="tab">
          <v-tab v-for="app in webapps" :key="app.title">{{ app.title }}</v-tab>

          <v-tab-item v-for="app in webapps" :key="app.title">
            <v-card flat tile>
              <br>
              <h3 class="my-0 mx-2">Requirements: </h3>
              <v-card-text  xs12 md6>
                <v-checkbox v-for="req in app.requirements" v-if="req.obligatory == true" v-model="selected_reqs"
                            color="black"
                            :label="req.requirement"
                            :value="req.requirement"></v-checkbox>
              </v-card-text>
              <h3 class="my-0 mx-2">Tips: </h3>
              <v-card-text  xs12 md6>
                <v-checkbox v-for="req in app.requirements" v-if="req.obligatory == false" v-model="selected_reqs"
                            color="black"
                            :label="req.requirement"
                            :value="req.requirement"></v-checkbox>
              </v-card-text>
            </v-card>
          </v-tab-item>

        </v-tabs>
      </v-flex>

      <v-flex xs12 md6 m-5>
        <h2 >Additional requirements and tips based on your answers: </h2>
        <div class="mx-2">
          <v-checkbox v-for="req in reqs" v-if="req.obligatory == true" v-model="selected_reqs"
                      color="black"
                      :label="req.requirement"
                      :value="req.requirement"></v-checkbox>
        </div>
        <br>
        <h2>General requirements: </h2>
        <div class="mx-2">
          <v-checkbox v-for="req in general" v-if="req.obligatory == true" v-model="selected_reqs"
              color="black"
              :label="req.requirement"
              :value="req.requirement"></v-checkbox>
        </div>
      </v-flex>

      <v-flex xs12 md6 m-5>
        <h2 class="my-2">Do you want to add yours?</h2>
        <div class="mx-2">
          <v-checkbox v-for="req in entered_reqs" v-model="selected_reqs"
                color="black"
                :label="req.requirement"
                :value="req.requirement"></v-checkbox>
            <v-text-field
              label="Add requirement"
              color="black"
              v-model="entered"
              :value="entered"
            ></v-text-field>
          <v-btn :disabled="disable" small value="submit" v-on:click="addReq(app)">Add requirement</v-btn>
        </div>
      </v-flex>

      <v-flex xs12 md6 m-5>
        <h2 class="my-2">List of your chosen requirements</h2>
        <div class="mx-2" v-for="req in selected_reqs">
          <p>{{ req }}</p>
        </div>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>

  export default {
      name: 'result',
      data: function(){
          return{
              tab: null,
              selected_reqs: [],
              entered_reqs: [],
              entered: '',
              disable: true,
              reqs_count: this.webapps.length+this.reqs.length+this.general.length
          }
      },
      props: ["webapps", "reqs", "general"],
      methods:{
          addReq(){
              this.entered_reqs.push({id: this.reqs_count+1, requirement:this.entered});
              this.entered = '';
          },
      },
      watch:{
          entered: function () {
              if(this.entered != ''){
                  this.disable = false
              }
          },
      }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
