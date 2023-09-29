import Front from './components/Front.vue'
import AdminHome from './components/AdminHome.vue'
import UserHome from './components/UserHome.vue'
import Booking from './components/Booking.vue'
import AdminRegister from './components/AdminRegister.vue'
import UserRegister from './components/UserRegister.vue'
import UserLogin from './components/UserLogin.vue'
import AdminLogin from './components/AdminLogin.vue'
import {createRouter, createWebHistory} from 'vue-router'

const routes=[
    {
        name:'Front', 
        component:Front,
        path:'/'
    },
    {
        name:'AdminHome',
        component:AdminHome,
        path:'/adminhome'
    },
    {
        name:'UserHome',
        component:UserHome,
        path:'/userhome'
    },
    {
        name:'Booking',
        component:Booking,
        path:'/booking'
    },
    {
        name:'AdminRegister',
        component:AdminRegister,
        path:'/adminregister'
    },
    {
        name:'UserRegister',
        component:UserRegister,
        path:'/userregister'
    },
    {
        name:'UserLogin',
        component:UserLogin,
        path:'/userlogin'
    },
    {
        name:'AdminLogin',
        component:AdminLogin,
        path:'/adminlogin'
    }
];

const router=createRouter({
    history:createWebHistory(),
    routes
});

export default router
