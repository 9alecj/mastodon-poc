<template>
  <div id="app">
    <nav class="navbar sticky-top navbar-light navbar-expand-lg"> <button class="navbar-toggler" type="button"
        data-toggle="collapse" data-target="#collapsibleNavbar"> <span class="navbar-toggler-icon"></span> </button>
      <div class="collapse navbar-collapse d-flex justify-content-center" id="collapsibleNavbar">
        <ul class="navbar-nav">
          <li class="nav-item px-3">
            <a class="nav-link" href="/">Public Posts</a>
          </li>
          <li class="nav-item px-3">
            <a class="nav-link" href="/trending-posts">Trending Posts</a>
          </li>
          <li class="nav-item px-3">
            <a class="nav-link" href="/trending-links">Trending Links</a>
          </li>
          <li class="nav-item px-3">
            <a class="nav-link" href="/trending-tags">Trending Tags</a>
          </li>
        </ul>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  text-align: center;
}

nav {
  background: #755BB9
}

.nav-link {
  font-size: 1em;
  color: #ffffff !important;
  font-weight: 500
}
</style>