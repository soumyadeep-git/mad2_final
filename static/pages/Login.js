const Login = {
  template: `<div class="d-flex justify-content-center align-items-center vh-100">
  <div class="card shadow p-4 border rounded-3 ">
    <h3 class="card-title text-center mb-4">Login</h3>
    <div class="form-group mb-3">
      <input v-model="email" type="email" class="form-control" placeholder="Email" required/>
    </div>
    <div class="form-group mb-4">
      <input v-model="password" type="password" class="form-control" placeholder="Password" required/>
    </div>
    <button class="btn btn-primary w-100" @click="submitInfo">Submit</button>
  </div>
</div>`,
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {

    submitInfo() {
      console.log("clicked")
    }

  },
};


export default Login;
