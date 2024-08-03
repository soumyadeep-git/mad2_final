import Navbar from '../components/Navbar.js'
import Login from "../pages/Login.js";
import Logout from "../pages/Logout.js"

import Register from "../pages/Register.js"


const routes = [
  { path: "/login", component: Login },
  { path: "/logout", component: Logout },
  { path: "/register", component: Register }
  // { path: "/login", component: Login }
];


const router = new VueRouter({
  routes,
});

export default router; 
