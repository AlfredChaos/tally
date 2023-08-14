<template>
  <div id="header">
    <h1>
      <router-link to="/">LOGO</router-link>
    </h1>
    <div class="avatar">
      <router-link to="/user">User</router-link>
    </div>
  </div>
  <div id="main">
      <router-view></router-view>
  </div>
</template>

<style>
html,
body,
ul,
li,
div,
h1 {
  padding: 0;
  margin: 0;
}
html,
body {
  height: 100%;
}
#app {
  font-family: Arial, Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}
#header {
  position: fixed;
  left: 0;
  top: 0;
  right: 0;
  display: flex;
  padding: 0 30px;
  align-items: center;
  justify-content: space-between;
  background: #000;
  color: #fff;
  height: 54px;
}

#header a {
  font-weight: bold;
  border-radius: 50%;
  display: inline-block;
  text-decoration: none;
  color: #fff;
  cursor: pointer;
}
#header .avatar a {
  width: 42px;
  height: 42px;
  line-height: 42px;
  background-color: #eee;
  color: #666;
}
#main {
  position: fixed;
  left: 0;
  top: 54px;
  display: flex;
  height: 100%;
  width: 100%;
}
</style>
