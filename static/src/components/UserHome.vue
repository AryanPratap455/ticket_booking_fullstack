<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">User Dashboard</a>
            <a class="btn btn-dark text-white" href="/booking" role="button">Booked</a>
            <input type="text" v-model="search" placeholder="search here">
            <a class="btn btn-dark text-white" @click="Search" role="button">Search</a>
            <a class="navbar-brand" @click="logout">Logout</a>
        </div>
    </nav>
    <div class="output">{{search.status}}</div><br>
    <div class="random" v-for="i in search.val">
        <a class="output" href="/userhome" role="button">{{i}}</a>
    </div>

    <!-- Modal for choosing seat and confirm booking -->

    <div class="card mt-4 ms-3 me-3" v-for="ven in coll[0]">
        <h5 class="card-header bg-primary text-white">venue-{{ ven.id }}</h5>
        <div class="card-body bg-warning">
            <!-- <p class="card-text">  </p>-->

            <div class="card me-4" style="width: 18rem;" v-for="sho in coll[1]">
                <div class="card" v-if="sho.venue_id_r == ven.id">
                    <div class="card-body-child pb-2">
                        <h5 class="card-title text-white">Show name:- {{ sho.show_name }}, {{ sho.tags }}</h5>
                        <p class="card-text">Date & Time : {{ sho.time }}
                            <hr>Price : {{ sho.price }}
                        </p>

                        <!--  Modal for confirm booking   -->

                        <div class="modal fade" id="bookShow" tabindex="-1" aria-labelledby="exampleModalLabel"
                            aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="exampleModalLabel">Enter the details here</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal"
                                            aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <div class="seat">Available seats :{{available}}</div>
                                        <div class="mb-2">
                                            <label>Number of seats :</label>
                                            <input v-model="seat_count" type="text">
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary"
                                            data-bs-dismiss="modal">Close</button>
                                        <button type="button" @click="book(sho.show_id)" class="btn btn-primary"
                                            data-bs-dismiss="modal">Confirm Book</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <button type="button" class="btn btn-success mb-1" data-bs-toggle="modal"
                        data-bs-target="#bookShow" @click="remain_seat(sho.show_id)">Book</button>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'UserHome',
    data: function () {
        return {
            coll: [],
            seat_count: '',
            available: '',
            search: ''
        }
    },
    methods: {
        getResponse() {
            const path = `http://localhost:5000/userhome`;
            axios.get(path)
                .then((res) => {
                    console.log(res.data);
                    this.coll = res.data;
                })
                .catch((err) => {
                    console.error(err);
                })
        },
        remain_seat: function(show_id) { // Accept the userId parameter
            console.log(show_id);
            const path = `http://localhost:5000/seat_remain/${show_id}`; // Include the ID in the path
            axios
                .get(path)
                .then((res) => {
                    console.log(res.data.available_seat);
                    this.available = res.data.available_seat;
                })
                .catch((err) => {
                    console.error(err);
                });
        },
        book: function (show_id) {
            if (this.seat_count > this.available){
                alert('You are trying to book more than available seat. Please enter less seat');
                return ;
            }
            if(this.available===0){
                alert('No seat is avialable, You cannot book now ');
                return ;
            }
            async function postJSON(data) {
                try {
                    const response = await fetch(`http://localhost:5000/bookshow/${show_id}`, {
                        method: "POST", // or 'PUT'
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data),
                    });

                    const result = await response.json();
                    console.log("Success:");
                } catch (error) {
                    console.error("Error:", error);
                }
            }

            const data = {
                seat_c: this.seat_count
            };
            postJSON(data);
            alert('Show has been booked');
        },

        Search: function () {
            const vm = this;
            async function postJSON(data) {
                try {
                    const response = await fetch(`http://localhost:5000/search`, {
                        method: "POST", // or 'PUT'
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(data),
                    });

                    const result = await response.json();
                    console.log(result.status);
                    vm.search = result;
                } catch (error) {
                    console.error("Error:", error);
                }
            }

            const data = {
                search: this.search
            };
            postJSON(data);
            //this.$router.push({ name: 'Search_output' });
        },

        logout() {
            console.warn('Logout called');
            fetch(`http://localhost:5000/logoutuser`)
                .then(r => r.json())
                .then(d => {
                    console.log("Logout done");
                    console.log(JSON.stringify(d)); // Log the JSON data
                });
            //localStorage.clear();
            this.$router.push({ name: 'UserLogin' });
        }

    },
    created() {
        this.getResponse();
    }
}
</script>

<style scoped>
.card-body-child {
    background-color: rgb(0, 132, 255);
}
</style>