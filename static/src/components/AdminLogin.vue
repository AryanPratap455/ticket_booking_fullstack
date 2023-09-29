<template>
    <div class="container-fluid bg-warning pb-3">
        <div class="container-fluid text-white bg-primary pt-5 pb-5">
            <a class="btn btn-success mb-2 mt-0" style="float:left" href="/" role="button">Home</a>
            <h1>Admin Login Page</h1>
        </div>

        <div class="row mt-5 ms-5 me-5 pb-5">

            <div class="col-sm-6 mb-3 mb-sm-0 ms-5">
                <div class="card pb-5 pt-4">
                    <div class="card-body">
                        <h5 class="card-title">Login</h5>
                        <form>
                            <div class="email mt-3">
                                <label>Email :</label>
                                <input type="email" v-model="email" />
                            </div>
                            <div class="password mt-3">
                                <label>Passsword :</label>
                                <input type="password" v-model="password" />
                            </div>
                            <button type="button" @click="login" class="btn btn-primary mt-3">Login</button>
                        </form>
                        <p>Don't have account click here for register</p>
                        <p class="card-text"><router-link to="adminregister">Admin Registration</router-link></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'AdminLogin',
    data() {
        return {
            email: "",
            password: "",
            msg: ""
        }
    },
    methods: {
        async login() {
            if (!this.username && !this.password) {
                alert("Please enter both the username and the password !!")
                return ;
            }
            await axios.post('http://localhost:5000/loginadmin', {
                    email: this.email,
                    password: this.password,
                })
            .then((res) =>{
                if(res.data.status === "success"){
                    this.$router.push({name:'AdminHome'});
                    alert("Logged in successfully");
                }

                else{
                    console.log(res)
                    alert("Invalid email or password data !!");
                }
            })
            
        }
    },
}
</script>