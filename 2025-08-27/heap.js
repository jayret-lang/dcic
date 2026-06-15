
// http://stackoverflow.com/questions/4270485/drawing-lines-on-html-page
function DrawLine(on, x1, y1, x2, y2){

    if(y1 < y2){
        var pom = y1;
        y1 = y2;
        y2 = pom;
        pom = x1;
        x1 = x2;
        x2 = pom;
    }

    var a = Math.abs(x1-x2);
    var b = Math.abs(y1-y2);
    var c;
    var sx = (x1+x2)/2 ;
    var sy = (y1+y2)/2 ;
    var width = Math.sqrt(a*a + b*b ) ;
    var x = sx - width/2;
    var y = sy;

    a = width / 2;

    c = Math.abs(sx-x);

    b = Math.sqrt(Math.abs(x1-x)*Math.abs(x1-x)+Math.abs(y1-y)*Math.abs(y1-y) );

    var cosb = (b*b - a*a - c*c) / (2*a*c);
    var rad = Math.acos(cosb);
    var deg = (rad*180)/Math.PI

    htmlns = "http://www.w3.org/1999/xhtml";
    div = document.createElementNS(htmlns, "div");
    div.setAttribute('style','z-index: 0;border:1px solid #aaa;width:'+width+'px;height:0px;-moz-transform:rotate('+deg+'deg);-webkit-transform:rotate('+deg+'deg);position:absolute;top:'+y+'px;left:'+x+'px;');   

    on.appendChild(div);
    return div;

}
// https://github.com/brownplt/code.pyret.org/blob/horizon/src/web/js/output-ui.js (Thanks Jack!)
// https://blog.brownplt.org/2018/06/11/philogenic-colors.html
var converter = $.colorspaces.converter('CIELAB', 'hex');

function hueToRGB(hue) {
  var a = 40*Math.cos(hue);
  var b = 40*Math.sin(hue)
  return converter([74, a, b]);
}

var goldenAngle = 2.39996322972865332;
var lastHue = 0;

var makePalette = function(){
  var palette = new Map();
  return function(n){
    if(!palette.has(n)) {
      lastHue = (lastHue + goldenAngle)%(Math.PI*2.0);
      palette.set(n, lastHue);
    }
    return palette.get(n);
  };};

jQuery(document).ready(function($) {
  var frames = $(".HeapExpr");
  frames.each(function(_, f) {
    var palette = makePalette();
    var refs = $(f).find(".heapref");
    refs.each(function(_, elt) {
      var id = elt.textContent;
      $(elt).attr("style", "color: " + hueToRGB(palette(id)));
    });
    var targets = $(f).find("span.sink");
    targets.each(function(_, t) {
      var id = $(t).text();
      $(t).addClass("loc");
      var source = $(f).find("span.source:contains('" + id + "')");
      var tline;
      var sline;
      t = $(t);
      t.hover(
        function() {
          tline = DrawLine(
            f,
            t.offset().left + 3,
            t.offset().top + 5,
            source.offset().left + 3,
            source.offset().top + 5);
        },
        function() {
          f.removeChild(tline);
        });
      source.hover(
        function() {
          sline = DrawLine(
            f,
            source.offset().left + 3,
            source.offset().top + 5,
            t.offset().left + 3,
            t.offset().top + 5);
        },
        function() {
          f.removeChild(sline);
        });
    });
  });
});
