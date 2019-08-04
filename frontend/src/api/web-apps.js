import { HTTP } from "./common"
import router from "../router"

export const WebApp = {
    create(config){
        return HTTP.post('/webapps/', config).then(response =>{
            return response.data
        })
    },
    delete(webapp){
        return HTTP.delete('/webapps/${note.id}/')
    },
    list(data){
        return HTTP.get('/webapps/', {params: {
            data }
        }).then(response =>{
            console.log(response.data);
            router.push({name: 'result', params: {webapps: response.data.webapps, reqs: response.data.reqs,
                    general: response.data.general}})
        })
    }
}