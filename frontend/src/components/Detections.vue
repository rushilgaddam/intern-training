<template>
  <v-app dark>
    <v-app-bar app color="indigo darken-4">
      <v-app-bar-title class="text-h6">
        <v-icon left class="mr-2">mdi-cctv</v-icon>
        Object Detection Dashboard
      </v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-cog</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-account</v-icon>
      </v-btn>
      <v-img src="/static/dist/static/lighthouseavionics.png" class="logo" height="40" width="auto" />
    </v-app-bar>

    <v-row justify="center" class="mb-4">
      <v-col cols="12" md="6">
        <v-text-field
          v-model="backendIp"
          label="Enter Backend IP"
          placeholder="192.168.30.86"
          prepend-inner-icon="mdi-lan-connect"
          outlined
          dense
          hide-details
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-btn color="primary" @click="setVideoUrl">Connect</v-btn>
      </v-col>
    </v-row>


    <v-main>
      <v-container fluid class="pa-6">
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card elevation="6" color="grey darken-3">
              <v-card-title class="text-h5 text-white">
                <v-icon left class="mr-2">mdi-video</v-icon>
                Live Video Feed
              </v-card-title>
              <v-card-text>
                <img :src="videoUrl" style="max-width: 100%; border-radius: 8px;" alt="Live video stream" />
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="6">
            <v-card elevation="6" color="grey darken-3">
              <v-card-title class="text-h6 text-white">
                <v-icon left class="mr-2">mdi-history</v-icon>
                History Stats
              </v-card-title>
              <v-card-text>
                <v-list dense>
                  <v-list-item>
                    <v-list-item-icon><v-icon>mdi-counter</v-icon></v-list-item-icon>
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
              <v-card-title class="text-h6 text-white">
                <v-icon left class="mr-2">mdi-chart-line</v-icon>
                Current Stats
              </v-card-title>
              <v-card-text>
                <v-list dense>
                  <v-list-item>
                    <v-list-item-icon><v-icon>mdi-camera</v-icon></v-list-item-icon>
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
      backendIp: '',
      videoUrl: "",
      totalFrames: 0,
      totalPeople: 0,
      averagePeople: 0,
      currentFrames: 0,
      currentPeople: 0,
      currentAverage: 0,
      socket: null,
    }
  },
  methods: {
    setVideoUrl() {
      if (this.backendIp) {
        this.videoUrl = `http://${this.backendIp}:5001/video_feed`
      }
    },

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
