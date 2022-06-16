<template>
<div>
  <h1>Multitouch Reporter</h1>
  Reporting to {{ addr }}. <br/>
  Running: <input type="checkbox" v-model="running">
  <div style="touch-action: none" id="mainArea" v-touch:drag="eventChanger" v-touch:press="eventChanger" v-touch:release="eventChanger">
  <!-- <div style="touch-action: none" id="mainArea" v-touch:drag="eventChanger" v-touch:release="eventChanger"> -->
    <!-- <p>Coordinates: {{ coord }}</p> -->

    <p>Touches:</p>
    <ul>
      <li v-for="(touch, index) in touches">
        {{ index }}: [{{ parseInt(touch.clientX) }}, {{ parseInt(touch.clientY) }}]
      </li>
    </ul>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <!-- create vue-for -->

  </div>
</div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<script>
export default {
  data() {
    return {
      coord: '[0,0]',
      touches: null,
      event: null,
      running: true,
      addr: 'http://192.168.0.24:8000',
      changed: false,
    }
  },
  methods: {
    eventChanger(event) {
      this.event = event
      // event.preventDefault() // let's keep this commented, until necessary
      this.changed = true
    },
    updater() {
      if (this.changed==false) { return }
      let ev = this.event

      if (ev==null) { return } // null check
      if (!ev=="touchmove") { alert("Mouse move (or any other event) detected. This web app only supports touch.") }
      if (ev.targetTouches.length==0) { this.touches = ev.targetTouches; return } // not being touched
      this.touches = ev.targetTouches // update visualization
      // console.log(ev) // debug

      if (!this.running) { return }

      let touches = ev.targetTouches
      let touchList = new Array()
      for (let i = 0; i < touches.length; i++) { 
        let x = touches[i].clientX
        let y = touches[i].clientY
        touchList.push([x,y])
      }
      // this.axios.post(this.addr+'/touch', {"touchlist": touchList}).then((response) => {})
      this.axios.post(this.addr+'/touch', {touches: touchList}).then((response) => {})
      // this.axios.post(this.addr+'/test', {test: 1}).then((response) => {}) // debug: POST request
      // console.log(touchList) // debug
      this.changed = false
    },
  },
  mounted() {
    setInterval(this.updater, 30) // 60 fps
  },
}
</script>