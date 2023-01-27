<template>
  <div id="app">
      <nav class="navbar navbar-dark bg-dark navbar-expand-lg">
        <a class="navbar-brand" href="#">Mastodon Test</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item active">
              <a class="nav-link" href="/">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/public">Public</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/trending-statuses">Trending</a>
            </li>
          </ul>
        </div>
      </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #e2e1e0;
}
.navbar {
    /* What the docs use */
    --bs-navbar-padding-x: 0.5rem;
}
</style>