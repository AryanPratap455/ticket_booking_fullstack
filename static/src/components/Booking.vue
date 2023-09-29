<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">User Dashboard</a>
            <a class="btn btn-dark text-light" href="/userhome" role="button">Home</a>
            <a class="navbar-brand" href="#">Logout</a>
        </div>
    </nav>

    <div class="bg-warning mt-2 mb-2 pt-3 pb-3 ms-5 me-5">
        <div class="text-danger">
            <h3>The booked show is here</h3>
        </div>
    </div>

    <div class="card m-5" v-for="block in deta">
        <div class="card-header bg-success text-white">
            Venue-{{ block.venue_name }}
        </div>
        <div class="card-body bg-primary text-white">
            <blockquote class="blockquote mb-0">
                <p style="float:left; ">Show name-{{block.shows_name}}</p>
                <p style="float:left; margin-left:30%; margin-right:20%">Date and time-{{block.time}}</p>
                <p>Rating-{{block.rating}}</p>
            </blockquote>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    name: 'Booking',
    data: function () {
        return {
            deta: ""
        }
    },
    methods: {
        getResponse() {
            const path = `http://localhost:5000/booking`;
            axios.get(path)
                .then((res) => {
                    console.log(res.data);
                    this.deta = res.data;
                })
                .catch((err) => {
                    console.error(err);
                })
        },
    },
    created() {
        this.getResponse();
    }
}
</script>
