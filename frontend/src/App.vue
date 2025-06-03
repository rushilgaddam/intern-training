<template>
  <div id="app">
    <Detections />
  </div>
</template>

<script>
import Detections from './components/Detections.vue'

export default {
  name: 'App',
  components: {
    Detections
  }
}
</script>

<style>
/* optional styling */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 40px;
}
</style>
