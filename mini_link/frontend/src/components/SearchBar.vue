<template>
  <div class="container _align-bottom">
    <h1>Mini Link</h1>
    <!--url shortner form -->
    <form @submit.prevent="createAUrl()">
      <i-input type="url" v-model="urlToSend" placeholder="Enter a url">
        <i-button type="submit" slot="append">Shorten</i-button>
      </i-input>
    </form>
    <!-- links previews-->
    <div class="urls _display-flex _justify-content-space-between">
      <link-prevue
        :showButton="false"
        v-for="url in myUrls"
        v-on:click.native="shareDialog(url.shortend)"
        :cardWidth="`8em`"
        :url="url.long"
      ></link-prevue>
    </div>
    <!--Share url model-->
    <i-modal v-model="modal">
      <template slot="header">Share Url</template>
      You shortend URL is here:
      <a target="_blank" :href="selectedUrl">{{ selectedUrl }}</a>
      <br>
      <div class="_display-flex _justify-content-center">
        <qr-code :text="selectedUrl" />
      </div>
    </i-modal>
  </div>
</template>

<script>
import VueQRCodeComponent from "vue-qrcode-component";
import LinkPrevue from "link-prevue";
import axios from "axios";

export default {
  name: "SearchBar",
  components: {
    LinkPrevue,
  },
  data() {
    return {
      urlToSend: null,
      UrlShortend: null,
      myUrls: [],
      selectedUrl: null,
      errors: null,
      modal: false,
    };
  },
  methods: {
    createAUrl() {
      let options = {
        url: this.urlToSend,

        headers: {
          "Content-Type": "application/json",
        },
      };
      axios
        .post("/api/links/create/", { url: this.urlToSend })
        .then((response) => {
          this.myUrls.push({
            long: this.urlToSend,
            shortend: response.data.url,
          });
        });
    },
    shareDialog(url) {
      this.modal = true;
      this.selectedUrl = url;
    },
  },
};
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
}
.container {
  width: 60%;
}
.urls {
  margin-top: 10%;
  margin-bottom: 20%;
}
</style>
