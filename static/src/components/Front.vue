<template>
  <div class="container-fluid bg-warning pb-5">
  <div class="container-fluid text-white bg-primary pt-5 pb-5"><h1>Welcome to ticket booking app</h1></div>

  <div class="row mt-5 ms-5 me-5 pb-5">

    <div class="col-sm-6 mb-3 mb-sm-0">
      <div class="card pb-5 pt-4">
        <div class="card-body">
          <h5 class="card-title">Admin Block</h5>
          <p class="card-text"><router-link to="adminregister">Admin Registration</router-link></p>
          <p class="card-text"><router-link to="adminlogin">Admin Login </router-link></p>
        </div>
      </div>
    </div>

    <div class="col-sm-6">
      <div class="card pb-5 pt-4">
        <div class="card-body">
          <h5 class="card-title">User Block</h5>
          <p class="card-text"><router-link to="userregister">User Registration</router-link></p>
          <p class="card-text"><router-link to="userlogin">User Login </router-link></p>
        </div>
      </div>
    </div>

  </div>
</div>
</template>

<script>
import axios from 'axios'
export default{
    name:'Front',
    data(){
        return{
            msg:'Aryan'
        }
    },
    methods:{
        getResponse(){
            const path='http://localhost:5000/shark';
            axios.get(path)
            .then((res)=>{
                console.log(res.data)
                this.msg=res.data;
            })
            .catch((err)=>{
                console.error(err);
            })
        }
    },
    created(){
        this.getResponse();
    }
}
</script>