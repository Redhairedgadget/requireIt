<template>
    <transition
    name="fade"
    mode="out-in"
    >
        <v-container fill-height jusitfy-center align-content-center :key="currentQuestion">
            <v-layout wrap>

                <v-flex id="list" xs12>
                    <h1>{{ questions[currentQuestion].question }}</h1>

                    <v-radio-group v-model="chosen" v-for="option in questions[currentQuestion].options">
                        <v-radio
                               :label="option"
                               :value="option"
                               color="black"
                        />
                    </v-radio-group>
                    <v-btn rounded color="secondary" v-if="currentQuestion!=questions.length-1" @click="onNext()">
                        Next
                    </v-btn>
                    <!--TODO: check if array has empty entries onClick-->
                    <v-btn rounded color="secondary" v-if="currentQuestion==questions.length-1" @click="getWebapps()">
                        Finish
                    </v-btn>
                    <v-btn rounded v-if="currentQuestion>0" @click="onBack()">Prev</v-btn>
                </v-flex>
            </v-layout>
        </v-container>
    </transition>
</template>

<script>
    import { mapGetters } from 'vuex'

    export default {
        name: 'questionnaire',
        data: function () {
            return{
                chosen: undefined,
                questions:[
                    {question: "What is your industry?", options:['Business', 'Media', 'Entertainment', 'Education', 'NGO']},
                    {question: "What is your revenue model?", options:['Advertisement', 'One-time payments', 'Subscription plans']},
                    {question: "Is your application local or global?", options:['Local', 'Global']},
                    {question: "What age is your target audience?", options:['Children, teenagers', 'Young adults without children', 'Families', 'Elderly']},
                    {question: "What is the scope of your application?", options:['Community/Niche', 'Generation', 'Everyone']},
                ],
                answers: [],
                currentQuestion: 0,
              }
        },
        methods: {
            onNext: function(){
                if(this.currentQuestion == 0 && this.answers[this.currentQuestion]=="Business"){
                    this.answers[this.currentQuestion+1]= 'bspecial';
                    this.currentQuestion+=2;
                }else{
                    this.currentQuestion++;
                }
                if(this.answers[this.currentQuestion] == undefined){
                    this.chosen = this.questions[this.currentQuestion].options[0]
                }else{
                    this.chosen = this.answers[this.currentQuestion]
                }
            },

            onBack: function () {
                if(this.answers[0] == "Business" && this.currentQuestion-1 =="1"){
                    this.currentQuestion--;
                }
                this.currentQuestion--;
                this.chosen = this.answers[this.currentQuestion];
            },
            getWebapps: function () {
                this.$store.dispatch('getWebApps', {data: this.answers});
            }
        },
        watch:{
            chosen: function(){
                this.answers[this.currentQuestion] = this.chosen;
            }
        },
        computed:{
            ...mapGetters(['webapps'])
        },
        beforeMount(){
            this.answers = new Array(this.questions.length)
            this.chosen = this.questions[this.currentQuestion].options[0]
        }
    }
</script>

<style>

    .fade-enter-active,
    .fade-leave-active {
    transition-duration: 0.3s;
    transition-property: opacity;
    transition-timing-function: ease;
    }

    .fade-enter,
    .fade-leave-active {
    opacity: 0
    }

</style>