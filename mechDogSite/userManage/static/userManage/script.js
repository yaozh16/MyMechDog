
function iFrameHeight(o) {
    var ifm = document.getElementById("displayer");
    var subWeb = document.frames ?
      document.frames["displayer"].document :
      ifm.contentDocument;
    if (ifm != null && subWeb != null) {
        ifm.height = subWeb.body.scrollHeight;
    }
}
