<template>
  <v-app dark>
    <v-app-bar app color="indigo darken-4">
      <v-app-bar-title class="text-h6">Object Detection Dashboard</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-img src="/static/dist/static/lighthouseavionics.png" class="logo" height="40" width="auto" />

    </v-app-bar>

    <v-main>
      <v-container fluid class="pa-6">
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card elevation="6" color="grey darken-3">
              <v-card-title class="text-h5 text-white">Live Video Feed</v-card-title>
              <v-card-text>
                <img :src="videoUrl" style="max-width: 100%; border-radius: 8px;" alt="Live video stream" />
              </v-card-text>

            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="6">
            <v-card elevation="6" color="grey darken-3">
              <v-card-title class="text-h6 text-white">History Stats</v-card-title>
              <v-card-text>
                <v-list dense>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Total Frames: {{ totalFrames }}</v-list-item-title>
                      <v-list-item-title>Total People Detected: {{ totalPeople }}</v-list-item-title>
                      <v-list-item-title>Average People/Frame: {{ averagePeople }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>

          <v-col cols="12" md="6">
            <v-card elevation="6" color="grey darken-3">
              <v-card-title class="text-h6 text-white">Current Stats</v-card-title>
              <v-card-text>
                <v-list dense>
                  <v-list-item>
                    <v-list-item-content>
                      <v-list-item-title>Current Frames: {{ currentFrames }}</v-list-item-title>
                      <v-list-item-title>Current People: {{ currentPeople }}</v-list-item-title>
                      <v-list-item-title>Current Average People: {{ currentAverage }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      videoUrl: "http://192.168.30.86:5001/video_feed",
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
      const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
      const ws = new WebSocket(protocol + window.location.host + '/ws/stats');


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

<style scoped>
.logo {
  cursor: pointer;
}

.v-card-title {
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}
</style>
