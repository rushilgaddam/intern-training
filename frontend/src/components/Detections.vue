<template>
  <div id = "app">
    <h2>Object Detection</h2>
    
    <div>
      <img :src="videoUrl" style = "width:640px; border: 2px solid #333"/>
    </div>

    <div>
      <h2>History</h2>
      <p><strong>Total Frames:</strong>{{totalFrames }}</p>
      <p><strong>Total People Detected:</strong>{{totalPeople }}</p>
      <p><strong>Average People/Frame:</strong>{{ averagePeople }}</p>
      <br>
      <h2>Curent</h2>
      <p><strong>Current Frames:</strong>{{currentFrames }}</p>
      <p><strong>Current People:</strong>{{currentPeople }}</p>
      <p><strong>Current Average People:</strong>{{ currentAverage }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      videoUrl: "http://localhost:5001/video_feed",
      totalFrames: 0,
      totalPeople: 0,
      averagePeople: 0,
      currentFrames: 0,
      currentPeople: 0,
      currentAverage: 0,
      socket: null
    }
  },
  methods: {
    initWebSocket () {
      const ws = new WebSocket("ws://localhost:8000/ws/stats");

      ws.onopen = () => {
        console.log("WebSocket connection established")
      }

      ws.onmessage = (event) => {
        const data = JSON.parse(event.data)
        this.totalFrames = data.total_frames
        this.totalPeople = data.total_people
        this.averagePeople = data.average_people
        this.currentFrames = data.current_total_frames
        this.currentPeople = data.current_people
        this.currentAverage = data.current_average
      }

      ws.onerror = (error) => {
        console.error("WebSocket error", error)
      }

      this.socket = ws
    }
  },
  mounted () {
    this.initWebSocket()
  }
}

</script>
<style>
#app {
  background-color: #1e3a8a; 
  color: #e0f2fe; 
  min-height: 100vh;
  padding: 20px;
  font-family: Arial, sans-serif;
}

h2 {
  color: #93c5fd; 
}

p {
  font-size: 16px;
}
</style>


