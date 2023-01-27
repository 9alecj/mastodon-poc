<template>
  <div id="app">
    <nav>
      <ul class="nav justify-content-center">
        <li class="nav-item">
          <a class="nav-link" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/public">Public</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/trending-statuses">Trending</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/trending-links">Trending Links</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/trends">Trends</a>
        </li>
      </ul>
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