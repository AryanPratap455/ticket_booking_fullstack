<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Admin Dashboard</a>
      <a class="navbar-brand" @click="logout">Logout</a>
    </div>
  </nav>

  <div class="bg-primary mt-4 mb-4 pt-3 pb-3">
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-warning text-dark" data-bs-toggle="modal" data-bs-target="#exampleModal">
      +Create more venue
    </button>

    <!-- Modal for creating venue -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Add more venue here</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="mb-2">
              <label>Name :</label>
              <input v-model="name" type="text">
            </div>
            <div class="mb-2">
              <label>Place :</label>
              <input v-model="place" type="text">
            </div>
            <div class="mb-2">
              <label>Location :</label>
              <input v-model="location" type="text">
            </div>
            <div class="mb-2">
              <label>Capacity :</label>
              <input v-model="capacity" type="integer">
            </div>

          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" @click="addvenue" class="btn btn-primary" data-bs-dismiss="modal">Submit</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!--  Model for creating show  -->

  <div class="modal fade" id="exampleModal_show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Add more show here</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="mb-2">
            <label>Show name :</label>
            <input v-model="show_name" type="text">
          </div>
          <div class="mb-2">
            <label>Price :</label>
            <input v-model="price" type="integer">
          </div>
          <div class="mb-2">
            <label>Tags :</label>
            <input v-model="tags" type="text">
          </div>
          <div class="mb-2">
            <label>Rating</label>
            <input v-model="rating" type="text">
          </div>
          <div class="mb-2">
            <label>Time :</label>
            <input v-model="time" type="datetime-local">
          </div>
          <div class="mb-2">
            <label>venue id :</label>
            <input v-model="venue_id" type="integer">
          </div>
        </div>

        <div class=" modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" @click="addshow" class="btn btn-primary" data-bs-dismiss="modal">Submit</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Body part is below action on venue and show -->

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-5 mb-5 ms-5" v-for="ven in msg[0]">

        <!-- Modal for updating venue -->

        <div class="modal fade" id="UpdateVenue" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Change the data below for update venue</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="mb-2">
                  <label>Name :</label>
                  <input v-model="name" type="text">
                </div>
                <div class="mb-2">
                  <label>Place :</label>
                  <input v-model="place" type="text">
                </div>
                <div class="mb-2">
                  <label>Location :</label>
                  <input v-model="location" type="text">
                </div>
                <div class="mb-2">
                  <label>Capacity :</label>
                  <input v-model="capacity" type="integer">
                </div>

              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" @click="updateVenue(ven.id)" class="btn btn-primary"
                  data-bs-dismiss="modal">Submit</button>
              </div>
            </div>
          </div>
        </div>

        <!--  -->
        <div class="card">
          <div class="card-body bg-warning">
            <h3 class="card-title text-danger">Venue-{{ ven.id }}: {{ ven.venue_name }} , {{ ven.place }}</h3>
            <hr>
            <button type="button" class="btn btn-success mb-1" data-bs-toggle="modal"
              data-bs-target="#exampleModal_show">Create Show</button>

            <!-- inside each venue for action on show  -->

            <div class="row">
              <div style="float:left;" v-for="sho in msg[1]">

                <!-- Modal for updating  show  -->

                <div class="modal fade" id="UpdateShow" tabindex="-1" aria-labelledby="exampleModalLabel"
                  aria-hidden="true">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Change the data below for update show</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                        <div class="mb-2">
                          <label>Show name :</label>
                          <input v-model="show_name" type="text">
                        </div>
                        <div class="mb-2">
                          <label>Tags :</label>
                          <input v-model="tags" type="text">
                        </div>
                        <div class="mb-2">
                          <label>Price :</label>
                          <input v-model="price" type="integer">
                        </div>
                        <div class="mb-2">
                          <label>Time :</label>
                          <input v-model="time" type="datetime-local">
                        </div>
                        <div class="mb-2">
                          <label>Rating</label>
                          <input v-model="rating" type="integer">
                        </div>

                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" @click="updateShow(sho.show_id)" class="btn btn-primary"
                          data-bs-dismiss="modal">Submit</button>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="col-sm-6">
                  <div class="card" v-if="sho.venue_id_r == ven.id">
                    <div class="card-body">
                      <h5 class="card-title">{{ sho.show_name }} </h5>
                      <p class="card-text">{{ sho.time }}</p>
                      <button type="button" class="btn btn-primary text-white me-2 btn-sm" data-bs-toggle="modal"
                        data-bs-target="#UpdateShow">
                        Update
                      </button>
                      <button @click="deleteShow(sho.show_id)" class="btn btn-primary btn-sm">Delete</button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <hr>
            <button type="button" class="btn btn-primary text-white me-2" data-bs-toggle="modal"
              data-bs-target="#UpdateVenue">
              Update venue
            </button>
            <button @click="deleteVenue(ven.id)" class="btn btn-primary">Delete venue</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AdminHome',

  data: function () {
    return {
      msg: [],
      name: "",
      place: "",
      location: "",
      capacity: "",

      show_name: "",
      tags: "",
      price: "",
      rating: "",
      time: "",
      venue_id: ""

    }
  },

  methods: {
    getResponse() {
      const path = 'http://localhost:5000/venuedata';
      axios.get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        })
    },

    addvenue: function () {
      async function postJSON(data) {
        try {
          const response = await fetch("http://localhost:5000/createvenue", {
            method: "POST", // or 'PUT'
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          });

          const result = await response.json();
          console.log("Success:", result);
        } catch (error) {
          console.error("Error:", error);
        }
      }

      const data = {
        name: this.name,
        place: this.place,
        location: this.location,
        capacity: this.capacity
      };
      postJSON(data);

    },

    trigger_celery_job: function () {
      fetch(`/trigger_celery_job`)
        .then(r => r.json())
        .then(d => console.log("celery task details", d))
    },

    updateVenue: function (id) {
      async function postJSON(data) {
        try {
          const response = await fetch(`http://localhost:5000/updatevenue/${id}`, {
            method: "POST", // or 'PUT'
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          });

          const result = await response.json();
          console.log("Success:", result);
        } catch (error) {
          console.error("Error:", error);
        }
      }

      const data = {
        name: this.name,
        place: this.place,
        location: this.location,
        capacity: this.capacity
      };
      postJSON(data);
      console.log(id);

    },


    addshow: function () {
      async function postJSON(data) {
        try {
          const response = await fetch("http://localhost:5000/createshow", {
            method: "POST", // or 'PUT'
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          });

          const results = await response.json();
          console.log("Success:", results);
        } catch (error) {
          console.error("Error:", error);
        }
      }

      const deta = {
        show_name: this.show_name,
        price: this.price,
        rating: this.rating,
        time: this.time,
        tags: this.tags,
        venue_id: this.venue_id
      };
      postJSON(deta);

    },


    updateShow: function (show_id) {
      console.log(show_id)
      async function postJSON(data) {
        try {
          const response = await fetch(`http://localhost:5000/updateshow/${show_id}`, {
            method: "POST", // or 'PUT'
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          });

          const result = await response.json();
          console.log("Success:", result);
        } catch (error) {
          console.error("Error:", error);
        }
      }

      const data = {
        show_name: this.show_name,
        price: this.price,
        rating: this.rating,
        time: this.time,
        tags: this.tags
      };
      postJSON(data);

    },

    deleteVenue: function (id) {
      console.log(id);
      fetch(`http://localhost:5000/deletevenue/${id}`).then(r => r.json()).then(d => console.log(" Venue deleted"))
    },

    deleteShow: function (show_id) {
      console.log(show_id);
      fetch(`http://localhost:5000/deleteshow/${show_id}`).then(r => r.json()).then(d => console.log(" Show deleted"))
    },

    logout() {
      console.warn('Logout called');
      fetch(`http://localhost:5000/logoutadmin`)
        .then(r => r.json())
        .then(d => {
          console.log("Logout done");
          console.log(JSON.stringify(d)); // Log the JSON data
        });
      //localStorage.clear();
      this.$router.push({ name: 'AdminLogin' });
    }

  },

  created() {
    this.getResponse();
  }
}
</script>
