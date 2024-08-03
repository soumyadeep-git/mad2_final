export default {
  template: `<div>
            <h1>Login</h1>
            <form class="form">
              <div class="form-group">
                <label for="username" class="form-label">Username</label>
                <input type="text" id="username" name="username" class="form-control">
              </div>
              <div class="form-group">
                <label for="password" class="form-label">Password</label>
                <input type="password" id="password" name="password" class="form-control">
              </div>
              <div class="form-group">
                <button type="button" class="btn btn-primary">Login</button>
              </div>
            </form>
          </div>`,
};
